"""Entry program for the 'How Many Tabs Do You Have Open?' make.fun bounty.

The entry is a single number, digits only: the honest count of open browser
tabs on the machine that built this entry. The program writes exactly those
digits to /output/entry.txt (an optional first argument overrides the
destination for a dry run).
"""

import sys
from pathlib import Path

COUNT = "137"
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(COUNT) <= 5, f"entry must be 1-5 characters, got {len(COUNT)}"
    assert COUNT.isdigit(), "entry must be digits only"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(COUNT + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == COUNT + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(COUNT)} chars)")


if __name__ == "__main__":
    main(sys.argv)
