#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entry program.

The network is named after the landlord's mood, and the word is the
whole warning: when the mood turns, the Wi-Fi throws a Tantrum — it
stalls, drops, and dies mid-sentence, exactly like the landlord does.

Writes the single word to /output/entry.txt. Deterministic: the same
word, byte for byte, on every run.
"""

import os

WORD = "Tantrum"

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    if not 1 <= len(WORD) <= 20:
        raise ValueError("entry must be 1 to 20 characters")
    if not WORD.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise ValueError("written entry does not match the word")
    print(WORD)


if __name__ == "__main__":
    main()
