#!/usr/bin/env python3
"""Fetch webpage items as HTML so the extraction pipeline can process them properly.

For LessWrong/AlignmentForum posts, uses the GraphQL API to get clean content.
For other webpages, downloads the HTML directly.

Usage:
    uv run python scripts/tools/fetch_webpages.py          # process all webpage items
    uv run python scripts/tools/fetch_webpages.py EGICVDI7  # process specific item
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

import yaml


LESSWRONG_DOMAINS = ["lesswrong.com", "alignmentforum.org"]


def extract_lesswrong_post_id(url: str) -> str | None:
    """Extract post ID from a LessWrong/AlignmentForum URL."""
    match = re.search(r"/posts/([a-zA-Z0-9]+)/", url)
    return match.group(1) if match else None


def fetch_lesswrong_post(post_id: str) -> dict:
    """Fetch post content from LessWrong GraphQL API."""
    query = {
        "operationName": "PostContent",
        "variables": {"input": {"selector": {"_id": post_id}}},
        "query": 'query PostContent($input: SinglePostInput!) { post(input: $input) { result { title htmlBody postedAt user { displayName } } } }',
    }
    data = json.dumps(query).encode("utf-8")
    req = urllib.request.Request(
        "https://www.lesswrong.com/graphql",
        data=data,
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
    )
    response = urllib.request.urlopen(req).read().decode("utf-8")
    return json.loads(response)["data"]["post"]["result"]


def make_lesswrong_html(post: dict) -> str:
    """Wrap LessWrong post content in HTML with JSON-LD for the extraction pipeline."""
    json_ld = {
        "headline": post["title"],
        "author": [{"name": post["user"]["displayName"]}],
        "datePublished": post["postedAt"],
        "text": post["htmlBody"],
    }
    return (
        "<html><head>"
        f'<script type="application/ld+json">{json.dumps(json_ld)}</script>'
        f"</head><body>{post['htmlBody']}</body></html>"
    )


def fetch_generic_html(url: str) -> str:
    """Download HTML from a URL."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req).read().decode("utf-8")


def is_lesswrong_url(url: str) -> bool:
    return any(domain in url for domain in LESSWRONG_DOMAINS)


def process_item(item_dir: Path) -> bool:
    """Process a single bib item: fetch HTML, remove PDF, clear old extraction."""
    citation_key = item_dir.name
    metadata_path = item_dir / ".metadata.txt"
    if not metadata_path.exists():
        return False

    metadata = metadata_path.read_text()
    url = None
    item_type = None
    for line in metadata.split("\n"):
        if line.startswith("URL: "):
            url = line[5:].strip()
        if line.startswith("Type: "):
            item_type = line[6:].strip()

    if not url or item_type != "webpage":
        return False

    html_dest = item_dir / f"{citation_key}.html"
    if html_dest.exists():
        print(f"  HTML already exists: {citation_key}, skipping")
        return False

    if is_lesswrong_url(url):
        post_id = extract_lesswrong_post_id(url)
        if not post_id:
            print(f"  Could not extract post ID from: {url}")
            return False
        print(f"  Fetching LessWrong post: {url}")
        post = fetch_lesswrong_post(post_id)
        html = make_lesswrong_html(post)
    else:
        print(f"  Fetching webpage: {url}")
        html = fetch_generic_html(url)

    html_dest.write_text(html, encoding="utf-8")
    print(f"  Saved: {citation_key}.html")

    # Remove PDF so extraction pipeline uses HTML
    for pdf in item_dir.glob("*.pdf"):
        pdf.unlink()
        print(f"  Removed: {pdf.name}")

    # Remove existing fulltext so extraction re-runs
    fulltext = item_dir / f"{citation_key}_fulltext.md"
    if fulltext.exists():
        fulltext.unlink()
        print(f"  Removed old fulltext")

    # Remove existing chapters so they get recreated
    chapters_dir = item_dir / "chapters"
    if chapters_dir.exists():
        import shutil
        shutil.rmtree(chapters_dir)
        print(f"  Removed old chapters")

    return True


def main():
    config_path = Path(__file__).parent.parent / "config.yaml"
    with open(config_path) as f:
        config = yaml.safe_load(f)

    bib_dir = Path(config["output_dir"])
    specific_key = sys.argv[1] if len(sys.argv) > 1 else None

    processed = 0
    for item_dir in sorted(bib_dir.iterdir()):
        if not item_dir.is_dir() or item_dir.name.startswith("."):
            continue
        if specific_key and item_dir.name != specific_key:
            continue
        if process_item(item_dir):
            processed += 1

    print(f"\nProcessed {processed} items")


if __name__ == "__main__":
    main()
