# gen_nav.py
from __future__ import annotations
from pathlib import Path
import re
from typing import Dict, List, Union, Tuple

NavNode = Union[str, Dict[str, "NavNode"], List["NavNode"]]

H1_RE = re.compile(r"^\s*#\s+(.+?)\s*$")

def md_title(md_path: Path) -> str:
    """Use first H1 as title; fallback to filename."""
    try:
        with md_path.open("r", encoding="utf-8") as f:
            for _ in range(40):  # scan first 40 lines
                line = f.readline()
                if not line:
                    break
                m = H1_RE.match(line)
                if m:
                    return m.group(1).strip()
    except UnicodeDecodeError:
        # if file is not utf-8, fallback
        pass

    # fallback: filename -> nice title
    name = md_path.stem
    name = name.replace("_", " ").replace("-", " ")
    # keep common acronyms
    name = re.sub(r"\bGwas\b", "GWAS", name, flags=re.I)
    name = re.sub(r"\bK matrix\b", "K matrix", name, flags=re.I)
    # title case but don't mess all-caps words
    words = []
    for w in name.split():
        words.append(w if w.isupper() else w[:1].upper() + w[1:])
    return " ".join(words)

def sort_key(path: Path) -> Tuple[int, str]:
    """
    Sort with numeric prefix first if exists: '01_Core' -> (1,'_Core'), else (999,'name').
    """
    m = re.match(r"^(\d+)[_-](.+)$", path.name)
    if m:
        return (int(m.group(1)), m.group(2).lower())
    return (999, path.name.lower())

def quote_yaml(s: str) -> str:
    """Quote YAML strings safely (handles spaces, parentheses, colon, etc.)."""
    if re.search(r"[:\[\]\{\},#&*!|>'\"%@`]", s) or s.strip() != s or " " in s:
        return '"' + s.replace('"', '\\"') + '"'
    return s

def emit_yaml(nav: List[dict], indent: int = 0) -> str:
    """
    nav is list of {title: value} where value is str (path) or list (children).
    """
    lines: List[str] = []
    pad = "  " * indent
    for item in nav:
        # item has single key
        (k, v), = item.items()
        kq = quote_yaml(k)
        if isinstance(v, str):
            lines.append(f"{pad}- {kq}: {quote_yaml(v)}")
        elif isinstance(v, list):
            lines.append(f"{pad}- {kq}:")
            lines.append(emit_yaml(v, indent + 1))
        else:
            raise TypeError(v)
    return "\n".join(lines)

def build_nav(root: Path, include_home: bool = True) -> List[dict]:
    """
    Build nested nav from directory structure.
    Only includes .md files; ignores hidden dirs and mkdocs.yml etc.
    """
    root = root.resolve()

    def walk_dir(d: Path) -> List[dict]:
        items: List[dict] = []

        # md files in this dir (exclude index.md unless it's root)
        md_files = sorted([p for p in d.iterdir() if p.is_file() and p.suffix.lower() == ".md"], key=lambda p: p.name.lower())
        for f in md_files:
            if f.name.lower() == "index.md" and d != root:
                continue
            title = md_title(f)
            rel = f.relative_to(root).as_posix()
            items.append({title: rel})

        # subdirs
        subdirs = sorted([p for p in d.iterdir() if p.is_dir() and not p.name.startswith(".")], key=sort_key)
        for sd in subdirs:
            children = walk_dir(sd)
            if children:
                # folder title: strip numeric prefix like 01_Core -> Core
                folder_name = sd.name
                folder_name = re.sub(r"^\d+[_-]", "", folder_name)
                folder_title = folder_name.replace("_", " ").replace("-", " ")
                items.append({folder_title: children})

        return items

    nav = []
    if include_home:
        # if root/index.md exists, make it Home
        if (root / "index.md").exists():
            nav.append({"Home": "index.md"})
    nav.extend(walk_dir(root))

    # Remove duplicate Home if root index.md also added by walk_dir
    nav = [x for x in nav if list(x.keys())[0] != md_title(root / "index.md")] if include_home and (root / "index.md").exists() else nav
    return nav

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="docs", help="content root directory (usually docs)")
    ap.add_argument("--out", default="nav.generated.yml", help="output YAML file")
    args = ap.parse_args()

    root = Path(args.root)
    if not root.exists():
        raise SystemEx
