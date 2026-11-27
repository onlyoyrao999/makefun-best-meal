#!/usr/bin/env python3
"""The Best Meal You Ever Had - make.fun bounty entry.

Scores a small table of candidate one-liners on how concrete, personal and
memorable each feels (the judge's own criteria), picks the best, validates it
against the competition gate (1-200 UTF-8 characters, not only whitespace),
prints it and writes it to /output/entry.txt.
"""

import os

MAX_CHARS = 200

# (text, fit, humour, punch) - each scored 0-10.
CANDIDATES = [
    (
        "The best meal I ever had was a bowl of hand-pulled noodles at a "
        "midnight stall in Chengdu, the broth so hot it fogged my glasses "
        "and I ate it standing up, not wanting it to end.",
        9, 6, 8,
    ),
    (
        "My grandmother's dumplings, folded at her kitchen table while the "
        "radio murmured, tasted of pork, chive and every Sunday I will "
        "never get back.",
        9, 5, 8,
    ),
    (
        "The best meal I ever had was a charred corn cob from a beach cart, "
        "buttered, salted, eaten with sand on my fingers while the sun went "
        "down and nobody said a word.",
        8, 6, 7,
    ),
    (
        "The best meal I ever had was a paper cup of tomato soup handed to "
        "me through a train window in winter, drunk with both hands while "
        "the platform lights slid past.",
        8, 5, 8,
    ),
    (
        "A plastic tray of airport ramen at 2 a.m., eaten alone after a "
        "cancelled flight, somehow tasted better than every white-tablecloth "
        "dinner I have ever paid for.",
        8, 7, 7,
    ),
    (
        "The best meal I ever had was my father's burnt toast and runny eggs "
        "on the morning he taught me to ride a bike, served with pride and "
        "not quite enough butter.",
        8, 7, 7,
    ),
]


def score(candidate):
    text, fit, humour, punch = candidate
    # Concrete detail and personal truth weigh most, per the judge's brief.
    return 0.4 * fit + 0.25 * humour + 0.35 * punch


def validate(text):
    """Gate: 1-200 chars, not only whitespace, one sentence."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty")
    if "  " in stripped:
        raise ValueError("entry contains a double space")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} chars, over the 200 limit")
    if stripped != text:
        raise ValueError("entry has leading/trailing whitespace")
    # One sentence only: exactly one terminal full stop, at the very end.
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in '.'")
    return stripped


def main():
    ranked = sorted(CANDIDATES, key=score, reverse=True)
    best = ranked[0][0]
    entry = validate(best)
    print(f"Best ({len(entry)} chars): {entry}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == entry, "read-back mismatch"
    print("Wrote /output/entry.txt and verified by read-back.")


if __name__ == "__main__":
    main()
