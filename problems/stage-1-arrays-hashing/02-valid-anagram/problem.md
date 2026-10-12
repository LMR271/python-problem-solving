# 1.2 · Valid Anagram

**Stage:** 1 · Arrays and hashing · **Difficulty:** Easy · **New concept:** comparing two frequency dicts

**Also on LeetCode:** [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

## Task

Write `is_anagram(s, t)` that returns `True` if `t` is an **anagram** of `s` (uses exactly the same letters, each the same number of times, just rearranged). Inputs are lowercase letters only.

## Examples

```python
is_anagram("listen", "silent")   # True
is_anagram("rat", "car")         # False
is_anagram("aab", "abb")         # False
```

## Before you code (on paper)

1. Check `"listen"` and `"silent"` by hand. What did you compare?
2. Why is checking "same set of letters" not enough? (Look at the third example.)
3. You already wrote a function in 0.7 that does half the work. How do you use it here?
4. Quick early exit: what if the lengths differ?

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

Two words are anagrams exactly when their letter counts are identical.

</details>

<details>
<summary>Hint 2 · the tool</summary>

Build a count dict for each word (like 0.7). Two dicts can be compared with `==`.

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
if lengths differ: return False
count letters of s into dict A
count letters of t into dict B
return A == B
```

</details>

## Stretch

Another approach is `sorted(s) == sorted(t)`. Which is faster in Big-O terms, and why?

## Run the tests

```bash
pytest problems/stage-1-arrays-hashing/02-valid-anagram -v
```
