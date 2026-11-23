"""Entry for make.fun bounty u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.

Writes a single one-line joke about office life to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).

The joke was chosen against the judge's five criteria, in order:
1. a genuine one-line joke about office life (expensing, finance approval);
2. a real turn at the end ("my breakdown counts as collaboration");
3. recognition -- the wince of burnout treated as a line item;
4. tight wording, every word earning its place;
5. freshness -- not the obvious Monday-morning or photocopier line.

Deterministic: Python 3.13 standard library only, no network, no
randomness, no timestamps. The output is byte-identical on every run.
"""

import os
import sys

JOKE = (
    "I expensed my therapy as 'team building' and finance approved it "
    "\u2014 apparently my breakdown counts as collaboration."
)

# The gate requires 1 to 199 characters. Fail loudly rather than
# ever writing an entry the sealed scorer would refuse.
if not 1 <= len(JOKE) <= 199:
    raise ValueError(f"joke is {len(JOKE)} characters, must be 1-199")


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
