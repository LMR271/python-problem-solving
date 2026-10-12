# 0.9 · Running Sum

**Stage:** 0 · Python warm-ups · **Difficulty:** Warm-up · **New concept:** Big-O in practice, the same answer in O(n²) and in O(n)

**Also on LeetCode:** [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)

## Task

Write `running_sum(nums)` that returns a new list where position `i` holds the sum of all numbers from position `0` up to and including `i`.

Solve it **twice**. First the simple way, then the fast way. Keep both versions in your file (name the slow one `running_sum_slow`) and compare them in `notes.md`.

## Examples

```python
running_sum([1, 2, 3, 4])   # [1, 3, 6, 10]
running_sum([5])            # [5]
running_sum([])             # []
```

## Before you code (on paper)

1. **Slow version**: for each position, add up everything from the start again. For a list of 4 numbers, how many additions is that in total? For 1,000 numbers? (Hint: 1 + 2 + 3 + ... + n is about n²/2.)
2. **Fast version**: look at the output `[1, 3, 6, 10]`. How do you get `10` from the number **just before it** in the output?
3. What's the Big-O of each version? Write both in `notes.md` with one sentence of why.

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

Each output value is the previous output value plus one new number.

</details>

<details>
<summary>Hint 2 · the tool</summary>

Keep one accumulator `total` (like 0.1), and append it to the result after every addition.

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
result = []
total = 0
for each n in nums:
    total = total + n
    append total to result
return result
```

</details>

## Stretch

Time both versions on a list of 10,000 numbers with `import time` and `time.perf_counter()`. Does the slow one take roughly 10,000 times longer, or less? Why?

## Run the tests

```bash
pytest problems/stage-0-python-warmups/09-running-sum -v
```
