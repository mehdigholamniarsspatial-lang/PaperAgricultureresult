"""Convert the data-sources workbook into dashboard/data/data_sources.json (+ a copy of the workbook for download).

    python tools/import_sources.py "path/to/Ireland_agri_GHG_data_sources.xlsx"

Needs openpyxl at build time only; the dashboard itself reads the JSON.
"""
import json
import re
import shutil
import sys
from pathlib import Path

import openpyxl

OUT = Path(__file__).resolve().parents[1] / "dashboard" / "data"
HEADER = ["id", "group", "parameter", "description", "unit", "years", "dataset", "provider", "download", "docs", "role"]

# Analysis stage(s) each entry feeds, matched on the 'Role in the analysis' text (an entry may feed several).
TAGS = [
    ("Outcome", r"\bOutcome"),
    ("Decomposition (LMDI)", r"LMDI|^Activity"),
    ("ARDL controls & prices", r"ARDL|Deflator|real prices"),
    ("Regional DiD", r"DiD|regional panel|regional imputed|national and regional"),
    ("Policy indices", r"index P|index M|Policy-mix|coverage share|Inter-coder|policy M10"),
    ("Checks & harmonisation", r"check|reconciliation|Converts"),
    ("Robustness & supplements", r"robustness|GWP\*|Supplementary|ceiling"),
    ("Not used", r"^None"),
]
KIND = {"Policy codebooks": "Codebook", "Reference parameters": "Reference parameter", "Derived in notebook": "Derived variable"}


def years(s):
    m = re.match(r"(\d{4})\s*[–-]\s*(\d{4})?", s or "")
    if not m:
        return None, None
    return int(m.group(1)), int(m.group(2) or 2024)


def main(xlsx):
    ws = openpyxl.load_workbook(xlsx, data_only=True).active
    rows = list(ws.iter_rows(values_only=True))
    title, note = rows[0][0], rows[1][0]
    head = next(i for i, r in enumerate(rows) if r[0] == "#")
    items, prev_tags, prev_param = [], [], ""
    for r in rows[head + 1:]:
        if not isinstance(r[0], (int, float)):
            continue
        d = {k: ("" if v is None else str(v).strip()) for k, v in zip(HEADER, r)}
        d["id"] = int(r[0])
        m = re.match(r"\(as above(?:, (.*))?\)$", d["parameter"])
        if m:  # spell out the inherited parameter list so every card stands on its own
            d["parameter"] = prev_param + (f" ({m.group(1)})" if m.group(1) else "")
        else:
            prev_param = d["parameter"]
        tags = prev_tags if d["role"].startswith("As above") else [t for t, rx in TAGS if re.search(rx, d["role"])]
        d["tags"], prev_tags = tags, tags
        d["y0"], d["y1"] = years(d["years"])
        d["kind"] = KIND.get(d["group"], "Raw dataset")
        d["used"] = "Not used" not in tags
        for k in ("download", "docs"):
            if not d[k].startswith("http"):
                d[k + "_note"] = "" if d[k] in ("", "–") else d[k]
                d[k] = ""
        items.append(d)
    OUT.joinpath("data_sources.json").write_text(
        json.dumps({"title": title, "note": note, "items": items}, ensure_ascii=False, indent=1), encoding="utf-8")
    shutil.copyfile(xlsx, OUT / "data_sources.xlsx")
    print(f"{len(items)} entries -> {OUT / 'data_sources.json'}")


if __name__ == "__main__":
    main(sys.argv[1])
