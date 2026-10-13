# Notes · Count Vowels

## Key idea (one line)
The sentence I'd say to recall the whole solution.

## Pattern trigger
"When I see ..., I think ..."

## Approach
How I solved it, in 2 to 4 sentences.

- first we need to have a counting variables which is initialized with a zero (vowel_count) -> this is counting the total numbers of vowels in a given text
- then we define a list including all the vowel = ["a", "e", "i", "o", "u"] in order to later check if the char is in the list of vowels (with the "in" keyword)
- afterwords we lowercase the sentence/text/string to handel case sensitivity and so capture all the vowels
- then we use a for loop to go through the individual characters and check for each char in it is included in the vowel list and if yes we will increment the vowel_count by one.
- After looping through the whole string we return the vowel_count

## Complexity
- Time: O(n) because the bottleneck would be the length of the text/string which is n therefore the longer the text/string to longer the function runs
- Space: O(n) because basic comparison operations and variable declarations but the new string creation with text.lower() creates a new string of length n; one could improve this by doing it one the fly in the if statement "if char.lower() in vowel:" to have a space complexity of O(1)

## Bug I made / what tripped me up


## Alternative I read afterwards


## Hints used
0 / 1 / 2 / 3
