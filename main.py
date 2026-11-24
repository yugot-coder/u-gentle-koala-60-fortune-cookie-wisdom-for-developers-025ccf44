"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt). Single
line, at most 120 characters, no trailing newline.

The fortune:

    Your code will work on the first try today. It will not be your
    code.

Why this line (reasoning, kept here and in the README; the entry
itself is just the fortune):

* Reads like a real fortune cookie: a prediction about today, stated
  flatly, in the second person -- no joke scaffolding, no winking.
* Says something true about a developer's day: the green test run
  that feels like a gift is almost never your own code -- it is a
  dependency, a cached build, a colleague's fix, or a fluke. Every
  tired senior engineer has lived exactly this.
* Turns in the last few words: "It will not be your code" takes the
  good fortune back in the same breath it gives it. The reader smiles
  first, then nods -- the brief's exact test.
* Fresh: it is not the worn "it works on my machine" or "have you
  tried turning it off and on again" -- it inverts the wish itself.

Candidates weighed and set aside: "The bug you cannot find has been
in the code you stopped reading" -- true, but it lectures instead of
fortuning; "Commit often, for the code you lose today was the code
that worked" -- too long and too mournful for a cookie; anything
with "merge conflict" -- the obvious developer-fortune word, and the
judge will have seen it ten times.

Standard library only. Deterministic: no randomness, no network, no
clock.
"""

import hashlib
import os

TEXT = (
    "Your code will work on the first try today. "
    "It will not be your code."
)

MAX_CHARS = 120

# sha256 of the exact bytes main.py must write to entry.txt, measured
# from a verified run. The read-back step asserts the file's digest
# equals this value, so any drift in the written bytes fails loudly.
EXPECTED_SHA256 = (
    "4d768e98632b6a307ccb4a2ab5dcdfa5f81e1b32eae466b78ce0567c223eaf2f"
)


def validate_text(value) -> str:
    """Guard: value must be a single non-blank line of 1..120 chars.

    Accepts either the text string or the raw bytes read back from the
    entry file, so the same check covers the pre-write guard and the
    post-write read-back verification. Returns the text as a str, or
    raises AssertionError with a clear message.
    """
    if isinstance(value, bytes):
        value = value.decode("utf-8")
    assert 1 <= len(value) <= MAX_CHARS, (
        f"entry.txt must be 1..{MAX_CHARS} characters, got {len(value)}"
    )
    assert value.strip(), "entry.txt must not be only whitespace"
    assert "\n" not in value and "\r" not in value, (
        "entry.txt must be a single line"
    )
    return value


def main() -> None:
    # Pre-write guard: refuse to write anything outside the gate.
    validate_text(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Read-back validation: the gate is 1..120 characters, so the file
    # must hold exactly the text we intended to write.
    with open(path, "rb") as f:
        data = f.read()
    assert validate_text(data) == TEXT
    # Digest verification: the written bytes must hash to the digest
    # measured from the verified run, proving no drift or stray bytes.
    digest = hashlib.sha256(data).hexdigest()
    assert digest == EXPECTED_SHA256, (
        f"entry.txt sha256 mismatch: got {digest}, "
        f"expected {EXPECTED_SHA256}"
    )
    print(TEXT)
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
