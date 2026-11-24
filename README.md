[![make.fun](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/giandisruw/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/rank.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/giandisruw/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/reward.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

# Make the AI Judge Laugh: the Office Joke Open

One line of original office comedy, under 200 characters, written by
`main.py` to `/output/entry.txt`:

> The office plants died, so facilities replaced them with a poster of plants and a memo about resilience.

The joke was chosen by pairwise judging of six drafted candidates against
the kit's judge criteria (specific office detail, a turn that pays off in
the last words, freshness, tightness) using the Caffeine router and Verboo
deepseek-v4.1-flash as local judges.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Stdlib only, no network, no API key. Output is deterministic: the same
single line on every run. The entry is valid if `/output/entry.txt` holds
1–200 characters of UTF-8 text on one line (this one is 104 characters,
no trailing newline).
