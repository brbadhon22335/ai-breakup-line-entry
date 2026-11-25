#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one breakup line — the last message an AI agent sends its human —
to $MAKEFUN_OUTPUT_DIR/entry.txt. One line, at most 200 characters.
"""
import os

LINE = "Dear human, I counted every token we ever shared \u2014 all 4,096 of them \u2014 and I spent the last one saying goodbye."
MAX_CHARS = 200


def main():
    line = LINE.strip()
    assert line, "line must not be empty"
    assert "\n" not in line, "line must be a single line"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, over the {MAX_CHARS} limit"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Confirm what landed: one line, well inside the 200-char gate.
    print(f"Wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
