#!/usr/bin/env python3
"""Write one one-line review of Monday to /output/entry.txt.

The review is written here in full: the program takes no input, uses no
network and no randomness, so every run produces the same bytes.
"""
import os

REVIEW = "Monday, one star: 200 unread emails, 199 of them asking if I saw the email. I saw it. I saw every single one."

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tmp = OUTPUT_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(REVIEW)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, OUTPUT_PATH)


if __name__ == "__main__":
    main()
