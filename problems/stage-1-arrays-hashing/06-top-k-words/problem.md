# 1.6 · Top-k Words

**Pattern:** hash map (a `dict` that maps each key to a value, with O(1) lookup)
**Difficulty:** Easy

## Task

Write `top_k_words(text, k)` that returns the `k` most frequent words in `text` as a list of `(word, count)` tuples, most frequent first.

Rules:

1. Words are case-insensitive. `"The"` and `"the"` are the same word.
2. A word is a run of letters `a-z` and apostrophes. Everything else (spaces, digits, punctuation) separates words. So `"don't"` is one word and `"end."` is `"end"`.
3. Ties in count are broken **alphabetically** (`"apple"` before `"banana"`).
4. If there are fewer than `k` distinct words, return all of them.
5. If `k <= 0` or the text has no words, return `[]`.

## Examples

```python
top_k_words("the cat and the hat", 2)
# [("the", 2), ("and", 1)]      "and", "cat", "hat" tie at 1, "and" wins alphabetically

top_k_words("Go go GO! Stop.", 5)
# [("go", 3), ("stop", 1)]      fewer than 5 distinct words, so return all

top_k_words("", 3)
# []
```

## Before you code (on paper)

1. Restate the task in one sentence.
2. Solve `"b a b c a b"` with `k = 2` by hand. What did you do first? What did you keep track of?
3. Your steps probably split into two phases. What are they?
4. How do you sort by "count high to low, then word A to Z" at the same time?
5. Which edge cases from the rules above could break a first attempt?

## Stretch

- Solve it once with a plain `dict`, then once with `collections.Counter`. Which reads better?
- Sorting all distinct words costs O(m log m) for m distinct words. Look up `heapq.nsmallest` and think about when it would be faster.

## Run the tests

```bash
pytest problems/stage-1-arrays-hashing/06-top-k-words -v
```
