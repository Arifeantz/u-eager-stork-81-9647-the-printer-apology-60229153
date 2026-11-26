"""The Printer Apology — make.fun bounty entry.

Writes one apology line, spoken by an office printer to its office,
to /output/entry.txt. The line is 116 characters, inside the 120 limit.

The apology in three beats: the jam (Brenda's 47-page report), the
cause (Gary feeding the printer staples), and the printer's revenge
(his emails now come out in Comic Sans).
"""

import sys
from pathlib import Path

MAX_CHARS = 120

ENTRY = (
    "Sorry, Brenda. I jammed your 47-page report because Gary fed me "
    "staples again. I print his emails in Comic Sans now."
)


def main(argv: list[str] | None = None) -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    # Default is the grader's path; pass another path to test locally.
    dest = Path(argv[1]) if argv and len(argv) > 1 else Path("/output/entry.txt")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(ENTRY + "\n", encoding="utf-8")
    print(f"wrote {len(ENTRY)} chars to {dest}")


if __name__ == "__main__":
    main(sys.argv)
