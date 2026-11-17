import sys
import pathlib

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path

OUT = pathlib.Path(sys.argv[1])
FIRA = pathlib.Path("/usr/local/texlive/2025/texmf-dist/fonts/opentype/public/fira")
for f in FIRA.glob("FiraSans-*.otf"):
    font_manager.fontManager.addfont(f)
matplotlib.rcParams.update({
    "font.family": "Fira Sans",
    "pdf.fonttype": 3,
    "mathtext.fontset": "custom",
    "mathtext.rm": "Fira Sans",
    "mathtext.it": "Fira Sans:italic",
    "mathtext.bf": "Fira Sans:bold",
})

BG, INK, LABEL, MUTED, RULE = "#fafafa", "#23373b", "#3b4d51", "#6a787b", "#c9d0d1"
SOLVED_C, TOPIC_C = "#7b8a8e", "#eb811b"

SOLVED = {2015: 5, 2016: 2, 2017: 3, 2018: 5, 2019: 5, 2020: 5, 2021: 2, 2022: 1, 2023: 1, 2024: 2, 2025: 4}
SOLVED_2026 = 8
OPENAI_EARLY = 3
NAMED = 23
SOLVED_LABELS = {2015: ("Erdős discrepancy problem", -0.7), 2020: ("Connes embedding problem", -5.0), 2024: ("Einstein tile", -0.7)}
CLAIM_LABELS = {
    31: "Matrix multiplication in $O(n^{2.25})$",
    29: "Unique games conjecture",
    27: "No Siegel zeros",
    25: "Hilbert’s tenth problem over $\\mathbf{Q}$",
}

W, H = 140, 61
P, R = 1.55, 0.6
BASE, X0 = 7.0, 7.0
DX = (120.0 - X0) / 11


def year_x(y):
    return X0 + (y - 2015) * DX


def cy(row):
    return BASE + (row + 0.5) * P


def build(stage, path):
    fig = plt.figure(figsize=(W / 25.4, H / 25.4), facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, W), ylim=(0, H), aspect="equal")
    ax.axis("off")
    dots = {SOLVED_C: [], INK: [], TOPIC_C: []}

    def text(x, y, s, size=8, color=LABEL, **kw):
        ax.text(x, y, s, fontsize=size, color=color, **kw)

    def leader(xs, ys):
        ax.plot(xs, ys, color=MUTED, lw=0.4, solid_capstyle="butt")

    def stack_label(x, rows, y, s, dx, ha="left"):
        leader([x, x], [cy(rows - 1) + 1.2, y - 0.8])
        text(x + dx, y, s, va="bottom", ha=ha)

    ax.plot([X0 - 3.5, 124.0], [BASE - 0.6] * 2, color=RULE, lw=0.5)
    for y in range(2015, 2027):
        text(year_x(y), BASE - 2.4, str(y), color=MUTED, va="top", ha="center")
    for year, n in SOLVED.items():
        for r in range(n):
            dots[INK if year in SOLVED_LABELS and r == n - 1 else SOLVED_C].append((year_x(year), cy(r)))
        if year in SOLVED_LABELS:
            stack_label(year_x(year), n, cy(4) + 2.5, *SOLVED_LABELS[year])

    for r in range(SOLVED_2026):
        dots[SOLVED_C].append((year_x(2026), cy(r)))

    text(4.0, 54.8, "43", size=22, weight="bold", color=INK, va="center")
    text(20.5, 54.8, "notable open problems solved\nby mathematicians, 2015–2026", size=8.5, color=INK, va="center", linespacing=1.3)

    if stage == 2:
        x = year_x(2026)
        early, top = SOLVED_2026 + OPENAI_EARLY, SOLVED_2026 + OPENAI_EARLY + NAMED
        for r in range(SOLVED_2026, top):
            dots[TOPIC_C].append((x, cy(r)))
        for r, s in {early - 1: "Navier–Stokes blow-up", **CLAIM_LABELS}.items():
            leader([x - 1.3, x - 3.3], [cy(r)] * 2)
            text(x - 4.1, cy(r), s, va="center_baseline", ha="right")

        y0, y1, bx, bw = cy(early) - 0.7, cy(top - 1) + 0.7, x + 1.6, 2.4
        ym, q = (y0 + y1) / 2, 1.6
        verts = [(bx, y0), (bx + bw / 2, y0), (bx + bw / 2, y0 + q), (bx + bw / 2, ym - q), (bx + bw / 2, ym), (bx + bw, ym),
                 (bx + bw / 2, ym), (bx + bw / 2, ym + q), (bx + bw / 2, y1 - q), (bx + bw / 2, y1), (bx, y1)]
        codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.CURVE3, Path.CURVE3]
        ax.add_patch(PathPatch(Path(verts, codes), facecolor="none", edgecolor=INK, lw=0.7))
        text(bx + bw + 1.2, ym, "6 Oct\nOpenAI", color=INK, weight="bold", va="center", linespacing=1.3)

        text(4.0, 43.4, "26", size=22, weight="bold", color=TOPIC_C, va="center")
        text(20.5, 43.4, "results claimed by OpenAI in 2026,\n23 of them in one release on 6 October", size=8.5, color=INK, va="center", linespacing=1.3)
        text(20.5, 36.5, "Claims, largely unverified so far", color=MUTED, va="center_baseline")

    for color, pts in dots.items():
        ax.add_collection(PatchCollection([Circle(p, R) for p in pts], facecolor=color, edgecolor="none"))
    fig.savefig(path, facecolor=BG)
    plt.close(fig)


build(1, OUT / "maths_decade_stage1.pdf")
build(2, OUT / "maths_decade_stage2.pdf")
