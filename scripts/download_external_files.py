#!/usr/bin/env python3
"""Download external files referenced in original HTML files into the wiki clone."""

import os
import re
import sys
from pathlib import Path
from urllib.parse import urljoin
import time

try:
    import requests
except ImportError:
    print("Installing requests...")
    os.system(f"{sys.executable} -m pip install requests")
    import requests

BASE_URL = "https://musictheory.pugetsound.edu/mt21c/"
HTML_DIR = Path("original")
OUTPUT_DIR = Path("../teoria-musical.wiki/external")


def find_external_references(html_dir):
    """Find all external file references in HTML files."""
    references = set()

    for html_file in html_dir.glob("*.html"):
        content = html_file.read_text(errors="replace")
        matches = re.findall(r'external/[^\s"\'<>)]+', content)
        references.update(matches)

    return sorted(references)


def download_file(url, output_path):
    """Download a file from URL to output path."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(response.content)
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False


def main():
    os.chdir(Path(__file__).parent.parent)

    print("Finding external file references in HTML originals...")
    references = find_external_references(HTML_DIR)
    print(f"Found {len(references)} unique external files")

    print(f"\nDownloading to {OUTPUT_DIR}/")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    success_count = 0
    skip_count = 0
    fail_count = 0

    for i, ref in enumerate(references):
        # ref is like "external/images/unit1/foo.svg"
        # strip "external/" prefix since OUTPUT_DIR already ends with /external
        rel_path = ref[len("external/"):] if ref.startswith("external/") else ref
        output_path = OUTPUT_DIR / rel_path

        if output_path.exists():
            skip_count += 1
            continue

        url = urljoin(BASE_URL, ref)
        print(f"[{i+1}/{len(references)}] {ref}...", end=" ", flush=True)

        if download_file(url, output_path):
            print("ok")
            success_count += 1
        else:
            print("FAILED")
            fail_count += 1

        time.sleep(0.05)

    print(f"\nComplete: {success_count} downloaded, {skip_count} cached, {fail_count} failed")


if __name__ == "__main__":
    main()
