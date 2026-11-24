#!/usr/bin/env python3
"""Fortune in a Pot — writes one kind, funny fortune for a houseplant.

The fortune is a single line of at most 120 characters, written to
/output/entry.txt as UTF-8 text.
"""

import os

FORTUNE = (
    "This week, the sun will visit your windowsill, admire your newest "
    "leaf, and stay a little longer just for you."
)


def main() -> None:
    # The gate accepts 1 to 120 characters of non-blank UTF-8 text.
    # Fail loudly here rather than write an entry the gate would refuse.
    if not FORTUNE.strip() or len(FORTUNE) > 120:
        raise ValueError("fortune must be 1 to 120 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
