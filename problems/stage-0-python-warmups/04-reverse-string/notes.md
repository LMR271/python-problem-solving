# Notes · Reverse a String

## Key idea (one line)
The sentence I'd say to recall the whole solution.

## Pattern trigger
"When I see ..., I think ..."

## Approach
How I solved it, in 2 to 4 sentences.

- First, an empty string named “result” is defined, which is used to append the individual characters in reverse order.
- The function checks whether the input string is empty; if so, it returns an empty string.
- Otherwise, the “for” loop iterates through the string and appends each character to “result,” but in reverse order, so that each current character is appended to the beginning of the result that has already been processed.
- Afterward, the loop terminates and “result” is returned.
- A possible alternative solution would be to use the slicing technique to start at the end of the string and then work backward toward the beginning of the string in increments of 1.


## Complexity
- Time Complexity: O(n^2), where n is the length of the string. Because strings are immutable in Python, each string concatenation (i + result) creates a new string in memory by copying all existing characters, leading to quadratic time overall.

- Space Complexity: O(n), as storing the final reversed string requires memory directly proportional to the length of the input

## Bug I made / what tripped me up


## Alternative I read afterwards


## Hints used
0 / 1 / 2 / 3
