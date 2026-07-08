<div align="center">

# 🌟 CSU Experiment Report Skill

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=1E90FF&center=true&vCenter=true&width=560&lines=CSU+Experiment+Report+Skill;Mrite-style+workflow+for+CSU+reports;%E4%B8%AD%E5%8D%97%E5%A4%A7%E5%AD%A6%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E7%94%9F%E6%88%90%E6%8A%80%E8%83%BD)](https://git.io/typing-svg)

**中南大学实验报告 Codex Skill**

_基于 CSU LaTeX 模板与 Mrite 式工作流，帮助 Codex 自动完成实验规划、证据生成、报告撰写与 PDF 编译_

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-1E90FF?style=for-the-badge)]()
[![LaTeX](https://img.shields.io/badge/LaTeX-XeLaTeX-008080?style=flat-square&logo=latex&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![CSU](https://img.shields.io/badge/CSU-%E4%B8%AD%E5%8D%97%E5%A4%A7%E5%AD%A6-1E90FF?style=flat-square)]()

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=1E90FF&height=80&section=header" />

## 目录

<div align="center">

[![简介](https://img.shields.io/badge/-简介-1E90FF?style=for-the-badge)](#简介)&nbsp;
[![核心思想](https://img.shields.io/badge/-核心思想-00BFFF?style=for-the-badge)](#核心思想)&nbsp;
[![功能特色](https://img.shields.io/badge/-功能特色-87CEFA?style=for-the-badge)](#功能特色)&nbsp;
[![项目结构](https://img.shields.io/badge/-项目结构-4682B4?style=for-the-badge)](#项目结构)

[![使用方式](https://img.shields.io/badge/-使用方式-1E90FF?style=for-the-badge)](#使用方式)&nbsp;
[![生成流程](https://img.shields.io/badge/-生成流程-00BFFF?style=for-the-badge)](#生成流程)&nbsp;
[![依赖环境](https://img.shields.io/badge/-依赖环境-87CEFA?style=for-the-badge)](#依赖环境)

</div>

## 简介

`csu-experiment-report-skill` 是一个用于 **中南大学实验报告** 生成的 Codex Skill。它不是一个复杂命令行工具箱，而是一套面向 Codex 的实验报告工作流说明与 CSU LaTeX 模板资源。

当用户要求生成、改写或编译实验报告时，Codex 会使用该 Skill 完成从报告工程搭建、实验计划整理、必要证据生成、正文撰写到 XeLaTeX 编译检查的完整流程。

## 核心思想

本 Skill 参考了 Mrite 的工作方式：**先理解任务，再写计划，再按实验本身生成证据，最后撰写和编译报告**。

它刻意保持轻量：

- 只保留一个脚手架脚本 `scaffold.py`
- 不内置通用画图命令
- 不要求用户理解 `--type bar_chart` 这类内部参数
- 需要图表时，由 Codex 在报告项目的 `code/` 目录中临场编写本实验专用 Python 脚本
- 结果图片统一保存到 `figures/`，并在 LaTeX 中通过 `\caption{}` 命名与解释

## 功能特色

| 能力 | 说明 |
| --- | --- |
| **CSU 报告模板** | 内置中南大学实验报告 LaTeX 模板、校徽资源与封面信息模板 |
| **Mrite 式规划** | 先生成 `experiment_plan.md`，明确实验目标、证据来源、图表规划与风险 |
| **单文件正文** | 默认使用 `content/content.tex` 承载完整正文，避免实验报告项目过碎 |
| **专用证据脚本** | 按实验需要在 `code/` 下编写 Python 脚本，生成可复现实验结果与图表 |
| **标准章节结构** | 默认包含实验目的、实验原理、实验内容与步骤、结果与分析、心得体会、参考文献 |
| **编译检查** | 使用 XeLaTeX 两遍编译，并检查日志中的错误、缺图、引用和排版问题 |

## 项目结构

<details>
<summary><b>点击展开核心目录结构</b></summary>

```text
csu-experiment-report-skill/
├── SKILL.md                         # Codex Skill 入口说明
├── agents/
│   └── openai.yaml                  # Codex UI 元数据
├── scripts/
│   └── scaffold.py                  # 唯一脚本：生成 CSU 实验报告工程骨架
├── references/
│   ├── report-writing.md            # 报告写作与章节规范
│   ├── latex-guide.md               # LaTeX 图表、代码、编译说明
│   └── figure-types.md              # Mrite 式专用 Python 绘图规范
└── assets/
    ├── csuexperiment.cls            # CSU 实验报告 LaTeX 类
    ├── csuexperiment_style.cls      # 模板样式
    ├── KaiTi_GB2312.ttf             # 字体资源
    ├── images/                      # CSU Logo 资源
    └── templates/
        ├── main.tex                 # 主 LaTeX 文件模板
        ├── info.tex                 # 封面信息模板
        ├── content.tex              # 单文件正文模板
        └── experiment_plan.md       # 实验计划模板
```

</details>

生成报告后，目标项目通常类似：

```text
csu-experiment-report/
├── csuexperiment_main.tex
├── content/
│   ├── info.tex
│   └── content.tex
├── figures/                         # 结果图片
├── code/                            # 本实验专用 Python 脚本
├── data/                            # 实验数据或附件
├── images/                          # 模板图片资源
└── experiment_plan.md               # 生成前的实验计划
```

## 使用方式

### 安装到 Codex Skills

将仓库放到 Codex skills 目录下，例如：

```bash
git clone https://github.com/Furinar/csu-experiment-report-skill.git ~/.codex/skills/csu-experiment-report-skill
```

Windows 环境可放到：

```text
C:\Users\<你的用户名>\.codex\skills\csu-experiment-report-skill
```

### 在 Codex 中使用

对 Codex 说类似下面的话即可：

```text
使用 $csu-experiment-report-skill 帮我生成一份中南大学操作系统进程调度实验报告。
```

也可以提供更多材料：

```text
请根据我给的 Python 代码、运行截图和实验要求，生成一份 CSU 实验报告并编译成 PDF。
```

## 生成流程

1. **搭建工程**

   Codex 调用 `python3 scripts/scaffold.py` 生成 CSU LaTeX 报告项目。

2. **写实验计划**

   在 `experiment_plan.md` 中整理实验目标、输入材料、步骤、图表和风险。

3. **生成证据**

   如果需要结果图或表格，Codex 在 `code/` 下编写本实验专用 Python 脚本，运行后将图片保存到 `figures/`。

4. **撰写正文**

   Codex 填写 `content/content.tex`，默认章节包括：

   - 实验目的
   - 实验原理
   - 实验内容与步骤
   - 结果与分析
   - 心得体会
   - 参考文献

5. **编译 PDF**

   在报告项目目录执行：

   ```bash
   xelatex -interaction=nonstopmode -file-line-error csuexperiment_main.tex
   xelatex -interaction=nonstopmode -file-line-error csuexperiment_main.tex
   ```

   模板会在 Windows 和 macOS 上自动选择可用的中文字体回退；正常情况下不需要手动修改字体配置。

6. **检查修复**

   Codex 根据 `.log` 检查 LaTeX 错误、图片缺失、引用未定义、表格溢出等问题，并修复到 PDF 可用。

## 依赖环境

| 类别 | 说明 |
| --- | --- |
| **Codex** | 用于识别并执行 Skill 工作流 |
| **Python 3** | 用于运行 `scaffold.py`，以及按实验临场生成结果图表 |
| **XeLaTeX** | 用于编译 CSU 实验报告 PDF；Windows 推荐 TeX Live 或 MiKTeX，macOS 推荐 MacTeX |
| **matplotlib** | 当实验需要图表时，由 Codex 编写专用 Python 脚本使用 |

## 平台支持

- 支持 Windows 和 macOS 的常见 XeLaTeX 环境。
- 中文字体默认按平台自动回退，目标是免配置编译成功；两端字形可能略有差异，但版式应保持稳定。
- `make view` 在 macOS 使用 `open`，在 Linux 使用 `xdg-open`；Windows 可直接双击生成的 PDF 文件。

## 设计取舍

本项目不提供通用画图命令，也不封装额外编译脚本。这样做是为了让 Skill 保持清晰：

- 模板搭建是稳定重复工作，交给 `scaffold.py`
- 实验结果和图表高度依赖具体题目，交给 Codex 临场写专用脚本
- 编译流程是标准 XeLaTeX，两条命令足够透明

这使得 Skill 更接近“实验报告写作代理的工作指南”，而不是难以维护的参数化工具集合。

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=1E90FF&height=80&section=footer" />

<div align="center">

<sub>Made for CSU experiment reports</sub>

<br />

<a href="#-csu-experiment-report-skill">
  <img src="https://img.shields.io/badge/Back_to_Top-1E90FF?style=for-the-badge" alt="Back to Top" />
</a>

</div>
