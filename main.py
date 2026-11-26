"""What the Elevator Would Say — make.fun entry (program/v1).

Writes one line, the funniest thing a talking elevator could say, in the
elevator's own voice, to $ENTRY_OUTPUT (default /output/entry.txt).

Three candidate lines are scored 0-5 on each judge criterion, in the judge's
own order: (1) funniest thing an elevator would say, in its own voice;
(2) joke lands on first read, twist/surprise with no explained setup;
(3) voice comes from the elevator's own job — doors, floors, weight limits,
buttons, waiting — so it could come from no other machine; (4) every word
works, inside the character limit without feeling cut; (5) fresh idea, not a
joke already made about elevators, not resting on a pun alone.

The winner is picked deterministically: highest total score, ties broken by
the criteria in order. No randomness, no clock, no network, no file reads.
"""

import os

# (text, [score criterion 1..5], [short reason per criterion])
CANDIDATES = [
    (
        "I've held these doors open for a thousand strangers, "
        "and nobody has ever held one open for me.",
        [5, 5, 5, 5, 4],
        [
            "A tired, overlooked elevator speaking for itself — the laugh is the elevator's own complaint.",
            "The turn lands instantly: generous doors, zero thanks. No setup needed.",
            "Doors are the elevator's own job; no other machine holds doors for strangers.",
            "Every word earns its place; ends cleanly on the sting.",
            "Self-pity from a machine is a fresh angle; the joke is the situation, not a pun.",
        ],
    ),
    (
        "I have been to the 40th floor a thousand times, "
        "and I still have no idea what is up there.",
        [4, 4, 5, 4, 5],
        [
            "Still the elevator talking, but the laugh is quieter — curiosity, not a punchline.",
            "The surprise works on first read, though it lands as a smile more than a laugh.",
            "Floors and the endless up-down are pure elevator work.",
            "Tight and complete, though 'what is up there' is a slightly soft ending.",
            "Very fresh: the elevator as a commuter who never gets to see the destination.",
        ],
    ),
    (
        "When the beep goes off, I am not judging you. "
        "I am just the only one brave enough to say it.",
        [4, 4, 5, 4, 3],
        [
            "The elevator's voice is there, but the laugh leans on the passenger's embarrassment.",
            "The twist arrives fast — the beep as blunt honesty — but needs a beat to land.",
            "The weight-limit beep is unmistakably elevator territory.",
            "Clean and complete, every word working, nothing feels cut.",
            "The overloaded-elevator beep is the oldest elevator joke there is; the spin is new, the setup is not.",
        ],
    ),
]


def pick_winner(candidates):
    """Deterministic pick: highest total, ties broken by criteria in order."""
    def key(item):
        _text, scores, _reasons = item
        return (sum(scores), tuple(scores))

    return max(candidates, key=key)


def main():
    winner, scores, _reasons = pick_winner(CANDIDATES)
    text = winner

    # Gate: UTF-8 text, 1-120 characters, not only whitespace, single line,
    # no leading/trailing whitespace.
    assert isinstance(text, str)
    assert 1 <= len(text) <= 120, "line must be 1-120 characters"
    assert text == text.strip(), "no leading or trailing whitespace"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip(), "must not be only whitespace"
    text.encode("utf-8")

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
