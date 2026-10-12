#!/usr/bin/env python3
"""
Convierte posts de Jekyll (_posts/*.md) a Astro (src/content/blog/*.md)

Uso:
    python3 migrate_posts.py <ruta-a-_posts> [limite]

Ejemplo (solo 2 posts):
    python3 migrate_posts.py ../MAInformatico.github.io/_posts 2
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path

TARGET_DIR = Path("./src/content/blog")


def parse_frontmatter(content: str):
    """Extrae frontmatter YAML simple y el cuerpo del Markdown."""
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", content, re.DOTALL)
    if not match:
        return {}, content

    yaml_block, body = match.groups()
    data = {}

    for line in yaml_block.splitlines():
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if not m:
            continue
        key, raw_value = m.groups()
        value = raw_value.strip()

        # Quitar comillas
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]

        # Array simple [a, b, c]
        if value.startswith("[") and value.endswith("]"):
            items = value[1:-1].split(",")
            value = [i.strip().strip("\"'") for i in items if i.strip()]

        data[key] = value

    return data, body


def normalize_date(raw) -> str:
    if not raw:
        return datetime.now().strftime("%Y-%m-%d")
    m = re.search(r"(\d{4})-(\d{1,2})-(\d{1,2})", str(raw))
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return datetime.now().strftime("%Y-%m-%d")

def yaml_str(s) -> str:
    """Escapa un string para YAML con comillas simples."""
    if s is None:
        return "''"
    return "'" + str(s).replace("'", "''") + "'"


def migrate(source_dir: Path, limit: int):
    if not source_dir.exists():
        print(f"❌ No existe el directorio: {source_dir}")
        sys.exit(1)

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    files = sorted(f for f in source_dir.iterdir() if f.suffix == ".md")
    to_process = files[:limit]

    print(f"📂 Encontrados {len(files)} posts, procesando {len(to_process)}\n")

    ok = skipped = 0

    for src in to_process:
        content = src.read_text(encoding="utf-8")
        data, body = parse_frontmatter(content)

        if not data.get("title"):
            print(f"⚠️  Saltando {src.name} (sin título)")
            skipped += 1
            continue

        # Nombre destino: quitar prefijo YYYY-MM-DD-
        clean_name = re.sub(r"^\d{4}-\d{1,2}-\d{1,2}-", "", src.name)
        pub_date = normalize_date(data.get("date"))

        lines = [
            "---",
            f"title: {yaml_str(data['title'])}",
            f"description: {yaml_str(data.get('description') or data.get('excerpt') or '')}",
            f"pubDate: {yaml_str(pub_date)}",
        ]

        if data.get("categories"):
            cats = data["categories"]
            cats = cats if isinstance(cats, list) else [cats]
            lines.append("categories: [" + ", ".join(yaml_str(c) for c in cats) + "]")
        elif data.get("tags"):
            tags = data["tags"]
            tags = tags if isinstance(tags, list) else [tags]
            lines.append("tags: [" + ", ".join(yaml_str(t) for t in tags) + "]")

        lines += ["---", "", body.lstrip()]

        out_path = TARGET_DIR / clean_name
        out_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"✅ {src.name}  →  {clean_name}")
        ok += 1

    print(f"\n🎉 Completado: {ok} migrados, {skipped} saltados")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 migrate_posts.py <ruta-a-_posts> [limite]")
        sys.exit(1)

    source = Path(sys.argv[1])
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10**9
    migrate(source, limit)
