#!/usr/bin/env python3
"""Add a webpage to Zotero with an HTML snapshot attachment.
Uses Playwright to render JS-heavy pages (like LessWrong) so the snapshot
contains the fully rendered DOM, matching what Zotero's browser connector saves."""

import sys
import os
import json
import argparse
import urllib.request
import urllib.parse
import base64
import re
from datetime import datetime, timezone
from pathlib import Path
from html.parser import HTMLParser
from playwright.sync_api import sync_playwright

API_KEY = os.environ.get("ZOTERO_API_KEY")
if not API_KEY:
    print("Error: ZOTERO_API_KEY not set")
    sys.exit(1)

USER_ID = None


def get_user_id():
    global USER_ID
    if USER_ID:
        return USER_ID
    req = urllib.request.Request(
        f"https://api.zotero.org/keys/{API_KEY}",
        headers={"Zotero-API-Key": API_KEY}
    )
    USER_ID = json.loads(urllib.request.urlopen(req).read())["userID"]
    return USER_ID


def api_request(endpoint, method="GET", data=None, headers=None):
    user_id = get_user_id()
    url = f"https://api.zotero.org/users/{user_id}/{endpoint}"
    hdrs = {"Zotero-API-Key": API_KEY, "Content-Type": "application/json"}
    if headers:
        hdrs.update(headers)
    if data is not None:
        req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=hdrs, method=method)
    else:
        req = urllib.request.Request(url, headers=hdrs, method=method)
    resp = urllib.request.urlopen(req)
    body = resp.read()
    return json.loads(body) if body else None


def get_collection_key(name_or_key):
    collections = api_request("collections")
    for c in collections:
        if c["data"]["key"] == name_or_key or c["data"]["name"].lower() == name_or_key.lower():
            return c["data"]["key"]
    return None


class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.og = {}
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._in_title = True
            return
        if tag != "meta":
            return
        d = dict(attrs)
        prop = d.get("property", d.get("name", ""))
        content = d.get("content", "")
        if prop.startswith("og:") and content:
            self.og[prop] = content
        if prop == "description" and content:
            self.og.setdefault("description", content)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def url_to_filename(url):
    path = urllib.request.urlparse(url).path.rstrip("/")
    slug = path.split("/")[-1] if path else "snapshot"
    slug = re.sub(r"[^a-zA-Z0-9_-]", "_", slug)
    if not slug:
        slug = "snapshot"
    return slug + ".html"


def parse_authors(authors_str):
    creators = []
    for author in authors_str.split(","):
        author = author.strip()
        if not author:
            continue
        parts = author.rsplit(" ", 1)
        if len(parts) == 2:
            creators.append({"creatorType": "author", "firstName": parts[0], "lastName": parts[1]})
        else:
            creators.append({"creatorType": "author", "name": author})
    return creators


SCROLL_JS = """async () => {
  for (let y = 0; y < document.body.scrollHeight; y += 800) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 150)); }
  window.scrollTo(0, 0);
}"""

LIST_JS = """() => ({
  css: [...document.querySelectorAll('link[rel~="stylesheet"]')].map(l => l.href),
  img: [...document.querySelectorAll('img')].map(i => i.currentSrc || i.src).filter(u => u.startsWith('http')),
})"""

COOKIE_JS = """() => document.querySelectorAll('body *').forEach(e => {
  if (getComputedStyle(e).position === 'fixed' && /cookie/i.test(e.innerText || '')) e.remove();
})"""

APPLY_JS = """({css, img, base}) => {
  document.querySelectorAll('link[rel~="stylesheet"]').forEach(l => {
    if (css[l.href] == null) return;
    const s = document.createElement('style'); s.textContent = css[l.href]; l.replaceWith(s);
  });
  document.querySelectorAll('picture source').forEach(s => s.remove());
  document.querySelectorAll('img').forEach(i => {
    const u = i.currentSrc || i.src;
    if (img[u]) i.src = img[u];
    i.removeAttribute('srcset'); i.removeAttribute('loading');
  });
  document.querySelectorAll('script, noscript, link[rel="preload"], link[rel="modulepreload"]').forEach(e => e.remove());
  const b = document.createElement('base'); b.href = base; document.head.prepend(b);
}"""


def download_page(url):
    """Render the page headlessly and return self-contained HTML (CSS and images inlined, scripts removed)."""
    print(f"  Rendering page with headless browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.goto(url, wait_until="load", timeout=90000)
        page.wait_for_timeout(3000)
        page.evaluate(SCROLL_JS)
        page.wait_for_timeout(2000)
        refs = page.evaluate(LIST_JS)
        css, img = {}, {}
        for href in set(refs["css"]):
            r = page.request.get(href)
            if r.ok:
                css[href] = re.sub(r"url\(\s*['\"]?(?!data:|https?:|#)([^'\")]+)['\"]?\s*\)",
                                   lambda m: f"url({urllib.parse.urljoin(href, m.group(1))})", r.text())
        for src in set(refs["img"]):
            r = page.request.get(src)
            if r.ok:
                ctype = r.headers.get("content-type", "image/png").split(";")[0]
                img[src] = f"data:{ctype};base64,{base64.b64encode(r.body()).decode()}"
        page.evaluate(COOKIE_JS)
        for frame in page.query_selector_all("iframe"):
            box = frame.bounding_box()
            if box and box["height"] > 50 and frame.is_visible():
                shot = base64.b64encode(frame.screenshot()).decode()
                frame.evaluate("(e, src) => { const i = document.createElement('img'); i.src = src; i.style.maxWidth = '100%'; e.replaceWith(i); }",
                               f"data:image/png;base64,{shot}")
        page.evaluate(APPLY_JS, {"css": css, "img": img, "base": url})
        html = "<!DOCTYPE html>\n" + page.content()
        browser.close()
    return html.encode("utf-8"), "utf-8"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a webpage to Zotero with HTML snapshot")
    parser.add_argument("url", help="URL of the webpage")
    parser.add_argument("--title", help="Page title (auto-detected if omitted)")
    parser.add_argument("--authors", help="Comma-separated author names")
    parser.add_argument("--date", help="Publication date")
    parser.add_argument("--abstract", help="Abstract / description")
    parser.add_argument("--site-title", help="Website title (e.g. 'LessWrong')")
    parser.add_argument("--collection", help="Zotero collection name or key")
    parser.add_argument("--resnapshot", help="Only re-render the snapshot into this existing file")
    args = parser.parse_args()

    if args.resnapshot:
        Path(args.resnapshot).write_bytes(download_page(args.url)[0])
        print(f"Snapshot saved: {args.resnapshot}")
        sys.exit(0)

    collection_key = None
    if args.collection:
        collection_key = get_collection_key(args.collection)
        if not collection_key:
            print(f"Error: Collection '{args.collection}' not found")
            sys.exit(1)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    print(f"Downloading {args.url}...")
    html_bytes, charset = download_page(args.url)
    html_text = html_bytes.decode(charset, errors="replace")

    mp = MetaParser()
    mp.feed(html_text)

    title = args.title or mp.og.get("og:title", mp.title).strip()
    abstract = args.abstract or mp.og.get("og:description", mp.og.get("description", ""))
    site_title = args.site_title or mp.og.get("og:site_name", "")

    if not title:
        print("Error: Could not detect page title. Provide --title.")
        sys.exit(1)

    creators = parse_authors(args.authors) if args.authors else []
    date = args.date or ""

    metadata = {
        "itemType": "webpage",
        "title": title,
        "creators": creators,
        "abstractNote": abstract,
        "websiteTitle": site_title,
        "date": date,
        "url": args.url,
        "accessDate": now,
    }
    if collection_key:
        metadata["collections"] = [collection_key]

    print(f"Title: {title}")
    if creators:
        print(f"Authors: {', '.join(c.get('lastName', c.get('name')) for c in creators)}")
    print(f"Site: {site_title}")

    result = api_request("items", method="POST", data=[metadata])
    if not result.get("successful"):
        print(f"Error creating item: {result}")
        sys.exit(1)

    parent_key = list(result["successful"].values())[0]["key"]
    print(f"Created item: {parent_key}")

    filename = url_to_filename(args.url)
    attachment = {
        "itemType": "attachment",
        "parentItem": parent_key,
        "linkMode": "imported_url",
        "title": "Snapshot",
        "accessDate": now,
        "url": args.url,
        "contentType": "text/html",
        "charset": charset,
        "filename": filename,
    }

    result = api_request("items", method="POST", data=[attachment])
    if not result.get("successful"):
        print(f"Error creating attachment: {result}")
        sys.exit(1)

    attach_key = list(result["successful"].values())[0]["key"]
    storage = Path.home() / "Zotero" / "storage" / attach_key
    storage.mkdir(parents=True, exist_ok=True)
    (storage / filename).write_bytes(html_bytes)
    print(f"Snapshot saved: {attach_key}/{filename}")

    print("Done!")
