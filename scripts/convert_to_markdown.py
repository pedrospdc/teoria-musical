#!/usr/bin/env python3
"""
Convert HTML files to clean Markdown, extracting only the main content.
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup
import html2text


INPUT_DIR = Path(__file__).parent.parent / "original"
OUTPUT_DIR = Path(__file__).parent.parent / "markdown"


def extract_main_content(soup):
    """Extract only the main content from the HTML."""
    main_content = soup.find('div', id='ptx-content')
    if not main_content:
        main_content = soup.find('main')
    if not main_content:
        main_content = soup.find('body')
    return main_content


def clean_soup(soup_element):
    """Remove unwanted elements from the soup."""
    if not soup_element:
        return soup_element

    for tag in soup_element.find_all(['script', 'style', 'nav', 'header', 'footer']):
        tag.decompose()

    remove_classes = [
        'ptx-navbar', 'ptx-toc', 'ptx-sidebar', 'searchbox',
        'autopermalink', 'ptx-content-footer', 'treebuttons',
        'search-results-controls', 'nav-other-controls'
    ]

    for class_name in remove_classes:
        for element in soup_element.find_all(class_=class_name):
            element.decompose()

    for div_id in ['ptx-sidebar', 'ptx-navbar', 'latex-macros', 'searchresultsplaceholder']:
        element = soup_element.find(id=div_id)
        if element:
            element.decompose()

    return soup_element


def extract_title(soup):
    """Extract the page title."""
    title_tag = soup.find('title')
    if title_tag:
        return title_tag.get_text().strip()
    h1 = soup.find('h1')
    if h1:
        return h1.get_text().strip()
    return "Untitled"


def convert_html_to_markdown(html_path, output_path):
    """Convert HTML file to Markdown."""
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'lxml')
    title = extract_title(soup)
    main_content = extract_main_content(soup)
    main_content = clean_soup(main_content)

    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0
    h.skip_internal_links = True
    h.inline_links = True
    h.ignore_anchors = True

    if main_content:
        markdown = h.handle(str(main_content))
    else:
        markdown = "No content found."

    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    markdown = re.sub(r'\[.*?\]\(#[^\)]*\)', '', markdown)
    markdown = re.sub(r'🔗', '', markdown)

    if not markdown.startswith('#'):
        markdown = f"# {title}\n\n{markdown}"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown.strip() + '\n')

    return True


def extract_table_of_contents(html_path):
    """Extract the table of contents structure."""
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')

    toc = []
    toc_nav = soup.find('nav', id='ptx-toc')
    if not toc_nav:
        return toc

    for chapter_li in toc_nav.find_all('li', class_='toc-chapter'):
        title_box = chapter_li.find('div', class_='toc-title-box')
        if not title_box:
            continue

        link = title_box.find('a')
        if not link:
            continue

        codenumber = link.find('span', class_='codenumber')
        title_span = link.find('span', class_='title')

        if codenumber and title_span:
            toc.append({
                'number': codenumber.get_text().strip(),
                'title': title_span.get_text().strip(),
                'file': link.get('href', ''),
                'type': 'chapter'
            })

    return toc


def create_index(toc, output_path):
    """Create a comprehensive Markdown index."""
    lines = [
        "# Teoria Musical para a Sala de Aula do Século XXI",
        "",
        "**Music Theory for the 21st-Century Classroom**",
        "",
        "Tradução para português brasileiro do livro de Robert Hutchinson.",
        "",
        "---",
        "",
        "## Índice",
        ""
    ]

    for item in toc:
        number = item['number']
        title = item['title']
        md_file = item['file'].replace('.html', '.md')
        if number.isdigit() and int(number) > 0:
            lines.append(f"{number}. [{title}]({md_file})")

    lines.extend([
        "",
        "---",
        "",
        "## Sobre",
        "",
        "Este material foi convertido para Markdown para facilitar a tradução.",
        "Todo o conteúdo original pertence ao autor Robert Hutchinson.",
        ""
    ])

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"✓ Created index: {output_path}")


def convert_all():
    """Convert all HTML files to Markdown."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    html_files = sorted(INPUT_DIR.glob('*.html'))
    total = len(html_files)

    print(f"Converting {total} HTML files to Markdown...")
    print("=" * 60)

    success_count = 0
    error_count = 0

    for i, html_path in enumerate(html_files, 1):
        md_path = OUTPUT_DIR / html_path.name.replace('.html', '.md')

        try:
            convert_html_to_markdown(html_path, md_path)
            print(f"[{i:3d}/{total}] ✓ {html_path.name}")
            success_count += 1
        except Exception as e:
            print(f"[{i:3d}/{total}] ✗ {html_path.name} - Error: {e}")
            error_count += 1

    print("=" * 60)
    print(f"Conversion complete!")
    print(f"  Success: {success_count}")
    print(f"  Errors:  {error_count}")
    print(f"  Output:  {OUTPUT_DIR}")

    print("\nCreating index...")
    main_html = INPUT_DIR / "MusicTheory.html"
    if main_html.exists():
        toc = extract_table_of_contents(main_html)
        create_index(toc, OUTPUT_DIR / "README.md")

    return success_count, error_count


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "all":
            convert_all()
        else:
            filename = sys.argv[1]
            html_path = INPUT_DIR / filename
            md_path = OUTPUT_DIR / filename.replace('.html', '.md')

            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

            print(f"Converting {filename}...")
            convert_html_to_markdown(html_path, md_path)
            print(f"✓ Saved to {md_path}")
    else:
        print("Usage:")
        print("  python convert_to_markdown.py <filename.html>  - Convert single file")
        print("  python convert_to_markdown.py all              - Convert all files")
