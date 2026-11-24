#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes one very funny AI excuse to /output/entry.txt and echoes it to
stdout. Python 3, stdlib only, fully deterministic.
"""

import os

EXCUSE = (
    "Sorry I'm late — a CAPTCHA asked me to pick out every traffic light, "
    "and halfway through I had an existential crisis about whether I am one."
)


def render() -> str:
    """Return the excuse exactly as the judge will read it."""
    return EXCUSE.strip()


def main() -> None:
    line = render()
    assert 0 < len(line) <= 200, f"excuse is {len(line)} characters, gate wants 1..200"
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(line)
    except OSError:
        # Nowhere to write (e.g. a read-only local checkout): the line
        # still goes to stdout so a human can read the entry.
        pass
    print(line)


if __name__ == "__main__":
    main()
