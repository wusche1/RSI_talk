import json
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

for f in Path("/usr/local/texlive/2025/texmf-dist/fonts/opentype/public/fira").glob("FiraSans-*.otf"):
    font_manager.fontManager.addfont(f)
matplotlib.rcParams.update({"font.family": "Fira Sans", "font.size": 8, "pdf.fonttype": 3})
BG, INK, MUTED, RULE, ORANGE = "#fafafa", "#23373b", "#6a787b", "#c9d0d1", "#eb811b"

events = defaultdict(list)
for m in json.load(open(sys.argv[1])):
    events[m["event_ticker"]].append(m)
years, probs = [], []
for ticker, markets in sorted(events.items()):
    top = max(markets, key=lambda m: m.get("floor_strike") or -9)
    years.append(2000 + int(ticker.split("-")[1]))
    probs.append(100 * float(top["last_price_dollars"]))

fig, ax = plt.subplots(figsize=(140 / 25.4, 60 / 25.4), facecolor=BG)
ax.set_facecolor(BG)
ax.bar(years, probs, color=ORANGE, width=0.6)
for y, p in zip(years, probs):
    ax.annotate(f"{p:g}%", (y, p), xytext=(0, 3), textcoords="offset points", ha="center", color=INK, weight="bold")
ax.set_ylim(0, 100)
ax.set_yticks([0, 25, 50, 75, 100], ["0%", "25%", "50%", "75%", "100%"])
ax.set_xticks(years)
ax.set_ylabel("Market price of US real GDP\ngrowth above 6% in that year", color=INK)
ax.tick_params(colors=MUTED, length=0)
ax.grid(axis="y", color=RULE, lw=0.4)
ax.set_axisbelow(True)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(RULE)
fig.savefig(sys.argv[2], facecolor=BG, bbox_inches="tight", pad_inches=0.05)
