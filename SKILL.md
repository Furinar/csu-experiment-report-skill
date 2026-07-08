---
name: csu-experiment-report-skill
description: Generate complete Central South University (CSU, 中南大学) experiment reports as polished, compilable XeLaTeX projects and PDFs. Use when Codex is asked to create, draft, improve, or compile a CSU 实验报告, including cover metadata, experiment planning, Chinese report chapters, code listings, data/result tables, matplotlib figures, references, and PDF validation. Works with topic-only, partial-outline, existing-code, existing-image, existing-data, or user-provided .tex inputs.
---

# CSU Experiment Report Skill

Create a complete CSU experiment report with a Mrite-style workflow: understand the experiment, write a short plan, run or synthesize reproducible evidence when needed, write the report, then compile and fix it. Keep the user experience simple; do not expose internal plotting commands or ask the user to choose script parameters.

## Operating Mode

- Proceed automatically when the user provides an experiment topic or materials.
- Ask at most once for missing cover metadata when a final submit-ready report clearly needs it. If speed matters, use visible placeholders such as `待填写姓名`.
- Use the default CSU chapter structure unless the user provides a custom structure or a complete `content.tex`.
- Base results on user-provided code, data, screenshots, logs, or a reproducible script written for this specific experiment.
- Write formal Chinese report prose. Avoid generic filler and remove all template instruction text from final `.tex` files.
- Assume the bundled template should compile on common Windows and macOS XeLaTeX environments without manual font edits; if XeLaTeX itself is missing, report that prerequisite clearly.

## Workflow

1. **Scaffold the report**
   Run the only bundled script:
   ```bash
   python3 <skill_dir>/scripts/scaffold.py \
     --output <output_dir> \
     --title "<experiment title>" \
     --author "<student name or placeholder>" \
     --studentid "<student ID or placeholder>" \
     --myclass "<class/major or placeholder>" \
     --supervisor "<supervisor or placeholder>" \
     --department "<department or placeholder>" \
     --finishdate "<date, optional>"
   ```
   Default output directory: `./csu-experiment-report/`.

2. **Plan first**
   Fill `<output_dir>/experiment_plan.md` before writing the final report. Capture the experiment objective, available evidence, planned steps, expected figures/tables, and risks.

3. **Produce evidence**
   If figures or result tables are needed, write a task-specific Python script under `<output_dir>/code/`. The script should load real data when available or generate a clearly reproducible demonstration, print key statistics, and save figures to `<output_dir>/figures/`.

4. **Write the report**
   Fill `<output_dir>/content/content.tex` using the default chapters:
   实验目的, 实验原理, 实验内容与步骤, 结果与分析, 心得体会, 参考文献.

5. **Compile and repair**
   Run XeLaTeX twice from `<output_dir>`:
   ```bash
   xelatex -interaction=nonstopmode -file-line-error csuexperiment_main.tex
   xelatex -interaction=nonstopmode -file-line-error csuexperiment_main.tex
   ```
   The bundled template selects reasonable Chinese font fallbacks for Windows and macOS automatically. Do not ask the user to edit the font configuration unless they explicitly want custom typography.
   Inspect the `.log` file for errors, missing figures, undefined references, overfull boxes, and obvious layout problems. Fix and recompile until the PDF is usable.

6. **Report result**
   Give the final PDF path, project path, and any remaining placeholders or manual review items.

## Quality Bar

- Every figure and table must be introduced and interpreted in nearby text.
- Put chart titles in LaTeX `\caption{}`. Python figures should contain only data, axes, ticks, legends, and necessary annotations.
- Use short code listings for key logic; place long generated scripts in `code/` and reference them in the report or appendix.
- Prefer `longtable` with fixed-width columns for wide Chinese tables.
- References must match the actual experiment topic and tools used.

## Reference Map

- `references/report-writing.md` — chapter-level writing standards and planning rules.
- `references/latex-guide.md` — CSU LaTeX commands, tables, figures, code listings, and compilation fixes.
- `references/figure-types.md` — Mrite-style Python plotting guidance for task-specific figures.
