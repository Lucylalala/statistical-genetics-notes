from pathlib import Path
import re

H1 = re.compile(r"^\s*#\s+(.+)$")

def title_of(md: Path) -> str:
    try:
        with md.open(encoding="utf-8") as f:
            for _ in range(20):
                line = f.readline()
                if not line:
                    break
                m = H1.match(line)
                if m:
                    return m.group(1).strip()
    except:
        pass
    return md.stem.replace("_", " ").replace("-", " ")

root = Path("docs")

print("nav:")
print("  - Home: index.md")

for section in sorted([d for d in root.iterdir() if d.is_dir()]):
    sec_title = section.name.replace("_", " ")
    print(f"  - {sec_title}:")
    for md in sorted(section.rglob("*.md")):
        if md.name == "index.md":
            continue
        t = title_of(md)
        rel = md.relative_to(root).as_posix()
        print(f"      - {t}: {rel}")
