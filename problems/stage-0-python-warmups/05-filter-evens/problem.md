# 0.5 · Filter Even Numbers

**Stage:** 0 · Python warm-ups · **Difficulty:** Warm-up · **New concept:** building a new list with `.append()` and the modulo operator `%` (the remainder after division)

## Task

Write `filter_evens(numbers)` that returns a **new** list containing only the even numbers, in the same order they appeared.

## Examples

```python
filter_evens([1, 2, 3, 4])    # [2, 4]
filter_evens([1, 3, 5])       # []
filter_evens([0, -2, 7])      # [0, -2]
```

## Before you code (on paper)

1. How do you know a number is even? Express it as "the remainder when dividing by 2 is ...".
2. Is `0` even? Is `-2`?
3. Where do the even numbers go while you loop?

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

Start with an empty list and add the numbers that pass the test.

</details>

<details>
<summary>Hint 2 · the tool</summary>

`n % 2 == 0` is `True` for even numbers. `my_list.append(x)` adds `x` to the end of a list.

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
evens = []
for each n in numbers:
    if n % 2 == 0:
        append n to evens
return evens
```

</details>

## Stretch

Rewrite it as a **list comprehension** (a one-line way to build a list): `[n for n in numbers if ...]`.

## Run the tests

```bash
pytest problems/stage-0-python-warmups/05-filter-evens -v
```
