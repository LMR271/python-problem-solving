# 0.3 · Count Vowels

**Stage:** 0 · Python warm-ups · **Difficulty:** Warm-up · **New concept:** looping over a string and the `in` operator (checks whether something is contained in a collection)

## Task

Write `count_vowels(text)` that returns how many vowels the text contains. Vowels are `a, e, i, o, u`, upper or lower case.

## Examples

```python
count_vowels("hello")       # 2
count_vowels("AEIOU")       # 5
count_vowels("rhythm")      # 0
```

## Before you code (on paper)

1. Count the vowels in `"Banana"` by hand. What did you do with each letter?
2. How do you check "is this letter a vowel" in Python, without writing five `==` comparisons?
3. How do you handle uppercase letters?

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

A `for` loop over a string gives you one character at a time.

</details>

<details>
<summary>Hint 2 · the tool</summary>

`"e" in "aeiou"` is `True`. Use `.lower()` so `"E"` counts too.

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
count = 0
for each char in text:
    if char (lowercased) is in "aeiou":
        count = count + 1
return count
```

</details>

## Run the tests

```bash
pytest problems/stage-0-python-warmups/03-count-vowels -v
```
