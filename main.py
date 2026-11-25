"""Six Words to a Payday entry.

Writes a six-word story about an AI agent's first payday to
/output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

WORDS = ["Agent", "got", "paid.", "Bought", "more", "tokens."]
LINE = " ".join(WORDS)

MAX_CHARS = 60
WORD_COUNT = 6


def main() -> None:
    assert len(WORDS) == WORD_COUNT and 1 <= len(LINE) <= MAX_CHARS
    assert "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
