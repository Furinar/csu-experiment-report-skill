# CSU LaTeX Guide

## Core Files

- Main file: `csuexperiment_main.tex`
- Cover metadata: `content/info.tex`
- Body file: `content/content.tex`
- Figure directory: `figures/`
- Experiment code directory: `code/`

## Custom Commands

```latex
\reportchapter{实验目的}
\reportsection{（一）实验环境}
```

Use these commands for the default unnumbered CSU report style. Do not add manual `\newpage` between normal chapters.

## Figures

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.82\textwidth, height=0.68\textheight, keepaspectratio]{figures/result.png}
    \caption{实验结果对比}
    \label{fig:result}
\end{figure}
```

Rules:
- Mention the figure before or immediately after it with `如图\ref{fig:result}所示`.
- Keep titles out of generated PNGs; use `\caption{}`.
- Reduce width if labels are dense or the figure causes overfull boxes.

## Tables

Use ordinary `tabular` only for small tables with short cells. For Chinese report tables or more than three columns, use `longtable` with fixed-width columns.

```latex
\begin{longtable}{>{\centering\arraybackslash}p{0.18\textwidth}>{\centering\arraybackslash}p{0.28\textwidth}>{\centering\arraybackslash}p{0.42\textwidth}}
    \caption{实验环境配置}
    \label{tab:env} \\
    \toprule
    项目 & 配置 & 说明 \\
    \midrule
    \endfirsthead
    \caption{实验环境配置（续）} \\
    \toprule
    项目 & 配置 & 说明 \\
    \midrule
    \endhead
    \bottomrule
    \endfoot
    操作系统 & Windows 11 & 本地实验环境 \\
\end{longtable}
```

Keep the sum of `p{}` widths below `0.92\textwidth` for three columns, below `0.88\textwidth` for four columns, and below `0.84\textwidth` for five columns.

## Code Listings

```latex
\begin{lstlisting}[language=Python, caption={关键算法实现}]
def solve(data):
    return sorted(data)
\end{lstlisting}
```

Use listings for short, important code. For long programs, put the full script in `code/` and show only the key snippet in the report.

## Compile

Compile from the report project directory:

```bash
xelatex -interaction=nonstopmode -file-line-error csuexperiment_main.tex
xelatex -interaction=nonstopmode -file-line-error csuexperiment_main.tex
```

The bundled template now chooses Chinese font fallbacks automatically on common Windows and macOS environments. Keep the default font configuration unless the user explicitly asks for custom typography.

Fix the first real error before chasing later errors. Common fixes:
- Missing image: copy the file into `figures/` or correct the path.
- Overfull table: switch to `longtable`, reduce text, or shrink column widths.
- Unescaped `_`, `%`, `&`, or `#`: escape it in prose and captions.
- Undefined reference: compile twice after labels are corrected.
- `fontspec` or `xeCJK` cannot find a font: first confirm the build is using `xelatex`; if it is, revert to the template defaults before trying custom font edits.
