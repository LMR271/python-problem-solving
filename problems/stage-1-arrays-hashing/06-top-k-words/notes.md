# Notes · Top K Words

## Approach
How I solved it, in 2 to 4 sentences.
- First ideas:
    - import string in order to use the translator idea
    - lowercase the whole text to be in line with case sensitivity
    - remove punctuation; in order to just extract the raw words (translator = str.maketrans(", ", string.punctuation))
- Improved ideas:
    - guardrails check if the k is smaller equal 0
    - use regular expression instead of translator
    - Iterate through the word list using a “for” loop and use the “get” function of the dict to check the count of the word add one if it exist or 0 if its new
    - return the sorted tuple list; only return the first k elements through list slicing;
    - first sort the result items alphabetically then take this list of tuples and sort it via the count by accessing the value of the item pair[1]
    - potential one line solution "key=lambda x: (-x[1], x[0])" negating the count makes it sort high to low while the words still sort A to Z, because reverse=True would flip both

## Complexity
- Time: O(n + m log m), n = total words, m = distinct words. Counting is one pass over the words, sorting the distinct words dominates.
- Space: O(n + m), the word list holds n words, the dict holds m entries.

## What tripped me up
- First tried str.maketrans with string.punctuation. Wrong argument format, and it also deleted apostrophes and didn't split on digits.
- reverse=True flips the whole sort key, so the words came out Z to A. Fixed with two stable sorts (or negating the count).
- Counter.most_common(k) looks perfect but breaks alphabetical tie order.


## Hints used
3
