"""The GPS Swears It Was a Shortcut -- make.fun entry.

Writes the GPS's own excuse for sending the driver down the wrong road
to /output/entry.txt. Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "The map said the lake had a bridge, and the map has never once "
    "admitted it was wrong, so don't look at me."
)


def validate(text: str) -> str:
    """Strip and check the entry line against the gate (1-200 chars)."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "entry must be at most 200 characters, got %d" % len(cleaned)
        )
    return cleaned


def main() -> None:
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
