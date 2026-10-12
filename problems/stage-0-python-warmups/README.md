# Stage 0 · Python warm-ups and Big-O

**Goal:** get fluent with the Python tools every later problem uses, and learn to say how fast your code is. No algorithms yet.

**Time per problem:** 5 to 20 minutes. Every `notes.md` asks for Big-O with a one-line reason, even here where it's almost always O(n). That habit is the real point of this stage.

## 1. The toolbox

### Loops

A **for loop** (repeats code once for every item in a collection) is the most important tool you have.

```python
for n in [4, 1, 3]:      # n is 4, then 1, then 3
    print(n)

for char in "hi":        # strings loop character by character
    print(char)

for i in range(3):       # range gives 0, 1, 2
    print(i)

for i, n in enumerate([4, 1, 3]):   # enumerate gives (position, item)
    print(i, n)          # 0 4, then 1 1, then 2 3
```

### The accumulator pattern

An **accumulator** (a variable that collects a running result while you loop) solves a huge number of problems. Start it at a neutral value, update it once per item, return it at the end.

```python
total = 0                # neutral start for adding
for n in [4, 1, 3]:
    total = total + n    # update once per item
# total is now 8
```

The same shape works for counting (`count = 0`), building a list (`result = []`), building a string (`result = ""`) and tracking the best value so far.

### Strings, lists, dicts, sets

```python
word = "code"
word[0], word[-1], len(word)     # "c", "e", 4
word.lower()                     # returns a NEW string, word is unchanged

nums = [4, 1, 3]
nums.append(7)                   # [4, 1, 3, 7], changes the list in place
nums[1:3]                        # [1, 3]  slice from 1 up to (not including) 3

ages = {"anna": 25}              # dict (a lookup table from keys to values)
ages["ben"] = 31
ages.get("carl", 0)              # 0, the default when the key is missing

seen = set()                     # set (unique items, no order, fast "in")
seen.add(3); seen.add(3)         # duplicates ignored
3 in seen                        # True
```

## 2. Names and objects (aliasing)

In Python a variable is a **name** (a label) that points to an **object**. Assigning one name to another doesn't copy anything. Both labels now point to the same object. This is called **aliasing** (two names for one object).

```python
a = [1, 2]
b = a            # b is a second label on the SAME list
b.append(3)
print(a)         # [1, 2, 3]   a changed too

c = a.copy()     # a real copy, a separate list
```

The classic trap, which comes back with grids in later stages:

```python
grid = [[0] * 3] * 3    # three labels on ONE inner list
grid[0][0] = 9
print(grid)             # [[9, 0, 0], [9, 0, 0], [9, 0, 0]]  surprise
grid = [[0] * 3 for _ in range(3)]   # three separate lists, correct
```

**Tool:** paste any snippet into [Python Tutor](https://pythontutor.com/python-compiler.html#mode=edit). It draws the labels and arrows step by step. Use it whenever code does something you didn't expect.

## 3. Big-O

**Big-O notation** (how much more work the code does as the input grows) is how you compare solutions without a stopwatch. Ignore constants. Ask only: if the input doubles, what happens to the work?

| Notation | Name | Input doubles, work... | Typical code |
| --- | --- | --- | --- |
| O(1) | constant | stays the same | `my_dict[key]`, `x in my_set` |
| O(log n) | logarithmic | grows by one step | halving the input each step (binary search, stage 5) |
| O(n) | linear | doubles | one loop over the input |
| O(n log n) | linearithmic | a bit more than doubles | `sorted(items)` |
| O(n²) | quadratic | quadruples | a loop inside a loop over the same input |

The two pieces of maths you need, nothing more:

1. **Arithmetic series** (adding 1 + 2 + 3 + ... + n). The result is about n²/2, so it's O(n²). That's why "for each item, look at everything before it" is quadratic. Problem 0.9 shows it
2. **Logarithm as halving** (log₂ n is how many times you can halve n until you reach 1). log₂ 1,000 ≈ 10 and log₂ 1,000,000 ≈ 20. That's why halving algorithms are so fast

## 4. What Python's built-ins cost

These are the costs that most often hide inside one innocent-looking line.

| Operation | Cost | Why |
| --- | --- | --- |
| `lst.append(x)`, `lst.pop()` | O(1) | works at the end of the list |
| `lst[i]`, `lst[i] = x` | O(1) | jumps straight to position i |
| `x in lst`, `lst.index(x)` | **O(n)** | checks items one by one |
| `lst.pop(0)`, `lst.insert(0, x)` | **O(n)** | shifts every other item |
| `lst[a:b]`, `lst.copy()` | O(k) | creates a new list of k items |
| `x in s`, `s.add(x)` for a set | O(1) on average | hashing |
| `d[k]`, `d[k] = v`, `k in d` for a dict | O(1) on average | hashing |
| `sorted(lst)`, `lst.sort()` | O(n log n) | |
| `text += "x"` inside a loop | can be **O(n²)** overall | strings can't change, so each `+=` may build a new string |

Source: [Python wiki, TimeComplexity](https://wiki.python.org/moin/TimeComplexity).

## Problems

| # | Problem | New concept | Done |
| --- | --- | --- | --- |
| 0.1 | [Sum a List](01-sum-list) | for loop + accumulator | ✅ |
| 0.2 | [Find the Maximum](02-find-max) | tracking the best so far | ⬜ |
| 0.3 | [Count Vowels](03-count-vowels) | looping over strings, `in` | ⬜ |
| 0.4 | [Reverse a String](04-reverse-string) | building a string | ⬜ |
| 0.5 | [Filter Even Numbers](05-filter-evens) | building a list, `%` | ⬜ |
| 0.6 | [FizzBuzz](06-fizzbuzz) | `if / elif / else` order | ⬜ |
| 0.7 | [Character Frequency](07-char-frequency) | building a dict | ⬜ |
| 0.8 | [Remove Duplicates](08-remove-duplicates) | sets | ⬜ |
| 0.9 | [Running Sum](09-running-sum) | O(n²) vs O(n) for the same answer | ⬜ |

## You're ready for stage 1 when

1. You can write a loop with an accumulator without looking anything up
2. You can predict what `b = a; b.append(1)` does to `a`
3. You can give the Big-O of any single or nested loop and say why
4. You know which column of the cost table `x in my_list` and `x in my_set` fall into
