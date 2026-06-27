# Report Writing Guide

## Planning

Fill `experiment_plan.md` before writing the final chapters. The plan should identify:
- experiment goal and course context;
- available evidence: code, data, screenshots, logs, user notes, generated examples;
- chapter-specific claims;
- planned figures, tables, and task-specific scripts under `code/`;
- risks such as missing metadata, missing real outputs, or uncertain environment.

## Default Chapter Structure

### 实验目的

Write 3-5 concrete sentences. Cover what the experiment verifies, what ability it trains, and what result should be obtained.

### 实验原理

Write 3-6 paragraphs. Include definitions, algorithm or system principles, formulas if relevant, and why the chosen method fits the experiment. Add a flowchart or architecture figure only when it clarifies the method.

### 实验内容与步骤

Use two sections:

```latex
\reportsection{（一）实验环境}
\reportsection{（二）实验步骤}
```

For the environment, include OS, language/runtime, compiler/interpreter, libraries, and dataset or input source. For steps, describe the actual workflow in order and include short code snippets only for key logic.

### 结果与分析

Use two sections:

```latex
\reportsection{（一）运行结果}
\reportsection{（二）结果分析}
```

Show results before interpreting them. Use tables for exact values and figures for trends, comparisons, distributions, or workflows. When a figure is needed, write a small Python script for this experiment under `code/` and save the figure to `figures/`. Analyze correctness, performance, edge cases, and likely error sources.

### 心得体会

Write 2-3 paragraphs tied to the specific experiment. Mention concrete problems encountered, how they were solved, and what could be improved.

### 参考文献

Prefer official docs, textbooks, course materials, and papers directly related to the experiment. Remove placeholder references.

## Evidence Rules

- Use user-provided code, screenshots, logs, and data as the primary source of truth.
- If no real result exists, generate a small reproducible demonstration with a local script and state the assumptions in the report.
- Do not fabricate exact performance numbers without either real execution, provided data, or an explicitly simulated example.

## Language Style

- Prefer natural paragraphs with precise transitions.
- Avoid generic sentences such as "本实验让我收获很多" unless followed by concrete detail.
- Keep lists short; use tables when comparing environments, parameters, or results.
- Make every table and figure earn its place with analysis text.
