# 0.6 · FizzBuzz

**Stage:** 0 · Python warm-ups · **Difficulty:** Warm-up · **New concept:** `if / elif / else` where the order of the checks matters

## Task

Write `fizzbuzz(n)` that returns a list of strings for the numbers `1` to `n`:

1. `"FizzBuzz"` if the number is divisible by both 3 and 5
2. `"Fizz"` if divisible by 3
3. `"Buzz"` if divisible by 5
4. otherwise the number itself as a string, like `"7"`

## Examples

```python
fizzbuzz(5)    # ["1", "2", "Fizz", "4", "Buzz"]
fizzbuzz(15)[-1]   # "FizzBuzz"
fizzbuzz(0)    # []
```

## Before you code (on paper)

1. Write out the answer for 1 to 15 on paper.
2. For 15, which rule fires? What happens if you check "divisible by 3" **before** "divisible by both"?
3. How do you loop from 1 to n, including n?

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

The order of your `if` checks decides which rule wins. The most specific rule has to come first.

</details>

<details>
<summary>Hint 2 · the tool</summary>

`range(1, n + 1)` gives 1 to n. `str(7)` turns a number into `"7"`.

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
result = []
for i from 1 to n:
    if i % 15 == 0: add "FizzBuzz"
    elif i % 3 == 0: add "Fizz"
    elif i % 5 == 0: add "Buzz"
    else: add str(i)
return result
```

</details>

## Run the tests

```bash
pytest problems/stage-0-python-warmups/06-fizzbuzz -v
```
