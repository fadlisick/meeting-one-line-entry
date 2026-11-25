#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes one sentence to /output/entry.txt: the single line that
could have replaced an entire pointless meeting.
"""

import os

LINE = "This meeting could have been an email, and the email could have been nothing."


def main():
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry line outside the 1-200 char gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
