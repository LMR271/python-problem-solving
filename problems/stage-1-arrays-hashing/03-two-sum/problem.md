# 1.3 · Two Sum

**Stage:** 1 · Arrays and hashing · **Difficulty:** Easy · **New concept:** dict as a lookup for "the partner I need"

**Also on LeetCode:** [1. Two Sum](https://leetcode.com/problems/two-sum/)

## Task

Write `two_sum(nums, target)` that returns the **indices** (positions) of the two numbers that add up to `target`, as `[i, j]` with `i < j`.

There is always exactly one solution, and you can't use the same position twice.

## Examples

```python
two_sum([2, 7, 11, 15], 9)   # [0, 1]   because 2 + 7 = 9
two_sum([3, 2, 4], 6)        # [1, 2]   because 2 + 4 = 6
two_sum([3, 3], 6)           # [0, 1]
```

## Before you code (on paper)

1. **Brute force first**: try every pair with two nested loops. Write it, get the tests green, commit it. What's its Big-O?
2. Now the key question. You're at the number `7` and the target is `9`. Which number do you **need** to have seen before? This is called the **complement** (target minus current).
3. What should you store so that "have I seen my complement, and where?" is one O(1) lookup?

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

For each number, the partner you need is `target - number`.

</details>

<details>
<summary>Hint 2 · the tool</summary>

A dict that maps **number to index** for everything you've seen so far. Use `enumerate(nums)` to get index and number together.

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
seen = {}            # number -> index
for i, n in enumerate(nums):
    need = target - n
    if need in seen:
        return [seen[need], i]
    seen[n] = i
```

</details>

## Stretch

Why do you check for the complement **before** adding the current number to the dict? Think about `[3, 3]` with target `6`, and `[3, 5]` with target `6`.

## Run the tests

```bash
pytest problems/stage-1-arrays-hashing/03-two-sum -v
```
