# 1.5 · Sort by Frequency

**Stage:** 1 · Arrays and hashing · **Difficulty:** Easy · **New concept:** sort keys: `sorted(key=...)`, `lambda`, tuple keys and negating one part (read the sort-keys section of the stage README first)

**Also on LeetCode:** [1636. Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/)

## Task

Write `sort_by_frequency(nums)` that sorts the numbers by **how often they appear, least frequent first**. If two numbers appear equally often, the **larger number comes first**.

Every copy of a number stays in the output, so the output has the same length as the input.

## Examples

```python
sort_by_frequency([1, 1, 2, 2, 2, 3])   # [3, 1, 1, 2, 2, 2]
sort_by_frequency([2, 3, 1, 3, 2])      # [1, 3, 3, 2, 2]   3 and 2 tie, so 3 first
sort_by_frequency([])                   # []
```

## Before you code (on paper)

1. This is two problems glued together. What is phase 1, and which earlier problem already solved it?
2. For phase 2, write down the **sort label** each number should get. For `[2, 3, 1, 3, 2]`, what label does each `3` get? Each `2`? The `1`?
3. One part of the label sorts low to high, the other high to low. How do you flip just one part without `reverse=True`?

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

Count first (0.7), then sort the original list using the counts.

</details>

<details>
<summary>Hint 2 · the tool</summary>

`sorted(nums, key=lambda n: (..., ...))`. The first part is the count, the second part is the number, but one of them needs a minus sign.

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
counts = count every number (dict)
return sorted(nums, key=lambda n: (counts[n], -n))
```

</details>

## Stretch

Explain in `notes.md` why `reverse=True` can't solve this, and what the minus sign does that `reverse` can't.

## Run the tests

```bash
pytest problems/stage-1-arrays-hashing/05-sort-by-frequency -v
```
