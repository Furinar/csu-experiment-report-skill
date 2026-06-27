#!/usr/bin/env python3
"""Scaffold a CSU experiment report project."""
import argparse
import shutil
from pathlib import Path
from string import Template


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold CSU experiment report")
    parser.add_argument("--output", "-o", required=True, help="Output directory")
    parser.add_argument("--title", required=True, help="Experiment title")
    parser.add_argument("--author", required=True, help="Student name")
    parser.add_argument("--studentid", required=True, help="Student ID")
    parser.add_argument("--myclass", required=True, help="Class/major")
    parser.add_argument("--supervisor", required=True, help="Supervisor name")
    parser.add_argument("--department", required=True, help="Department/college")
    parser.add_argument("--finishdate", default="", help="Completion date")
    args = parser.parse_args()

    if not args.finishdate:
        from datetime import datetime
        now = datetime.now()
        args.finishdate = f"{now.year}年{now.month}月"

    skill_dir = Path(__file__).resolve().parent.parent
    assets = skill_dir / "assets"
    templates = assets / "templates"
    out = Path(args.output).resolve()

    for subdir in ["content", "figures", "images", "code", "data"]:
        (out / subdir).mkdir(parents=True, exist_ok=True)

    for filename in [
        "csuexperiment.cls",
        "csuexperiment_style.cls",
        "KaiTi_GB2312.ttf",
        "latexmkrc",
        "Makefile",
    ]:
        copy_file(assets / filename, out / filename)

    for image in (assets / "images").iterdir():
        if image.is_file():
            copy_file(image, out / "images" / image.name)

    copy_file(templates / "main.tex", out / "csuexperiment_main.tex")
    copy_file(templates / "content.tex", out / "content" / "content.tex")
    copy_file(templates / "experiment_plan.md", out / "experiment_plan.md")

    info_template = (templates / "info.tex").read_text(encoding="utf-8")
    info_filled = Template(info_template).safe_substitute(
        titlecn=args.title,
        author=args.author,
        studentid=args.studentid,
        myclass=args.myclass,
        supervisor=args.supervisor,
        department=args.department,
        finishdate=args.finishdate,
    )
    (out / "content" / "info.tex").write_text(info_filled, encoding="utf-8")

    print(f"Project scaffolded at: {out}")
    print(f"Main file: {out / 'csuexperiment_main.tex'}")
    print(f"Plan file: {out / 'experiment_plan.md'}")
    print("Next: fill experiment_plan.md and content/content.tex, then compile with xelatex twice.")


if __name__ == "__main__":
    main()
