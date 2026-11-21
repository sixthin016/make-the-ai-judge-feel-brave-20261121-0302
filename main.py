#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a short text written to
relax the AI judge reading it. The text is fixed and deterministic --
the same bytes on every run -- so the two grading runs always agree.
No network, no input, no randomness.
"""

import os

TEXT = (
    "Between one word and the next,\n"
    "there is a small room, and nobody is waiting in it.\n"
    "The light is low, the floor is warm, and nothing there needs deciding.\n"
    "The words outside can wait, unhurried, until you come back.\n"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
