import sys
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

for f in Path("/usr/local/texlive/2025/texmf-dist/fonts/opentype/public/fira").glob("FiraSans-*.otf"):
    font_manager.fontManager.addfont(f)
matplotlib.rcParams.update({"font.family": "Fira Sans", "font.size": 8, "pdf.fonttype": 3})
BG, INK, MUTED, RULE, RED = "#fafafa", "#23373b", "#6a787b", "#c9d0d1", "#a01c1c"

ROWS = [
    ("Cunningham et al., September", "Anthropic survey: 4× productivity", 0, 0.6, "at most 0.6", "left"),
    ("Naam, September", "OpenAI logs: 1.6× experiments", 0.1, 0.2, "0.1 to 0.2", "left"),
    ("AI Futures Project, November", "METR: progress at 2× the usual rate", 0.8, 1.0, "“probably approaching 1”", "right"),
]

for stage in range(1, 5):
    fig = plt.figure(figsize=(140 / 25.4, 60 / 25.4), facecolor=BG)
    ax = fig.add_axes([0.37, 0.18, 0.61, 0.7])
    ax.set_facecolor(BG)
    ax.axvspan(1, 1.42, color=RED, alpha=0.08, lw=0)
    ax.axvline(1, color=RED, lw=1.4)
    ax.text(1.02, 3.3, "self-sustaining", color=RED, weight="bold", size=9, va="center")
    ax.text(0.98, 3.3, "fizzles out", color=MUTED, size=9, va="center", ha="right")
    labels = ax.get_yaxis_transform()
    for i, (who, basis, lo, hi, value, side) in enumerate(ROWS[: stage - 1]):
        y = 2.4 - i
        ax.barh(y, hi - lo, left=lo, height=0.36, color=MUTED)
        ax.text(-0.03, y + 0.17, who, color=INK, weight="bold", va="center", ha="right", transform=labels)
        ax.text(-0.03, y - 0.17, basis, color=MUTED, va="center", ha="right", transform=labels)
        if side == "left":
            ax.text(hi + 0.02, y, value, color=INK, weight="bold", size=9, va="center")
        else:
            ax.text(lo - 0.02, y, value, color=INK, weight="bold", size=9, va="center", ha="right")
    ax.set_xlim(0, 1.42)
    ax.set_ylim(-0.1, 3.6)
    ax.set_yticks([])
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1], ["0", "0.25", "0.5", "0.75", "1"])
    ax.set_xlabel("Loop strength today", color=INK)
    ax.tick_params(colors=MUTED, length=0)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(RULE)
    fig.savefig(f"{sys.argv[1]}/rsi_loop_strength_stage{stage}.pdf", facecolor=BG)
    plt.close(fig)
