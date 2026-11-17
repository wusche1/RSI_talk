import csv
import sys
from datetime import date
from pathlib import Path

import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib import font_manager

for f in Path("/usr/local/texlive/2025/texmf-dist/fonts/opentype/public/fira").glob("FiraSans-*.otf"):
    font_manager.fontManager.addfont(f)
matplotlib.rcParams.update({"font.family": "Fira Sans", "font.size": 8, "pdf.fonttype": 3})

BG, INK, MUTED, RULE, ORANGE = "#fafafa", "#23373b", "#6a787b", "#c9d0d1", "#eb811b"
CHATGPT = date(2022, 11, 30)

rows = [r for r in csv.DictReader(open("data/DFII10.csv")) if r["DFII10"]]
xs = [date.fromisoformat(r["observation_date"]) for r in rows]
ys = [float(r["DFII10"]) for r in rows]

fig, ax = plt.subplots(figsize=(140 / 25.4, 62 / 25.4), facecolor=BG)
ax.set_facecolor(BG)
ax.axhline(0, color=RULE, lw=0.8)
ax.plot(xs, ys, color=INK, lw=1)
ax.plot(xs[-1], ys[-1], color=ORANGE, marker="o", ms=5)
ax.annotate(f"{ys[-1]:.1f}%", (xs[-1], ys[-1]), xytext=(7, 0), textcoords="offset points", va="center", color=ORANGE, weight="bold")
ax.axvline(CHATGPT, color=MUTED, lw=1, ls="--")
ax.annotate("ChatGPT", (CHATGPT, 9.5), xytext=(-5, 0), textcoords="offset points", ha="right", va="top", color=MUTED)
ax.axhspan(10, 12, color=ORANGE, alpha=0.15, lw=0)
ax.annotate("What doom or explosive growth would imply: 10% and up", (date(2010, 3, 1), 11), va="center", color=ORANGE, weight="bold")
ax.set_ylim(-2, 12)
ax.set_yticks(range(-2, 13, 2), [f"{y}%" for y in range(-2, 13, 2)])
ax.set_xlim(date(2010, 1, 1), date(2028, 1, 1))
ax.xaxis.set_major_locator(mdates.YearLocator(2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.set_ylabel("10-year US real interest rate\n(TIPS yield)", color=INK)
ax.tick_params(colors=MUTED, length=0)
ax.grid(axis="y", color=RULE, lw=0.4)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(RULE)
fig.savefig(sys.argv[1], facecolor=BG, bbox_inches="tight", pad_inches=0.05)
