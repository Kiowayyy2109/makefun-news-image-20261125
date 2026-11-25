#!/usr/bin/env python3
"""make.fun news-image-20261125 entry (Python 3.13, standard library only).

The image beside this file, entry.png, sums up the world news of
Wednesday 25 November 2026. This program copies it to the output
directory, exactly like the kit's starter: outside the grader's
container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    # copyfile is byte-for-byte, so two runs write identical bytes.
    shutil.copyfile(HERE / "entry.png", out / "entry.png")


if __name__ == "__main__":
    main()
