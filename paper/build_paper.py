"""Build the research paper (.docx and .pdf) from paper_src.md.

Steps: number figures/tables and resolve {{fig:..}}/{{tab:..}} references, generate the dataset summary table from the
dashboard's data dictionary, convert with pandoc, then apply typography, table formatting, a table of contents and page
numbers in Microsoft Word (via COM), and export a PDF.

Usage:  python paper/build_paper.py
"""
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SRC = HERE / "paper_src.md"
MID = HERE / "_build" / "paper_processed.md"
OUT_DOCX = HERE / "Expansion_vs_Mitigation_Irish_Agri_GHG_paper.docx"
OUT_PDF = OUT_DOCX.with_suffix(".pdf")
FIG_DIR = HERE / "figures"

PAGEBREAK = '```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```'
TOCFIELD = ('```{=openxml}\n<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
            '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>Right-click and choose Update Field to build the table of contents.</w:t></w:r>'
            '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>\n```')


# ------------------------------------------------------------------ dataset summary table
def dictionary_table():
    spec = importlib.util.spec_from_file_location("data_store", ROOT / "dashboard" / "data_store.py")
    ds = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ds)
    dtype = {
        "kt CO₂e": "Continuous (annual flow)", "thousand head": "Count (June census)", "thousand LU": "Continuous (weighted count)",
        "LU per head": "Continuous (ratio)", "million litres": "Continuous (annual flow)", "litres per cow": "Continuous (ratio)",
        "%": "Continuous (percentage)", "kt N": "Continuous (annual flow)", "kg N/head/yr": "Continuous (rate)",
        "index, 2020 = 100": "Index (chain-linked, real)", "ratio": "Continuous (ratio)", "€ million, constant prices": "Continuous (monetary)",
        "index": "Composite index",
    }
    rows = ["| Group | Variable | Unit | Data type | Source | Coverage (*n*) | Role |",
            "|:---|:---|:---|:---|:---|:---|:---|"]
    last = None
    for g in ds.GROUPS:
        for k, (grp, label, unit, source, role, status, _desc) in ds.VARIABLES.items():
            if grp != g:
                continue
            y0, y1, n = ds.coverage(k)
            t = dtype[unit]
            if k == "cpi":
                t = "Index (nominal)"
            if status.startswith("Provisional"):
                label += "^b^"
            gl = g if g != last else ""
            last = g
            rows.append(f"| {gl} | {label} | {unit} | {t} | {source} | {y0}–{y1} ({n}) | {role} |")
    return ("TAB dictionary | Dataset summary: variables, units, data types, sources and coverage\n\n" + "\n".join(rows) +
            "\n\nNOTE: Coverage gives the first and last year with data and, in parentheses, the number of annual observations in the national "
            "panel (1990–2024, 35 years). ^b^ Based on the provisional mitigation coding. The panel also contains auxiliary series used only for "
            "derivations or checks (e.g. nominal prices and agricultural fuel emissions), which are not listed. Regional variables (dairy cows, "
            "livestock units and imputed livestock emissions for five constant-boundary units, 1991–2024) are described in Section 2.7.")


# ------------------------------------------------------------------ numbering
def preprocess(text):
    text = text.replace("TABLEINCLUDE dictionary", dictionary_table())
    figs, tabs = {}, {}
    for m in re.finditer(r"^FIG (\w+) \|", text, re.M):
        figs[m.group(1)] = str(len(figs) + 1)
    n = 0
    for m in re.finditer(r"^TAB (\w+)(?:=(\w+))? \|", text, re.M):
        if m.group(2):
            tabs[m.group(1)] = m.group(2)
        else:
            n += 1
            tabs[m.group(1)] = str(n)

    def ref(m):
        kind, key = m.group(1), m.group(2)
        table = figs if kind == "fig" else tabs
        if key not in table:
            raise KeyError(f"undefined reference {kind}:{key}")
        return ("Figure " if kind == "fig" else "Table ") + table[key]
    text = re.sub(r"\{\{(fig|tab):(\w+)\}\}", ref, text)

    out = []
    for line in text.split("\n"):
        m = re.match(r"^FIG (\w+) \| (.+?) \| (\S+) \| ([\d.]+)$", line)
        if m:
            key, cap, fn, w = m.groups()
            out += ['::: {custom-style="Figure Body"}', f"![]({(FIG_DIR / fn).as_posix()}){{width={w}in}}", ":::", "",
                    '::: {custom-style="Fig Caption"}', f"**Figure {figs[key]}.** {cap}.", ":::"]
            continue
        m = re.match(r"^FIGNOTE: (.+)$", line)
        if m:
            out += ['::: {custom-style="Fig Note"}', f"*Note.* {m.group(1)}", ":::"]
            continue
        m = re.match(r"^TAB (\w+)(?:=\w+)? \| (.+)$", line)
        if m:
            out += ['::: {custom-style="Tbl Caption"}', f"**Table {tabs[m.group(1)]}.** {m.group(2)}.", ":::"]
            continue
        m = re.match(r"^NOTE: (.+)$", line)
        if m:
            out += ['::: {custom-style="Tbl Note"}', f"*Note.* {m.group(1)}", ":::"]
            continue
        if line == "PAGEBREAK":
            out.append(PAGEBREAK)
            continue
        if line == "TOCFIELD":
            out.append(TOCFIELD)
            continue
        m = re.match(r"^# (Abstract) \{\.unnumbered\}$|^## (Highlights) \{\.unnumbered\}$", line)
        if m:
            out += ['::: {custom-style="Front Heading"}', m.group(1) or m.group(2), ":::"]
            continue
        out.append(line)
    print(f"{len(figs)} figures, {len(tabs)} tables")
    return "\n".join(out)


# ------------------------------------------------------------------ Word post-processing
def word_postprocess(docx, pdf):
    import win32com.client as win32
    word = win32.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    doc = word.Documents.Open(str(docx))
    try:
        pts = lambda cm: cm * 72 / 2.54
        TEXT_WIDTH = pts(21.0 - 2 * 2.54)
        for s in doc.Sections:
            ps = s.PageSetup
            ps.PageWidth, ps.PageHeight = pts(21.0), pts(29.7)
            ps.TopMargin = ps.BottomMargin = pts(2.54)
            ps.LeftMargin = ps.RightMargin = pts(2.54)
            ps.DifferentFirstPageHeaderFooter = True
            f = s.Footers(1)  # primary footer
            f.PageNumbers.Add(1, True)  # centred
            f.Range.Font.Name, f.Range.Font.Size = "Times New Roman", 9

        styles = {st.NameLocal: st for st in doc.Styles}
        SERIF = "Times New Roman"

        def style(name, size=None, bold=None, italic=None, align=None, before=None, after=None, spacing=None,
                  keep=None, left=None, first=None, color=0, font=SERIF, caps=None):
            st = styles.get(name)
            if st is None:
                return
            f = st.Font
            f.Name = font
            f.Color = color
            if size is not None: f.Size = size
            if bold is not None: f.Bold = bold
            if italic is not None: f.Italic = italic
            if caps is not None: f.SmallCaps = caps
            p = st.ParagraphFormat
            if align is not None: p.Alignment = align
            if before is not None: p.SpaceBefore = before
            if after is not None: p.SpaceAfter = after
            if spacing is not None:
                p.LineSpacingRule = 5
                p.LineSpacing = 12 * spacing
            if keep is not None: p.KeepWithNext = keep
            if left is not None: p.LeftIndent = left
            if first is not None: p.FirstLineIndent = first

        LEFT, CENTER, JUST = 0, 1, 3
        for n in ("Normal", "Body Text", "First Paragraph", "Compact"):
            style(n, size=11, align=JUST if n != "Compact" else None, after=6, spacing=1.2)
        style("Compact", size=11, after=3, spacing=1.15, align=LEFT)
        style("Abstract Text", size=10.5, align=JUST, after=6, spacing=1.15)
        style("Heading 1", size=14, bold=True, italic=False, before=18, after=8, keep=True, align=LEFT)
        style("Heading 2", size=12, bold=True, italic=False, before=12, after=4, keep=True, align=LEFT)
        style("Heading 3", size=11, bold=True, italic=True, before=8, after=3, keep=True, align=LEFT)
        style("Block Text", size=11, italic=False, left=pts(1.0), before=6, after=8, align=LEFT)
        style("Running Label", size=9, align=CENTER, after=30, color=0x555555, caps=True)
        style("Paper Title", size=18, bold=True, align=CENTER, before=60, after=24, spacing=1.15)
        style("Paper Author", size=12, align=CENTER, after=4)
        style("Paper Affiliation", size=10.5, italic=True, align=CENTER, after=36)
        style("Paper Meta", size=10.5, align=LEFT, after=6, spacing=1.15)
        style("Front Heading", size=13, bold=True, before=0, after=8, keep=True, align=LEFT)
        style("TOC Heading", size=14, bold=True, before=0, after=12, align=LEFT)
        style("Figure Body", align=CENTER, before=10, after=2, keep=True, spacing=1.0)
        style("Fig Caption", size=10, align=JUST, before=2, after=2, spacing=1.1, keep=True)
        style("Fig Note", size=9, align=JUST, after=12, spacing=1.1)
        style("Tbl Caption", size=10, align=LEFT, before=10, after=4, spacing=1.1, keep=True)
        style("Tbl Note", size=9, align=JUST, before=3, after=12, spacing=1.1)
        style("Bibliography", size=10.5, align=LEFT, after=6, spacing=1.15, left=pts(1.27), first=-pts(1.27))
        for i in (1, 2):
            style(f"TOC {i}", size=11, before=2 if i == 2 else 6, after=0, bold=(i == 1), left=pts(0.6 * (i - 1)))

        # Tables: three-line academic style
        for t in doc.Tables:
            t.Borders.Enable = False
            t.Range.Font.Size = 8.5 if t.Columns.Count >= 7 else 9
            t.Range.Font.Name = SERIF
            pf = t.Range.ParagraphFormat
            pf.SpaceBefore, pf.SpaceAfter = 1, 1
            pf.LineSpacingRule = 0
            pf.FirstLineIndent = 0
            t.TopPadding = t.BottomPadding = 0
            t.LeftPadding = t.RightPadding = pts(0.12)
            t.AllowAutoFit = True
            t.Rows(1).Range.Font.Bold = True  # bold before sizing, so header widths are measured correctly
            t.AutoFitBehavior(1)  # size columns to content first...
            cols = [t.Columns(i) for i in range(1, t.Columns.Count + 1)]
            total = sum(c.Width for c in cols)
            if total < TEXT_WIDTH:  # ...then widen narrow tables proportionally to the text width
                t.AllowAutoFit = False
                for c in cols:
                    c.Width = c.Width * TEXT_WIDTH / total
            else:  # wide tables: let Word fit them to the window, respecting minimum content widths
                t.AutoFitBehavior(2)
            t.Rows.AllowBreakAcrossPages = False
            if t.Rows.Count <= 20:  # keep short tables (and their note) on one page
                t.Range.ParagraphFormat.KeepWithNext = True
            else:  # long tables may break, but never straight after the header
                for i in range(1, 4):
                    t.Rows(i).Range.ParagraphFormat.KeepWithNext = True
            for b in (-1, -3):  # top, bottom
                br = t.Borders(b)
                br.LineStyle, br.LineWidth, br.Color = 1, 8, 0
            hdr = t.Rows(1)
            hdr.HeadingFormat = True
            hdr.Range.Font.Bold = True
            hb = hdr.Borders(-3)
            hb.LineStyle, hb.LineWidth, hb.Color = 1, 4, 0
            hdr.Shading.BackgroundPatternColor = 0xF2F2F2

        # Highlight every author-input flag
        rng = doc.Content
        fnd = rng.Find
        fnd.ClearFormatting()
        fnd.Text, fnd.MatchWildcards, fnd.Forward, fnd.Wrap = r"\[AUTHOR INPUT REQUIRED*\]", True, True, 0
        flags = 0
        while fnd.Execute():
            rng.HighlightColorIndex = 7  # yellow
            flags += 1
            rng.Collapse(0)
        print(f"author-input flags highlighted: {flags}")

        doc.Fields.Update()
        for toc in doc.TablesOfContents:
            toc.Update()
        doc.Save()
        doc.ExportAsFixedFormat(str(pdf), 17)
        n_pages = doc.ComputeStatistics(2)
        print(f"pages: {n_pages}")
    finally:
        doc.Close(False)
        word.Quit()


def main():
    MID.parent.mkdir(exist_ok=True)
    MID.write_text(preprocess(SRC.read_text(encoding="utf-8")), encoding="utf-8")
    subprocess.run(["pandoc", str(MID), "-f", "markdown+pipe_tables+superscript+subscript+tex_math_dollars", "-t", "docx",
                    "--columns=250", "-o", str(OUT_DOCX)], check=True)
    word_postprocess(OUT_DOCX, OUT_PDF)
    print("wrote", OUT_DOCX)


if __name__ == "__main__":
    main()
