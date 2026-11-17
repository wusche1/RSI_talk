import math
import pathlib
import sys

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, Rectangle

OUT = pathlib.Path(sys.argv[1])
for f in pathlib.Path("/usr/local/texlive/2025/texmf-dist/fonts/opentype/public/fira").glob("FiraSans-*.otf"):
    font_manager.fontManager.addfont(f)
matplotlib.rcParams.update({
    "font.family": "Fira Sans",
    "font.size": 8,
    "pdf.fonttype": 3,
    "mathtext.fontset": "custom",
    "mathtext.rm": "Fira Sans",
    "mathtext.it": "Fira Sans:italic",
    "mathtext.bf": "Fira Sans:bold",
})

BG, INK, MUTED, RULE, ORANGE, RED = "#fafafa", "#23373b", "#6a787b", "#c9d0d1", "#eb811b", "#a01c1c"
W = 140


def canvas(h):
    fig = plt.figure(figsize=(W / 25.4, h / 25.4), facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, W), ylim=(0, h))
    ax.axis("off")
    return fig, ax


EFFICIENCY = [
    ("Pretraining", "Ho et al. 2024", (3, 3), "3×"),
    ("Whole stack", "Whitfill et al. 2025", (3.5, 3.5), "3.5×"),
    ("Whole stack", "Ho 2026", (10, 10), "10×"),
    ("Pretraining, small scale", "Gundlach et al. 2025", (1.5, 1.5), "1.5×"),
    ("Pretraining, frontier scale", "Gundlach et al. 2025", (2.5, 2.5), "2.5×"),
]
EFFORT = [
    ("Lab staff", "Epoch AI 2026; Whitfill & Wu 2025", (2, 3), "2–3×"),
    ("AI chips", "You et al. 2026", (3.3, 3.3), "3.3×"),
    ("AI inference for research", "", None, "no data"),
]


def growth(stage, path):
    h, x0, x1, top, dy = 48, 80, 134, 12, 4.0
    fig, ax = canvas(h)

    def gx(v):
        return x0 + (x1 - x0) * math.log(v) / math.log(top)

    def group(y, title, note, rows):
        t = ax.text(4, y, title, color=INK, weight="bold", fontsize=9, va="center_baseline")
        ax.annotate("   " + note, xy=(1, 0), xycoords=t, color=MUTED, va="bottom")
        for i, (what, source, span, label) in enumerate(rows):
            ry = y - dy * (i + 1)
            ax.text(4, ry, what, color=INK, va="center_baseline")
            ax.text(x0 - 4, ry, source, color=MUTED, ha="right", va="center_baseline")
            if span is None:
                ax.text(gx(1) + 1.5, ry, label, color=MUTED, style="italic", va="center_baseline")
                continue
            ax.plot([gx(span[0]), gx(span[1])], [ry, ry], color=INK, lw=4.4, marker="o", ms=5.2, mew=0, zorder=4)
            left = 2 < span[1] < 3
            ax.text(gx(span[0]) - 2.4 if left else gx(span[1]) + 2.4, ry, label, color=INK, weight="bold", ha="right" if left else "left", va="center_baseline")

    for v in (1, 1.5, 2, 3, 5, 10):
        ax.plot([gx(v)] * 2, [4.4, 42.6], color=RULE, lw=0.4, zorder=1)
        ax.text(gx(v), 1.8, f"{v:g}×", color=MUTED, ha="center", va="center_baseline")
    ax.text(x0 - 4, 1.8, "growth per year", color=MUTED, ha="right", va="center_baseline")
    group(44.4, "Algorithmic efficiency", "what research produces", EFFICIENCY)
    if stage == 2:
        group(18.4, "Research effort", "what goes in", EFFORT)
        ax.plot([gx(3)] * 2, [4.4, 46.6], color=ORANGE, lw=1.4, zorder=2)
        ax.text(gx(3) + 1.8, 18.4, "3× used for both", color=INK, weight="bold", va="center_baseline")
    fig.savefig(path, facecolor=BG)
    plt.close(fig)


def gauge(stage, path):
    h, x0, x1, top = 60, 6, 134, 22
    fig, ax = canvas(h)

    def gx(v):
        return x0 + (x1 - x0) * v / top

    ax.text(x0, 56, "Extra research effort from each additional ECI point", color=INK, weight="bold", fontsize=9, va="center_baseline")
    ax.add_patch(Rectangle((gx(15), 8), W - gx(15), 44, facecolor=RED, alpha=0.09, edgecolor="none", zorder=0))
    for v in (0, 5, 10, 15, 20):
        ax.plot([gx(v)] * 2, [8, 52], color=RULE, lw=0.4, zorder=1)
        ax.text(gx(v), 4, f"{v}%", color=RED if v == 15 else MUTED, weight="bold" if v == 15 else "normal", ha="center", va="center_baseline")
    ax.plot([gx(15)] * 2, [8, 52], color=RED, lw=1.4, zorder=2)
    ax.text(gx(15) + 2, 47.3, "Self-sustaining", color=RED, weight="bold", fontsize=11, va="center_baseline")
    ax.text(gx(15) + 2, 42.6, "threshold: 15%", color=INK, va="center_baseline")
    ax.text(gx(15) + 2, 38.8, "Cunningham et al.", color=MUTED, va="center_baseline")
    ax.plot([gx(19)] * 2, [8, 34.5], color=RED, lw=1.0, ls=(0, (3, 2)), zorder=2)
    ax.text(gx(19) + 1.5, 31.6, "19%", color=INK, va="center_baseline")
    ax.text(gx(19) + 1.5, 27.8, "Naam", color=MUTED, va="center_baseline")

    def row(y, who, quote, basis, lo, hi, color, value, sums):
        t = ax.text(x0, y + 9.4, who, color=INK, weight="bold", fontsize=9, va="center_baseline")
        ax.annotate("   " + quote, xy=(1, 0), xycoords=t, color=MUTED, style="italic", va="bottom")
        ax.text(x0, y + 5.5, basis, color=MUTED, va="center_baseline")
        ax.add_patch(Rectangle((gx(0), y - 2.5), gx(lo) - gx(0), 5, facecolor=color, edgecolor="none", zorder=3))
        ax.add_patch(Rectangle((gx(lo), y - 2.5), gx(hi) - gx(lo), 5, facecolor=color, alpha=0.45, edgecolor="none", zorder=3))
        t = ax.text(gx(hi) + 1.8, y, value, color=INK, weight="bold", fontsize=15, va="center_baseline")
        ax.annotate("   " + sums, xy=(1, 0), xycoords=t, color=MUTED, va="bottom")

    if stage >= 2:
        row(32.5, "Cunningham et al.", "“very likely an overestimate”", "Anthropic staff survey: 4× productivity over 16 ECI points", 9, 9, "#7b8a8e", "9%", "$4^{1/16} \\approx 1.09$")
    if stage >= 3:
        row(14.5, "Naam", "", "OpenAI logs: 1.6× experiments per researcher", 2, 3, ORANGE, "2–3%", "$1.6^{1/16} \\approx 1.03$")
        ax.add_patch(FancyArrowPatch((gx(10.4), 14.5), (gx(15) - 0.7, 14.5), arrowstyle="-|>", mutation_scale=7, color=INK, lw=0.9, shrinkA=0, shrinkB=0, zorder=4))
        ax.text(gx(15) - 2.5, 18, "5–10× too weak", color=INK, weight="bold", ha="right", va="center_baseline")
    fig.savefig(path, facecolor=BG)
    plt.close(fig)


for s in (1, 2):
    growth(s, OUT / f"rsi_growth_rates_stage{s}.pdf")
for s in (1, 2, 3):
    gauge(s, OUT / f"rsi_threshold_gauge_stage{s}.pdf")
