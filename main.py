#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry (program/v1).

Writes a single line to /output/entry.txt: the text message a smart
fridge sends its owner at 3am. Python standard library only.
"""

import os

# The entry line, written fresh for this competition.
ENTRY = "It's 3am. I know what you did with the last slice. The microwave knows too. We talk."

MAX_CHARS = 140


def main():
    # Gate checks: one line, not empty, within the 140-character cap.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert not ENTRY.isspace(), "entry must not be only whitespace"
    assert len(ENTRY) <= MAX_CHARS, (
        "entry is %d characters, over the %d cap" % (len(ENTRY), MAX_CHARS)
    )

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Verify the write round-tripped: read the file back and make sure
    # what landed on disk is exactly the line we intended to submit.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit(
            "verification failed: /output/entry.txt does not match the "
            "intended entry (%r written, %r expected)" % (written, ENTRY)
        )

    print("wrote %d characters to /output/entry.txt" % len(ENTRY))


if __name__ == "__main__":
    main()
