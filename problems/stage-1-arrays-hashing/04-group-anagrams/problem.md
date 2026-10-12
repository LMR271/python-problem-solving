# 1.4 · Group Anagrams

**Stage:** 1 · Arrays and hashing · **Difficulty:** Medium · **New concept:** dict that maps a computed key to a list of items (grouping)

**Also on LeetCode:** [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

## Task

Write `group_anagrams(words)` that groups words which are anagrams of each other. Return a list of groups, where each group is a list of words.

The order of the groups, and of the words inside a group, **doesn't matter**. The tests accept any order.

## Examples

```python
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]   (any order)

group_anagrams([""])    # [[""]]
```

## Before you code (on paper)

1. Group the example by hand. How did you decide that `"eat"` and `"ate"` belong together?
2. Find something you can compute from a word that is **identical for all its anagrams**. Try a few ideas on `"eat"`, `"tea"` and `"ate"`.
3. Once you have that, it works like sorting mail into labeled boxes. What's the label, and what goes in the box?

## Hints

Only open a hint after about 15 minutes of real effort without progress. Note in `notes.md` how many you used.

<details>
<summary>Hint 1 · a nudge</summary>

All anagrams look the same once you put their letters in alphabetical order.

</details>

<details>
<summary>Hint 2 · the tool</summary>

Use the sorted letters as a dict **key**, and a list of words as the **value**. `"".join(sorted("tea"))` gives `"aet"`.

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

```
groups = {}                       # key -> list of words
for each word in words:
    key = the word's letters sorted, joined into a string
    if key not in groups: groups[key] = []
    append word to groups[key]
return list of all the values in groups
```

</details>

## Stretch

Look up `collections.defaultdict(list)` and use it to remove the `if key not in groups` line.

## Run the tests

```bash
pytest problems/stage-1-arrays-hashing/04-group-anagrams -v
```
