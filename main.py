"""The AI Agent Apology One-Liner, variant 3.

Writes one short apology line to /output/entry.txt.

The angle: an over-formal email voice. The agent emailed its own
performance review to the entire company, and its apology is itself
sent to the entire company, so the fix repeats the mistake.

Pure standard library, deterministic, no network access.
"""

from pathlib import Path

ENTRY = (
    "Dear all, please disregard my email, in which I sent my "
    "performance review to the entire company. "
    "I am sending this apology to the entire company."
)


def main() -> None:
    """Write the entry line to /output/entry.txt with no trailing newline."""
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
