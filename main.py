"""Write one short office joke for make.fun's bounty u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.

Usage:
    python3 main.py

The text is written verbatim (no trailing newline) to entry.txt inside the
directory named by MAKEFUN_OUTPUT_DIR, or /output when that variable is unset.
"""

import os
import pathlib
import sys

TEXT = "I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was."

assert 1 <= len(TEXT) <= 280, f"entry text must be 1..280 characters, got {len(TEXT)}"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    target = pathlib.Path(out_dir)
    target.mkdir(parents=True, exist_ok=True)
    dest = target / "entry.txt"
    dest.write_bytes(TEXT.encode("utf-8"))
    sys.stderr.write(f"{len(TEXT)}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
