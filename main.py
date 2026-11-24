#!/usr/bin/env python3
"""Write one one-line review of Monday to /output/entry.txt.

The review text lives in this file. The program reads no input, uses no
network and no randomness, so every run writes exactly the same bytes.
"""
import os

REVIEW = "Monday, one star: 200 unread emails, 199 of them asking if I saw the email. I saw it. I saw every single one."

OUTPUT_PATH = "/output/entry.txt"


def write_review():
    """Write REVIEW to OUTPUT_PATH atomically via a temp file."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp = OUTPUT_PATH + ".tmp"
    try:
        # Flush to disk before the rename so a crash cannot leave a partial file.
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(REVIEW)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp)
        except FileNotFoundError:
            pass
        raise


if __name__ == "__main__":
    write_review()
