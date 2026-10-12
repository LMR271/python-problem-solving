# 0.2 · Find the Maximum

**Stage:** 0 · Python warm-ups · **Difficulty:** Warm-up · **New concept:** tracking the best value so far

## Task

Write `find_max(numbers)` that returns the largest number in the list. If the list is empty, return `None`.

Don't use the built-in `max()`.

## Examples

```python
find_max([3, 7, 2])      # 7
find_max([-5, -1, -9])   # -1
find_max([])             # None
```

## Before you code (on paper)

1. Find the biggest number in `[3, 7, 2, 9, 4]` by pointing at one number at a time. What did you remember while moving along?
2. What should that "best so far" start as? Why is starting at `0` a bug? (Look at the negative example.)
3. Where in your code do you handle the empty list?

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

Remember the biggest number you've seen so far, and compare each new number against it.

</details>

<details>
<summary>Hint 2 · the tool</summary>

Start "best so far" with the **first** item of the list, `numbers[0]`, not with 0. Check for the empty list before that, with `if not numbers:`.

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
if numbers is empty: return None
best = first number
for each number in numbers:
    if number > best:
        best = number
return best
```

</details>

## Stretch

Write `find_min` the same way in your head. What changes?

## Run the tests

```bash
pytest problems/stage-0-python-warmups/02-find-max -v
```
