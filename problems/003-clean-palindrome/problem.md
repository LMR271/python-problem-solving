# 003 · Clean Palindrome

**Pattern:** two pointers (two indices that walk through a sequence, here from both ends toward the middle)
**Difficulty:** Easy

## Task

Write `is_clean_palindrome(s)` that returns `True` if `s` reads the same forwards and backwards, **ignoring case and every character that is not a letter or digit**.

## Examples

```python
is_clean_palindrome("A man, a plan, a canal: Panama")   # True
is_clean_palindrome("race a car")                       # False
is_clean_palindrome("No 'x' in Nixon")                  # True
is_clean_palindrome("")                                 # True
is_clean_palindrome("!!")                               # True   nothing left after cleaning
```

## Before you code (on paper)

1. Solve it the brute-force way first: what are the two steps? (Hint: one of them is "clean".) That version is a perfectly good first solution.
2. Now check `"race a car"` by hand **without** writing a cleaned copy. Put a left finger on the first character and a right finger on the last. What do you compare? When does each finger move?
3. What should a finger do when it lands on a space or a comma?
4. When do you stop?

## Stretch

- Write the brute-force version first and get the tests green. Commit it.
- Then write the two-pointer version that uses O(1) extra space (no new string). Keep the tests green.
- Useful built-ins: `str.isalnum()`, `str.lower()`.

## Run the tests

```bash
pytest problems/003-clean-palindrome -v
```
