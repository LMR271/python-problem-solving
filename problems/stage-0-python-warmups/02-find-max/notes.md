# Notes · Find the Maximum

## Key idea (one line)
The sentence I'd say to recall the whole solution.

## Pattern trigger
"When I see ..., I think ..."

## Approach
How I solved it, in 2 to 4 sentences.

- checked if the number list is an empty list and if yes I would return None
- setting the max_so_far to the first element in the number list
- start with a for loop to iterate through the number list but starting at index 1 because we already have index 0 check through the initialization of max_so_far
- comparing in the loop the max_so_far with the current element and if needed update the max_so_far to the current element and then pursue with the loop
- at the end of the number list the loop break and the max_so_far is returned as teh maximum of the list


## Complexity
- Time: O(n) because the loop visits each of the n numbers exactly once, and each visit does constant work (one comparison, maybe one assignment)
- Space: O(1) because only two variables (max_so_far and j) are stored, regardless of list length

## Bug I made / what tripped me up


## Alternative I read afterwards


## Hints used
0
