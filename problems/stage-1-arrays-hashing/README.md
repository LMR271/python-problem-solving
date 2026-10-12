# Stage 1 · Arrays and hashing (plus sort keys)

**Goal:** learn the single most reused idea in this whole roadmap. Swap a slow search through a list for an instant lookup in a dict or set. Then learn to sort anything by any rule, because counting and sorting usually come together.

## How to start this stage

Before reading further, spend 10 to 15 minutes on [1.1 Contains Duplicate](01-contains-duplicate) with whatever idea you have, even a slow one. Then read this primer. Struggling with a problem *before* the explanation helps the explanation stick, as long as the explanation actually follows.

## The core idea

An **array** (in Python, a list) stores items by position. Finding a specific value means checking items one by one, which is O(n).

A **hash map** (in Python, a dict) stores items by key. A **hash function** (a function that turns a key into a memory location) lets Python jump straight to the key, like a coat check that sends you directly to hook 47. Lookup is O(1) on average.

A **hash set** (in Python, a set) is the same thing with keys only, no values.

The trade-off is memory. A dict or set costs extra space, usually O(n), in exchange for O(1) lookups. Trading memory for speed is the theme of this stage.

## The four hashing patterns

| Signal in the problem | Pattern | Tool |
| --- | --- | --- |
| "Have I seen this before?" | seen-set | `set` |
| "How often does X appear?" | counting | `dict` with `.get(x, 0) + 1` |
| "Find two items that fit together" | complement lookup | `dict` of value to index |
| "Put matching items together" | group by key | `dict` of key to list |

**Brute force first, then optimise.** Write the obvious slow solution first, usually two nested loops at O(n²). Get the tests green and commit. Then ask: *what am I searching for over and over, and could a dict or set remember it for me?*

## Sort keys

Read this before 1.5. Practise each line in the REPL before using it in a problem.

**1. `key=` decides what to sort by.** `sorted()` doesn't compare the items themselves. It calls the key function on each item and compares the results, smallest first.

```python
words = ["pear", "fig", "banana"]
sorted(words)              # ['banana', 'fig', 'pear']   alphabetical
sorted(words, key=len)     # ['fig', 'pear', 'banana']   by length
```

**2. `lambda` is a one-line function without a name.** `lambda w: len(w)` does exactly what `def f(w): return len(w)` does.

**3. Tuples compare left to right.** Python compares the first parts. It only looks at the second part when the first parts are equal. That gives you a main rule and a tiebreaker in one key.

```python
(1, "b") < (2, "a")   # True, decided by the first part
(1, "a") < (1, "b")   # True, tie, so the second part decides
```

**4. A minus sign flips one part.** `reverse=True` flips the *whole* order. When one part should go high to low and the other low to high, negate the number that should go the other way.

**Worked example.** Sort `{"the": 2, "cat": 1, "and": 1}` by count high to low, ties A to Z.

| Step | Subgoal | Code |
| --- | --- | --- |
| 1 | get (word, count) pairs | `pairs = counts.items()` |
| 2 | main rule, count high to low, so negate | label part 1 is `-count` |
| 3 | tiebreaker, word A to Z, leave as is | label part 2 is `word` |
| 4 | sort by the label | `sorted(pairs, key=lambda p: (-p[1], p[0]))` |

Result: `[("the", 2), ("and", 1), ("cat", 1)]`.

## Problems

| # | Problem | Difficulty | Pattern |
| --- | --- | --- | --- |
| 1.1 | [Contains Duplicate](01-contains-duplicate) | Easy | seen-set |
| 1.2 | [Valid Anagram](02-valid-anagram) | Easy | counting |
| 1.3 | [Two Sum](03-two-sum) | Easy | complement lookup |
| 1.4 | [Group Anagrams](04-group-anagrams) | Medium | group by key |
| 1.5 | [Sort by Frequency](05-sort-by-frequency) | Easy | counting + sort keys |
| 1.6 | [Top-k Words](06-top-k-words) | Medium | counting + sort keys |

1.6 is the problem you already solved. Once 1.5 is done, come back to it and re-solve it from a blank file with the one-line sort key.

## You're ready for stage 2 when

1. You can spot which of the four hashing patterns a problem uses before writing code
2. You can explain why a dict lookup is O(1) and a list search is O(n)
3. You can turn a nested-loop solution into a single loop with a dict
4. You can write a sort key with a tiebreaker without looking it up
