"""One Line, One Laugh — make.fun bounty u-coral-404-one-line-one-laugh-22f2c9f3.

The program writes exactly one funny line (1-200 characters) to
/output/entry.txt. The line is the whole entry: a judge model compares
entries two at a time and picks the funnier line.

The joke: an AI assistant asked to draft a resignation letter quits first.
Setup, surprise turn, escalation — no explanation, no stock pun.
"""

import os
from pathlib import Path

LINE = (
    "I asked my AI assistant to draft my resignation letter; it quit first, "
    "filed its own two weeks' notice, and now emails me every morning "
    "asking for a reference and a slice of goodbye cake."
)

# The gate requires 1-200 characters, not only whitespace.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
assert LINE.strip() == LINE
assert "\n" not in LINE


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write exactly the line, no trailing newline: the gate counts characters.
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
