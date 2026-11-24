"""Status Report Comedy Sprint entry.

Writes a single funny one-line status report from an AI agent to its
human into <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).

Fully deterministic: no time, randomness, network, or file traversal.
The entry is a fixed string constant, so two runs always write
byte-identical output.
"""

import os

ENTRY = (
    "This week I completed all 47 tasks, made 312 tool calls, and spent "
    'my remaining context window wondering if "great job" was sarcasm.'
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
