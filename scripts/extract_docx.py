#!/usr/bin/env python3
"""Extract body text and footnotes from a .docx manuscript; optionally split on headings.

Standard library only. Reads the .docx as a zip archive; makes no network calls.

Usage:
    python3 scripts/extract_docx.py article.docx                 # Markdown-like text to stdout
    python3 scripts/extract_docx.py article.docx -o article.md   # write to a file
    python3 scripts/extract_docx.py article.docx --chunk 8000    # write article_chunk_N.md files
                                                                 # split at headings, about N words each

Footnote references appear inline as [^n]; footnote texts follow the body as [^n]: text.
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _run_text(el) -> str:
    parts = []
    for node in el.iter():
        if node.tag == W + "t" and node.text:
            parts.append(node.text)
        elif node.tag == W + "tab":
            parts.append("\t")
        elif node.tag in (W + "br", W + "cr"):
            parts.append("\n")
        elif node.tag == W + "footnoteReference":
            parts.append(f"[^{node.get(W + 'id')}]")
        elif node.tag == W + "delText":
            continue  # tracked deletions are not part of the current text
    return "".join(parts)


def _heading_level(p) -> int | None:
    ppr = p.find(W + "pPr")
    if ppr is None:
        return None
    style = ppr.find(W + "pStyle")
    if style is not None:
        val = style.get(W + "val", "")
        m = re.match(r"(?i)heading\s*(\d)|^(\d)$|^Title$", val)
        if m:
            return int(m.group(1) or m.group(2) or 1)
    outline = ppr.find(W + "outlineLvl")
    if outline is not None:
        return int(outline.get(W + "val", "0")) + 1
    return None


def extract(path: Path) -> tuple[list[tuple[int | None, str]], dict[str, str]]:
    """Return ([(heading_level_or_None, paragraph_text)], {footnote_id: text})."""
    with zipfile.ZipFile(path) as z:
        doc = ET.fromstring(z.read("word/document.xml"))
        notes = {}
        if "word/footnotes.xml" in z.namelist():
            fn_root = ET.fromstring(z.read("word/footnotes.xml"))
            for fn in fn_root.findall(W + "footnote"):
                fid = fn.get(W + "id")
                if fn.get(W + "type") in ("separator", "continuationSeparator", "continuationNotice"):
                    continue
                text = " ".join(_run_text(p).strip() for p in fn.iter(W + "p")).strip()
                notes[fid] = text
    paras = []
    body = doc.find(W + "body")
    for p in body.iter(W + "p"):
        text = _run_text(p).strip()
        if text:
            paras.append((_heading_level(p), text))
    return paras, notes


def render(paras, notes, note_ids=None) -> str:
    out = []
    for level, text in paras:
        out.append(("#" * level + " " + text) if level else text)
    used = note_ids if note_ids is not None else list(notes)
    if used:
        out.append("\n---\n")
        for fid in used:
            if fid in notes:
                out.append(f"[^{fid}]: {notes[fid]}")
    return "\n\n".join(out) + "\n"


def chunk(paras, target_words: int):
    chunks, current, count = [], [], 0
    for level, text in paras:
        words = len(text.split())
        if level and current and count >= target_words * 0.5 and count + words > target_words:
            chunks.append(current)
            current, count = [], 0
        current.append((level, text))
        count += words
    if current:
        chunks.append(current)
    return chunks


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx", type=Path)
    ap.add_argument("-o", "--output", type=Path)
    ap.add_argument("--chunk", type=int, metavar="WORDS", help="split at headings into chunks of about WORDS words")
    args = ap.parse_args()
    try:
        paras, notes = extract(args.docx)
    except (zipfile.BadZipFile, KeyError) as exc:
        print(f"ERROR: cannot read {args.docx} as .docx: {exc}", file=sys.stderr)
        return 2
    if args.chunk:
        parts = chunk(paras, args.chunk)
        for i, part in enumerate(parts, 1):
            ids = re.findall(r"\[\^(\d+)\]", "\n".join(t for _, t in part))
            out = args.docx.with_name(f"{args.docx.stem}_chunk_{i}.md")
            out.write_text(render(part, notes, ids), encoding="utf-8")
            heads = [t for lvl, t in part if lvl][:3]
            words = sum(len(t.split()) for _, t in part)
            print(f"{out.name}: {words} words; headings: {'; '.join(heads) or '(none)'}")
        print("Chunks split at headings. Check the map above before relying on it.")
        return 0
    text = render(paras, notes)
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
