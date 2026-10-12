# 0.7 · Character Frequency

**Stage:** 0 · Python warm-ups · **Difficulty:** Warm-up · **New concept:** building a dict (a lookup table from keys to values) by counting

## Task

Write `char_frequency(text)` that returns a dict where each key is a character from the text and each value is how often it appears. Count every character exactly as it is, including spaces and capitals.

## Examples

```python
char_frequency("hello")   # {"h": 1, "e": 1, "l": 2, "o": 1}
char_frequency("aA")      # {"a": 1, "A": 1}
char_frequency("")        # {}
```

## Before you code (on paper)

1. Count the letters of `"banana"` on paper with a tally table. That table **is** a dict.
2. What do you do the first time you see a letter, versus the second time?
3. You've done this before, in 001. Which one-liner did you use?

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

Make an empty dict and update it once per character.

</details>

<details>
<summary>Hint 2 · the tool</summary>

`counts.get(char, 0)` returns the current count, or 0 if the character is new.

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
counts = {}
for each char in text:
    counts[char] = counts.get(char, 0) + 1
return counts
```

</details>

## Stretch

Look up `collections.Counter` and solve it in one line.

## Run the tests

```bash
pytest problems/stage-0-python-warmups/07-char-frequency -v
```
