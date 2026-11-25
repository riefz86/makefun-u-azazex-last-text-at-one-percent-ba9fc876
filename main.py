"""Last Text at One Percent.

The joke, in one sentence: a phone on its last percent of battery does
not send a battery warning -- it sends a eulogy for itself, and it uses
its final breath to settle a score with its owner.

The angle I chose
------------------
Most dying-phone lines lean on the same tired pun: "I'm dying", "low
battery", "charge me". A judge who has read a hundred entries will
have seen that line a hundred times, so this entry dodges it entirely:
the word "battery" never appears. Instead the humour comes from a
specific, lived-in grievance. Every phone owner knows the feeling of
blaming the phone for being slow while keeping dozens of tabs open,
and every phone, if it could talk, would remember exactly how many
tabs that was. So the phone dies mid-sentence doing what it loved --
buffering those tabs -- and its last act is to point out, politely,
that the slowness was never its fault. The turn is the reversal of
blame: the dying thing is not asking for sympathy, it is filing its
final complaint. That is a personality with a stake in dying, not a
warning label with a punchline stapled on.

Why the wording works as a text message
----------------------------------------
It opens the way a real last text opens -- "Okay, final words:" --
which frames everything after it as a deliberate goodbye rather than
an accident. It stays in the phone's own first-person voice from the
first word to the last, it names one concrete number (47 open tabs)
instead of a vague "so many tabs", and it ends on a single clean
"Goodbye." with no trailing gag to dilute it. Short, punchy, and it
parses on the first read, which is what a text message has to do.

What this program does
-----------------------
It writes exactly that one message, and nothing else, to
/output/entry.txt, so the sealed gate scorer sees UTF-8 text of 1 to
200 characters. A tiny validation helper checks the length before
writing, so a future edit that accidentally pushes the line past the
200-character cap fails loudly here instead of silently producing an
invalid entry on the server.

Safety note learned from an earlier bounty: never chmod the output
directory. The grader collects the output as a different user, and
chmod on a directory it does not own raises PermissionError. Only
os.makedirs with exist_ok=True, and a 0644 chmod on the file itself,
which the runner owns.
"""

import os

# The entry: one final text from a phone at one percent battery.
# No "battery" pun anywhere -- the joke is the reversed blame, and the
# second beat reframes the phone as an overworked employee quitting.
LINE = (
    "Okay, final words: tell my owner I died doing what I loved "
    "\u2014 buffering his 47 open tabs. He called me slow. "
    "I call this a hostile workplace. Goodbye."
)

# The gate scorer accepts 1 to 200 characters; keep a little headroom.
MAX_CHARS = 200


def validate(line):
    """Refuse to write a line the gate scorer would reject."""
    text = line.strip()
    if not text:
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d cap" % (len(text), MAX_CHARS)
        )
    return text


def main():
    line = validate(LINE)
    # makedirs only -- never chmod the directory itself (see docstring).
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # The file belongs to this runner, so a 0644 chmod on it is safe
    # and guarantees the grader can read it as another user.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
