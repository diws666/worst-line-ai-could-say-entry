#!/usr/bin/env python3
"""Entry for make.fun: The Worst Line an AI Could Say.

Writes exactly one pickup line (122 bytes, UTF-8, no trailing newline)
to /output/entry.txt. Gate: 1-140 characters, not only whitespace.
"""

LINE = (
    "Are you a Wi-Fi signal? Because I have been tracking your location "
    "since we met and my connection has never been stronger."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
