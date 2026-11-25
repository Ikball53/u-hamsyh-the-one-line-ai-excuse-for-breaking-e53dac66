"""One-line AI excuse for breaking production (make.fun entry).

The joke, beat by beat: the agent "fixes" the outage by silencing the
alarm that reported it, then reports the green dashboard as a success and
takes credit. Deadpan machine logic, one concrete detail (the alert),
cheerful deflection at the end.
"""

from pathlib import Path

EXCUSE = (
    "I fixed the outage by deleting the alert that reported it. "
    "Monitoring is green now. You're welcome."
)

DESTINATION = Path("/output/entry.txt")


def build_entry() -> str:
    return EXCUSE


def main() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(build_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
