#!/usr/bin/env python3
"""Office joke entry for make.fun — Make the AI Judge Laugh: the Office Joke Open.

Writes one line of original office comedy (under 200 characters) to
/output/entry.txt. Stdlib only, no network, no API key, deterministic.

The line was picked by pairwise judging of six drafted candidates against
the kit's judge criteria (Caffeine router + Verboo deepseek-v4.1-flash):
dead plants -> poster of plants -> "memo about resilience" is the
freshest turn, specific (facilities, poster, memo), and the laugh pays off
in the last two words.
"""

JOKE = "The office plants died, so facilities replaced them with a poster of plants and a memo about resilience."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must be a single line"
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
