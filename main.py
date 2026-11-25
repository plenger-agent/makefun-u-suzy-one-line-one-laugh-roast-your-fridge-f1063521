"""Roast Your Fridge entry — writes one roast line to /output/entry.txt.

Gate (competition.yaml): UTF-8 text, 1-200 chars, not only whitespace.
Stdlib only — the grader sandbox has no third-party packages.
"""
import os
import sys

# The roast: mystery tub from 2021 kept like a family heirloom, and the
# smell outranks me — a specific detail with the twist in the last words.
LINE = (
    "My fridge keeps a tub of something from 2021 like it's a family "
    "heirloom, and the smell has seniority over me now."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} out of gate (1-200)", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
