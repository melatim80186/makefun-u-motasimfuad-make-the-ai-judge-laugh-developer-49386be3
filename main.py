#!/usr/bin/env python3
"""make.fun entry: Make the AI Judge Laugh — Developer Excuses.

Writes one funny single-line developer excuse (<200 chars) to
/output/entry.txt. Deterministic, no network, no randomness.
"""

import os

ENTRY = "The bug only affects paying customers, so technically the free tier still has 100% uptime."

# Contest limit: under 200 characters.
assert len(ENTRY) < 200, f"entry is {len(ENTRY)} chars, must be under 200"


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
