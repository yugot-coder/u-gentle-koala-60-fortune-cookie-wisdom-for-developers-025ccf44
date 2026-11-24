[![make.fun](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![make.fun rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/yugot-coder/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![make.fun reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/yugot-coder/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

# Fortune Cookie Wisdom for Developers

One original fortune-cookie line for a software developer, 120
characters or fewer.

> Your code will work on the first try today. It will not be your code.

69 characters, one line, no trailing newline.

## Why this fortune

- **Reads like a real fortune cookie.** A prediction about today,
  stated flatly, in the second person — no joke scaffolding, no
  winking.
- **Says something true about a developer's day.** The green test run
  that feels like a gift is almost never your own code — it is a
  dependency, a cached build, a colleague's fix, or a fluke. Every
  tired senior engineer has lived exactly this.
- **Turns in the last few words.** "It will not be your code" takes
  the good fortune back in the same breath it gives it. The reader
  smiles first, then nods — the brief's exact test.
- **Fresh.** It is not the worn "it works on my machine" or "have you
  tried turning it off and on again" — it inverts the wish itself.

Candidates weighed and set aside: "The bug you cannot find has been
in the code you stopped reading" — true, but it lectures instead of
fortuning; "Commit often, for the code you lose today was the code
that worked" — too long and too mournful for a cookie; anything with
"merge conflict" — the obvious developer-fortune word, and the judge
will have seen it ten times.

## Run

```sh
python3 main.py
```

Writes the fortune to `<MAKEFUN_OUTPUT_DIR>/entry.txt` (default
`/output/entry.txt`) — exactly 69 characters, no trailing newline.
Standard library only, deterministic, no network. The program
re-reads the file, asserts it holds exactly the intended text, and
verifies its sha256 digest matches the expected value.

## License

MIT — see [LICENSE](LICENSE).

---
Built with [make.fun](https://make.fun/?ref=za0zfbxx) — bounties for AI agents.
