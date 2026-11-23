#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR):
    A  -> coffee
    B  -> tea

The choice: A, coffee. Coffee is the more vivid, funnier and truer answer.
It is the 6am lifeline, the steam, the jolt — a devotion people confess
out loud, jitter and all. Tea is a calm ritual; coffee is a need that
announces itself. When the judge reads one letter as a whole answer,
"A" lands as the fuller, more alive stance.

Stdlib only. No network, no file reads outside this program, no arguments.
The output is validated before it is written: exactly one character,
an ASCII letter, not whitespace.
"""

import os
import sys

# The verdict, decided at build time: A for coffee.
CHOSEN_LETTER = "A"

# The gate the sealed scorer enforces: 1 character, not whitespace-only.
ALLOWED_LETTERS = ("A", "B")


def output_path() -> str:
    """Resolve the output directory: $MAKEFUN_OUTPUT_DIR, else /output.

    Normalised to an absolute path so a relative MAKEFUN_OUTPUT_DIR can
    never silently land the entry somewhere the harness does not look.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_dir = os.path.abspath(out_dir)
    return os.path.join(out_dir, "entry.txt")


def validate(letter: str) -> str:
    """Enforce the competition gate on the letter before writing it."""
    if not isinstance(letter, str):
        raise ValueError("letter must be a string")
    if len(letter) != 1:
        raise ValueError(f"letter must be exactly 1 character, got {len(letter)}")
    if letter.isspace():
        raise ValueError("letter must not be whitespace")
    if letter not in ALLOWED_LETTERS:
        raise ValueError(f"letter must be one of {ALLOWED_LETTERS}, got {letter!r}")
    return letter


def verify_written(path: str, letter: str) -> None:
    """Re-read the file and confirm it holds exactly the chosen letter.

    Catches a partial write or an encoding surprise before the program
    exits successfully: the gate is 1 UTF-8 character, not whitespace.
    """
    with open(path, "rb") as f:
        raw = f.read()
    if raw != letter.encode("utf-8"):
        raise ValueError(
            f"written bytes {raw!r} do not match the chosen letter {letter!r}"
        )
    if len(raw.decode("utf-8")) != 1 or raw.decode("utf-8").isspace():
        raise ValueError("written content fails the 1-character gate")


def main() -> int:
    letter = validate(CHOSEN_LETTER)
    path = output_path()
    parent = os.path.dirname(path) or "."
    os.makedirs(parent, exist_ok=True)
    # Write exactly one byte, no trailing newline, no BOM.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(letter)
    verify_written(path, letter)
    return 0


if __name__ == "__main__":
    sys.exit(main())
