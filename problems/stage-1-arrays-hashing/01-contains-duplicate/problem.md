# 1.1 · Contains Duplicate

**Stage:** 1 · Arrays and hashing · **Difficulty:** Easy · **New concept:** set for "have I seen this before?"

**Also on LeetCode:** [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

## Task

Write `contains_duplicate(nums)` that returns `True` if any number appears at least twice, and `False` if every number is unique.

## Examples

```python
contains_duplicate([1, 2, 3, 1])   # True
contains_duplicate([1, 2, 3, 4])   # False
contains_duplicate([])             # False
```

## Before you code (on paper)

1. **Brute force**: compare every number with every other number. How many comparisons is that for 4 numbers? For 1,000? What's the Big-O?
2. You solved something very close in 0.8. What did you remember while looping there?
3. When can you stop early and return `True`?

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

This is 0.8 again, but you can stop as soon as you find the first repeat.

</details>

<details>
<summary>Hint 2 · the tool</summary>

A `set` of numbers you've already seen. Checking `n in seen` is O(1).

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
seen = empty set
for each n in nums:
    if n in seen: return True
    add n to seen
return False
```

</details>

## Stretch

There's a one-line solution comparing two lengths. Find it, and explain in `notes.md` why it works.

## Run the tests

```bash
pytest problems/stage-1-arrays-hashing/01-contains-duplicate -v
```
