import sys
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

for f in Path("/usr/local/texlive/2025/texmf-dist/fonts/opentype/public/fira").glob("FiraSans-*.otf"):
    font_manager.fontManager.addfont(f)
matplotlib.rcParams.update({"font.family": "Fira Sans", "font.size": 8, "pdf.fonttype": 3})
BG, INK, MUTED, RULE, ORANGE = "#fafafa", "#23373b", "#6a787b", "#c9d0d1", "#eb811b"

PROBS = [0.5, 19.3, 16.8, 15.0, 10.4, 8.3, 4.5, 4.0, 3.1, 2.6, 2.1, 1.9, 1.5, 1.1, 1.0]
years = list(range(2026, 2026 + len(PROBS)))
later = round(100 - sum(PROBS), 1)

fig, ax = plt.subplots(figsize=(140 / 25.4, 60 / 25.4), facecolor=BG)
ax.set_facecolor(BG)
ax.bar(years, PROBS, color=[ORANGE if y <= 2028 else MUTED for y in years], width=0.7)
ax.bar([2041.2], [later], color=MUTED, width=0.7)
for y, p in zip(years[:6], PROBS[:6]):
    ax.annotate(f"{p:g}%", (y, p), xytext=(0, 3), textcoords="offset points", ha="center", color=INK, weight="bold")
ax.annotate(f"{later:g}%", (2041.2, later), xytext=(0, 3), textcoords="offset points", ha="center", color=INK, weight="bold")
ax.annotate("37% by the end of 2028", (2027, 24), ha="center", color=ORANGE, weight="bold")
ax.annotate("median: late 2029", (2029.9, 17.5), xytext=(2032, 21), color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6))
ax.set_xticks(years[::2] + [2041.2], [str(y) for y in years[::2]] + ["2041+"])
ax.set_ylim(0, 27)
ax.set_yticks([0, 10, 20], ["0%", "10%", "20%"])
ax.set_ylabel("Probability that AGI\narrives in that year", color=INK)
ax.tick_params(colors=MUTED, length=0)
ax.grid(axis="y", color=RULE, lw=0.4)
ax.set_axisbelow(True)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(RULE)
fig.savefig(sys.argv[1], facecolor=BG, bbox_inches="tight", pad_inches=0.05)
