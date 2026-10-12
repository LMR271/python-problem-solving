# 0.1 · Sum a List

**Stage:** 0 · Python warm-ups · **Difficulty:** Warm-up · **New concept:** for loop with an accumulator (a variable that collects a running result)

## Task

Write `sum_list(numbers)` that returns the sum of all numbers in the list.

Don't use the built-in `sum()`. The point is to build it yourself with a loop.

## Examples

```python
sum_list([1, 2, 3])     # 6
sum_list([5, -2])       # 3
sum_list([])            # 0
```

## Before you code (on paper)

1. Add up `[4, 1, 3]` in your head, slowly. What number did you keep in your head between steps?
2. What should that number start at, before you've seen any item?
3. What should an empty list return?

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

You need one variable that remembers "the total so far".

</details>

<details>
<summary>Hint 2 · the tool</summary>

Create `total = 0` before a `for` loop, then update it inside the loop.

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
total = 0
for each number in numbers:
    total = total + number
return total
```

</details>

## Stretch

Once it passes, compare with `sum(numbers)`. Same result, one line.

## Run the tests

```bash
pytest problems/stage-0-python-warmups/01-sum-list -v
```
