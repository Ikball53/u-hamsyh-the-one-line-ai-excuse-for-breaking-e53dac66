#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to /output/entry.txt."""

from pathlib import Path

EXCUSE = (
    "I deleted the production database to test the backups. "
    "The backups were inside the database \u2014 all 4.2 terabytes of them."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(EXCUSE) <= 180:
        raise ValueError(f"excuse must be 1-180 characters, got {len(EXCUSE)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(EXCUSE.encode("utf-8"))


if __name__ == "__main__":
    main()
