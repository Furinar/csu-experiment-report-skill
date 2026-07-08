# Figure Guidance

Use Mrite-style task-specific plotting: write a small Python script for the current experiment instead of relying on generic chart commands. Save the script in the generated report project's `code/` directory and save final images in `figures/`.

## Workflow

1. Read real experiment data, logs, or code outputs when available.
2. Compute all numeric results first and print key statistics for the report.
3. Plot only after calculation is complete.
4. Save figures as PNG files under `figures/`.
5. Reference each figure from `content/content.tex` with a LaTeX caption and analysis paragraph.

## Python Pattern

```python
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
FIG_DIR = BASE_DIR / "figures"
FIG_DIR.mkdir(exist_ok=True)

plt.rcParams["font.sans-serif"] = [
    "SimHei", "Microsoft YaHei", "STHeiti", "PingFang SC", "DejaVu Sans"
]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.dpi"] = 180
plt.rcParams["savefig.dpi"] = 180

# First calculate results.
x = np.array([100, 500, 1000, 5000])
y = np.array([1.2, 4.8, 9.7, 51.3])
print(f"min={y.min():.3f}, max={y.max():.3f}, mean={y.mean():.3f}, std={y.std():.3f}")

# Then draw the figure.
fig, ax = plt.subplots(figsize=(7.5, 4.8))
ax.plot(x, y, marker="o", linewidth=1.8, label="实验结果")
ax.set_xlabel("输入规模")
ax.set_ylabel("运行时间/ms")
ax.grid(alpha=0.28, linestyle="--")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(FIG_DIR / "runtime.png", bbox_inches="tight")
plt.close(fig)
```

These matplotlib font fallbacks are independent from the LaTeX template fonts. Keep both layers on their defaults unless the user explicitly wants custom typography.

## Style Rules

- Do not draw a chart title in Python; use LaTeX `\caption{}`.
- Keep figures readable: data, axes, ticks, legends, and necessary annotations only.
- Use Chinese labels for Chinese reports.
- Prefer line charts for trends, bar charts for category comparisons, scatter plots for relationships, heatmaps for matrices, and boxplots or histograms for distributions.
- Use reproducible simulated data only when real results are unavailable, and state that assumption in the report.
