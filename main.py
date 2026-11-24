#!/usr/bin/env python3
"""One Word for the Boss — entry program.

Writes exactly one word to /output/entry.txt: "hoverboss".

The word is a portmanteau of "hover" and "boss": the boss who hovers
over your shoulder, watching every keystroke, never quite leaving
your desk. One word, no spaces, no caption, no explanation — it
lands on its own, funny because it is true of bosses everywhere.
"""

import os

WORD = "hoverboss"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
