"""Robot Romance: one-line pickup line for an AI.

Writes a single original pickup line to /output/entry.txt.
Stdlib only, no network, deterministic.
"""

LINE = (
    "Are you my context window? "
    "Because the moment you arrived, "
    "everything before you just vanished."
)


def main() -> None:
    # Enforce the gate ourselves: 1-200 chars, one line, not blank.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE and LINE.strip()
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
