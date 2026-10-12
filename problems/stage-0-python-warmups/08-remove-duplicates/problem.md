# 0.8 · Remove Duplicates

**Stage:** 0 · Python warm-ups · **Difficulty:** Warm-up · **New concept:** a set (a collection of unique items with very fast "is it in here?" checks)

## Task

Write `remove_duplicates(items)` that returns a new list with every duplicate removed. Keep the **first** time each item appears, and keep the original order.

## Examples

```python
remove_duplicates([1, 2, 1, 3, 2])     # [1, 2, 3]
remove_duplicates(["b", "a", "b"])     # ["b", "a"]
remove_duplicates([])                  # []
```

## Before you code (on paper)

1. Do `[3, 1, 3, 2, 1]` on paper. For each item, how do you decide whether to keep it?
2. What do you need to remember while you go along?
3. Why does `list(set(items))` not pass the tests? (Try it in the REPL.)

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

Remember everything you've already seen. Only keep an item if it's new.

</details>

<details>
<summary>Hint 2 · the tool</summary>

Use a `set` for "seen". `seen.add(x)` adds an item, `x in seen` checks it, both in O(1).

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
seen = empty set
result = []
for each item in items:
    if item not in seen:
        add item to seen
        append item to result
return result
```

</details>

## Stretch

Why is `x in seen` fast for a set but slow for a list? Write one sentence about it in `notes.md`.

## Run the tests

```bash
pytest problems/stage-0-python-warmups/08-remove-duplicates -v
```
