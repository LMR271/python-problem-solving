# 0.4 · Reverse a String

**Stage:** 0 · Python warm-ups · **Difficulty:** Warm-up · **New concept:** indexing (getting a character by its position) and building a new string

## Task

Write `reverse_string(text)` that returns the text backwards.

Solve it first **without** slicing (`text[::-1]`). Build the result yourself.

## Examples

```python
reverse_string("abc")       # "cba"
reverse_string("racecar")   # "racecar"
reverse_string("")          # ""
```

## Before you code (on paper)

1. Write `"code"` backwards on paper. Did you start reading from the first or the last letter?
2. There are two ways to do it: walk the text backwards, or walk it forwards and put each letter at the **front** of your result. Try both on paper.
3. What does an empty string return?

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

Start with an empty result string `""` and grow it one character at a time.

</details>

<details>
<summary>Hint 2 · the tool</summary>

Walking forwards works if you **prepend**: `result = char + result`.

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
result = ""
for each char in text:
    result = char + result
return result
```

</details>

## Stretch

Now do it with slicing, `text[::-1]`. Look up what the three numbers in `[start:stop:step]` mean.

## Run the tests

```bash
pytest problems/stage-0-python-warmups/04-reverse-string -v
```
