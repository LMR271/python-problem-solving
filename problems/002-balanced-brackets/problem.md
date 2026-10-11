# 002 · Balanced Brackets

**Pattern:** stack (a list where you only add and remove at the end, last in, first out)
**Difficulty:** Easy

## Task

Write `is_balanced(s)` that returns `True` if every bracket in `s` is closed by the matching bracket type, in the correct order. Otherwise return `False`.

Rules:

1. Bracket pairs are `()`, `[]` and `{}`.
2. All other characters are ignored.
3. An empty string (or one without brackets) is balanced.

## Examples

```python
is_balanced("(a[b]{c})")   # True
is_balanced("([)]")        # False   right types, wrong order
is_balanced("((")          # False   never closed
is_balanced("())")         # False   closed something that was never opened
is_balanced("")            # True
```

## Before you code (on paper)

1. Check `"{[()]}"` by hand, reading left to right. When you see a closing bracket, which opening bracket does it need to match?
2. Is it always the *most recent* unmatched opening bracket? Why?
3. Now do `"([)]"`. At which character exactly do you know it's broken?
4. There are three different ways a string can be unbalanced (see the examples). Where in your algorithm does each one get caught?

## Stretch

- Use a `dict` to map closing to opening brackets so you have no long `if/elif` chain.
- What is the time and space complexity? What input makes the stack as large as possible?

## Run the tests

```bash
pytest problems/002-balanced-brackets -v
```
