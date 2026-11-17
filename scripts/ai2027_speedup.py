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
SCENARIO = [
    (date(2026, 2, 15), 1.5, "Agent-1"),
    (date(2026, 12, 1), 2, ""),
    (date(2027, 1, 15), 3, ""),
    (date(2027, 3, 15), 4, "Agent-3"),
    (date(2027, 6, 15), 10, ""),
    (date(2027, 8, 15), 25, ""),
    (date(2027, 9, 15), 50, "Agent-4"),
]
OBSERVED = [(date(2025, 10, 7), 1), (date(2026, 10, 15), 4.5)]
TAKEOVER = date(2027, 11, 15)

fig, ax = plt.subplots(figsize=(140 / 25.4, 62 / 25.4), facecolor=BG)
ax.set_facecolor(BG)
xs, ys = [d for d, _, _ in SCENARIO], [y for _, y, _ in SCENARIO]
ax.plot(xs, ys, color=INK, lw=1.6, marker="o", ms=4)
for d, y, label in SCENARIO:
    ax.annotate(f"{y:g}×", (d, y), xytext=(-5, 4), textcoords="offset points", ha="right", color=INK, weight="bold")
    if label:
        above = label == "Agent-4"
        ax.annotate(label, (d, y), xytext=(0, 7) if above else (9, -2), textcoords="offset points", ha="center" if above else "left", va="bottom" if above else "center", color=MUTED)
ax.plot(*zip(*OBSERVED), color=ORANGE, lw=2.2, marker="o", ms=5)
ax.axvline(TAKEOVER, color="#a01c1c", lw=1.2, ls="--")
ax.annotate("November 2027:\nhumans lose control", (TAKEOVER, 1.3), xytext=(6, 0), textcoords="offset points",
            ha="left", va="bottom", color="#a01c1c", weight="bold", linespacing=1.3)
ax.set_yscale("log")
ax.set_ylim(1, 100)
ax.set_yticks([1, 2, 5, 10, 20, 50, 100], ["1×", "2×", "5×", "10×", "20×", "50×", "100×"])
ax.minorticks_off()
ax.set_xlim(date(2025, 8, 1), date(2028, 7, 1))
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.set_ylabel("Speed-up of algorithmic progress\nin the AI 2027 scenario", color=INK)
ax.tick_params(colors=MUTED, length=0)
ax.grid(axis="y", color=RULE, lw=0.4)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(RULE)
fig.savefig(sys.argv[1], facecolor=BG, bbox_inches="tight", pad_inches=0.05)
