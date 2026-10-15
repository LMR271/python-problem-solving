# Notes · Filter Even Numbers

## Key idea (one line)
The sentence I'd say to recall the whole solution.

## Pattern trigger
"When I see ..., I think ..."

## Approach
How I solved it, in 2 to 4 sentences.

- First, I defined an empty list named “result,” to which the events will be appended later.
- Then, using an if statement at the beginning of the function, I set up a check to determine whether the passed list is empty or not.
- If the list is not empty, we iterate through the list of numbers and check for each element whether it is divisible by 2 and yields an even result—in this specific case, we use the modulo operator to check whether the number % 2 equals zero, meaning it is an even number.
- If this is true for a given number, we add it to the “result” list.

## Complexity
- Time: O(n) because the loop visits each of the n numbers once, and each visit does constant work (one modulo check, and at most one append, which is O(1) for a list)
- Space: O(n) because in the worst case every number is even, so the result list grows to n items

## Bug I made / what tripped me up


## Alternative I read afterwards


## Hints used
0 / 1 / 2 / 3
