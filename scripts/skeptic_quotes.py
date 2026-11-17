import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

FIG = Path("content/05_counterarguments/figures/tweets").resolve()
ORD, BALL = ("Toby Ord", "@tobyordoxford", "avatar_ord.jpg"), ("Dean W. Ball", "Hyperdimensional", "avatar_ball.png")
COLUMNS = [
    [
        (ORD, "11 Nov 2026", "I see their arguments as being: without pacing, there is a substantial (~50%) chance of intelligence explosion next year. […]\n\nPersonally, I'd put a lower probability on this, but still non-trivial (e.g. 1 in 8). Which also suggests slowing down is very important, but I'm actively predicting the explosion is unlikely to happen next year."),
    ],
    [
        (BALL, "10 Nov 2026", "The METR study of Anthropic’s internal R&D acceleration is undeniably good evidence that weak recursion is taking place. But is it evidence that strong recursion is underway? […]\n\nI see almost no evidence, either from the METR study or from public disclosures of research-acceleration metrics by OpenAI or Anthropic, that strong recursion is taking place."),
    ],
]

CSS = """
body{margin:0;background:#fff}
#wrap{padding:6px;width:1875px;display:flex;gap:22px;align-items:flex-start;font-family:Helvetica,Arial,sans-serif}
.col{flex:1;display:flex;flex-direction:column;gap:22px}
.card{border:1.5px solid #cfd9de;border-radius:24px;padding:18px 24px 22px}
.head{display:flex;gap:16px;align-items:center;margin-bottom:16px}
.head img{width:62px;height:62px;border-radius:50%}
.name{font-weight:700;font-size:22px;color:#0f1419}
.meta{font-size:22px;color:#536471;margin-top:3px}
.text{font-size:24px;line-height:1.38;color:#0f1419;white-space:pre-wrap}
"""
card = lambda who, day, text: f'<div class="card"><div class="head"><img src="{who[2]}"><div><div class="name">{who[0]}</div><div class="meta">{who[1]} · {day}</div></div></div><div class="text">{text.replace("&", "&amp;")}</div></div>'
html = f"<style>{CSS}</style><div id=wrap>" + "".join(f'<div class="col">{"".join(card(*c) for c in col)}</div>' for col in COLUMNS) + "</div>"
(FIG / "skeptics.html").write_text(html)
with sync_playwright() as p:
    page = p.chromium.launch().new_page(viewport={"width": 1887, "height": 800}, device_scale_factor=2)
    page.goto((FIG / "skeptics.html").as_uri())
    page.locator("#wrap").screenshot(path=sys.argv[1])
(FIG / "skeptics.html").unlink()
