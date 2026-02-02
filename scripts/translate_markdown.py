#!/usr/bin/env python3
"""
Translate Markdown files to Portuguese.
This script prepares files for translation, preserving formatting.
"""

import re
from pathlib import Path
import json


INPUT_DIR = Path(__file__).parent.parent / "markdown"
OUTPUT_DIR = Path(__file__).parent.parent / "pt-br"
TEMP_DIR = Path(__file__).parent.parent / "temp"


def extract_translatable_content(markdown_text):
    """
    Extract translatable text from markdown, preserving:
    - LaTeX formulas
    - Image paths
    - Links
    - Code blocks
    """

    # Store non-translatable content
    preserved = {}
    counter = [0]

    def preserve(match):
        """Replace content with placeholder."""
        key = f"__PRESERVE_{counter[0]}__"
        preserved[key] = match.group(0)
        counter[0] += 1
        return key

    # Preserve LaTeX math (inline and display)
    text = re.sub(r'\\\(.*?\\\)', preserve, markdown_text)
    text = re.sub(r'\\\[.*?\\\]', preserve, markdown_text, flags=re.DOTALL)

    # Preserve image paths
    text = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', preserve, text)

    # Preserve link URLs but keep link text for translation
    def preserve_link_url(match):
        link_text = match.group(1)
        link_url = match.group(2)
        key = f"__LINKURL_{counter[0]}__"
        preserved[key] = link_url
        counter[0] += 1
        return f'[{link_text}]({key})'

    text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', preserve_link_url, text)

    # Preserve code blocks
    text = re.sub(r'```.*?```', preserve, text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', preserve, text)

    return text, preserved


def restore_preserved_content(translated_text, preserved):
    """Restore non-translatable content."""
    for key, value in preserved.items():
        translated_text = translated_text.replace(key, value)
    return translated_text


def save_for_translation(md_path, output_json):
    """Save markdown in a format ready for translation."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract translatable content
    translatable, preserved = extract_translatable_content(content)

    data = {
        'source_file': md_path.name,
        'original': content,
        'translatable': translatable,
        'preserved': preserved,
        'translated': ''  # To be filled
    }

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return data


def apply_translation(json_path, output_md):
    """Apply translation from JSON to create translated Markdown."""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not data.get('translated'):
        print(f"Warning: No translation found in {json_path}")
        return False

    # Restore preserved content
    translated = restore_preserved_content(data['translated'], data['preserved'])

    # Write translated markdown
    output_md.parent.mkdir(parents=True, exist_ok=True)
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(translated)

    return True


if __name__ == "__main__":
    import sys

    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if len(sys.argv) > 1 and sys.argv[1] == "prepare":
        # Prepare all files for translation
        md_files = sorted(INPUT_DIR.glob('*.md'))
        print(f"Preparing {len(md_files)} files for translation...")

        for md_file in md_files:
            json_file = TEMP_DIR / f"{md_file.stem}.json"
            save_for_translation(md_file, json_file)
            print(f"  ✓ {md_file.name}")

        print(f"\nFiles prepared in {TEMP_DIR}")

    elif len(sys.argv) > 1 and sys.argv[1] == "apply":
        # Apply translations from JSON files
        json_files = sorted(TEMP_DIR.glob('*.json'))
        print(f"Applying translations from {len(json_files)} files...")

        for json_file in json_files:
            md_file = OUTPUT_DIR / f"{json_file.stem}.md"
            if apply_translation(json_file, md_file):
                print(f"  ✓ {json_file.stem}.md")

        print(f"\nTranslations saved to {OUTPUT_DIR}")

    else:
        print("Usage:")
        print("  python translate_markdown.py prepare  - Prepare files for translation")
        print("  python translate_markdown.py apply    - Apply translations to create PT-BR files")
