"""Five Seconds to Explain the Glass -- a house cat's excuse.

The entry program writes exactly one sentence -- the excuse a house cat
gives in the five seconds after sweeping a glass off the table -- to
/output/entry.txt, and prints it to stdout.

The line is built from three parts so the joke's shape stays visible in
the code: the reframed blame, the grievance, and the punch verb. The
output is fully deterministic: no randomness, no clock, no network, no
model call. The sealed gate only needs UTF-8 text of 1 to 200 characters,
and the line below is 99 characters.
"""

import os
import sys

# --- The excuse, in parts -----------------------------------------------
# The cat's case, in its own voice: the glass was the aggressor, the fern
# is the wronged party, and the cat merely enforced the eviction.
SETUP = "The glass owed the fern an apology, not me"
GRIEVANCE = "it was hogging the windowsill"
PUNCH = "I simply evicted it"

MIN_CHARS = 1
MAX_CHARS = 200
DEFAULT_OUTPUT = "/output/entry.txt"


def build_line() -> str:
    """Assemble the single-sentence excuse from its three parts."""
    # One sentence: blame reframed, grievance stated, punch verb last.
    return f"{SETUP} — {GRIEVANCE} and {PUNCH}."


def measure_line(line: str) -> int:
    """Return the character count, raising if the line breaks the cap."""
    count = len(line)
    if count < MIN_CHARS or count > MAX_CHARS:
        raise ValueError(
            f"excuse must be {MIN_CHARS}-{MAX_CHARS} characters, got {count}"
        )
    if not line.strip():
        raise ValueError("excuse must not be only whitespace")
    return count


def write_entry(line: str, path: str) -> None:
    """Write the excuse as UTF-8 text to path, creating parents as needed.

    The file holds exactly the line, with no trailing newline, so the
    character count the gate sees is the count of the sentence itself.
    """
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


def main() -> int:
    """Build the excuse, check it, write it, and print it."""
    line = build_line()
    measure_line(line)
    output_path = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    write_entry(line, output_path)
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
