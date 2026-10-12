# Roadmap

A prerequisite-ordered path from Python basics to the standard interview patterns. Every stage only uses ideas from earlier stages, so the knowledge builds as a network instead of a pile of unrelated tricks.

## Why this order

University courses (MIT 6.006, Stanford CS106B, Berkeley CS61B, Princeton COS 226) and interview roadmaps (NeetCode, Tech Interview Handbook) agree on the big picture. Linear structures come first, then recursion, then trees, then graphs, and dynamic programming last.

They disagree on the foundations. Universities teach Big-O, the memory model and recursion explicitly. Interview roadmaps assume them, which is exactly where the first attempt at this repo broke down. This roadmap keeps the interview-pattern order but adds the university foundations at the point where each one is first needed.

## The dependency chain

| Stage | Topic | Builds on | Unlocks |
| --- | --- | --- | --- |
| 0 | Python warm-ups and Big-O | Python basics | everything (every notes.md asks for Big-O) |
| 1 | Arrays and hashing, sort keys | 0: cost of lists vs dicts | sliding window, graphs, DP memo tables |
| 2 | Two pointers | 0: indexing, loops | sliding window, linked-list fast/slow pointers |
| 3 | Stack, first classes | 0: lists | the call stack in recursion; classes for linked lists and trees |
| 4 | Sliding window | 1 counting + 2 pointers | |
| 5 | Binary search | 0: logarithms, 2: invariants | binary search trees |
| 6 | Recursion and divide and conquer | 3: call stack | linked lists, trees, backtracking, DP |
| 7 | Linked lists | 0 aliasing, 2 pointers, 3 classes, 6 recursion | trees (nodes and references) |
| 8 | Trees and BSTs | 6 recursion, 7 nodes, 5 binary search | heaps, backtracking, graphs |
| 9 | Heaps | 8 tree picture, 1 tuple keys | Dijkstra (later) |
| 10 | Backtracking | 6 recursion, 8 tree DFS, 0 aliasing | DP (brute force first) |
| 11 | Graphs | 1 dicts and sets, 8 DFS/BFS, 3 queues | |
| 12 | 1-D dynamic programming | 6 recursion trees, 1 memo dicts, 10 brute force | |

## Stages and problems

Weeks assume about 5 hours per week. LeetCode numbers in brackets.

| Stage | Key concepts | Problems | Weeks |
| --- | --- | --- | --- |
| 0 | accumulator, aliasing, Big-O, built-in costs | 8 warm-ups, Running Sum (1480) | 1.5 |
| 1 | dict, set, Counter, `key=`, lambda, tuple keys | Contains Duplicate (217), Valid Anagram (242), Two Sum (1), Group Anagrams (49), Sort by Frequency (1636), Top-k Words ✅ | 2 |
| 2 | converging pointers, loop invariant | Reverse String (344), Valid Palindrome (125), Squares of a Sorted Array (977), Two Sum II (167), Container With Most Water (11); stretch 3Sum (15) | 2 |
| 3 | LIFO, `deque`, classes | Valid Parentheses (20), Min Stack (155), Evaluate RPN (150), Queue using Stacks (232); stretch Daily Temperatures (739) | 1.5 |
| 4 | fixed and variable window, counts in a dict | Max Average Subarray (643), Best Time to Buy and Sell Stock (121), Contains Duplicate II (219), Longest Substring Without Repeating (3); stretch 424, 567 | 2 |
| 5 | `lo`/`hi` invariant, monotonic condition, search on the answer | Binary Search (704), Search Insert Position (35), Search a 2D Matrix (74), Koko Eating Bananas (875); stretch 153 | 2 |
| 6 | base case, call stack, recursion tree, `@cache`, merge sort | Fibonacci (509), Climbing Stairs (70), Pow(x, n) (50), Sort an Array with merge sort (912), Binary Search rewritten recursively | 3 |
| 7 | node references, dummy head, fast/slow pointers | Reverse Linked List (206, both ways), Merge Two Sorted Lists (21), Middle of the List (876), Linked List Cycle (141); stretch 19, 143 | 2 |
| 8 | recursive DFS, BFS with a queue, BST invariant | Max Depth (104), Same Tree (100), Invert Tree (226), Level Order (102), Validate BST (98); stretch 230 | 3 |
| 9 | `heapq`, top-k with a size-k heap | Last Stone Weight (1046), Kth Largest in a Stream (703), Top K Frequent (347), K Closest Points (973); stretch 215, 23 | 1.5 |
| 10 | choose, explore, unchoose; 2ⁿ and n! | Subsets (78), Permutations (46), Combination Sum (39), Letter Combinations (17); stretch 79 | 2.5 |
| 11 | adjacency dict, visited set, grid BFS/DFS, topological order | Flood Fill (733), Number of Islands (200), Max Area of Island (695), Rotting Oranges (994); stretch 207, 133 | 3.5 |
| 12 | memoisation to table, state and transition | Climbing Stairs again (70), Min Cost Climbing Stairs (746), House Robber (198), Coin Change (322); stretch 62 | 3 |

**Core total:** about 60 problems, about 30 working weeks. Plan for about 35 calendar weeks so exams and holidays don't break the streak.

**After the core** (8 to 10 weeks): intervals and greedy (56, 435, 55), tries (208), union-find, 2-D DP (1143), then mixed problem sets without topic labels and mock interviews.

Stages get scaffolded one at a time, when you reach them. That keeps the plan adjustable and avoids spoilers.

## The weekly rhythm

**3 deep sessions of about 90 minutes, plus 1 short review session of 30 to 45 minutes.**

### Deep session

1. **Warm-up recall (10 min).** Re-solve one problem that's due in [REVIEW.md](REVIEW.md) from a blank file, or explain the last concept out loud without notes
2. **New pattern? Explore first (10 to 15 min).** On the first problem of a stage, try any idea, even brute force, *before* reading the primer. Then read the primer and its worked example. New Python mechanics (like `key=` or `deque`) are the exception: read and drill those first, then use them
3. **Solve (30 to 40 min)** with [PROCESS.md](PROCESS.md). Write two edge-case tests of your own before coding
4. **Stuck?** Open the next hint after about 15 minutes without a new idea. After hint 3, read a solution, explain it back in your own words in `notes.md`, close it, and re-implement it from a blank file
5. **Look back (10 min).** Fill in `notes.md`, explain the solution out loud for 2 minutes as if in an interview, and read one alternative solution

### Review session

Pick 2 or 3 problems from [REVIEW.md](REVIEW.md) **by name only**, without looking at their stage folder. Deciding *which* pattern fits is the skill being trained here, so the label must stay hidden. Start these sessions from stage 3 on, once there are at least three patterns to mix.

### Review schedule

| How it went | What to do next |
| --- | --- |
| Solved with 0 or 1 hint | 2-minute recall after 1 week: say the key idea and the Big-O out loud |
| Needed 2+ hints or a solution | full re-solve from a blank file after 1 day, 1 week and 1 month |
| A re-solve fails | back to 1 day |

### Moving to the next stage

Try one unseen easy or lower-medium problem of the stage's pattern. Aim for under 45 minutes, at most 1 hint, with the Big-O justified. If it doesn't work out, do two more problems of that stage and move on anyway. The weekly review session will bring the pattern back.

## Companion resources

1. [Python Tutor](https://pythontutor.com/python-compiler.html#mode=edit) for seeing aliasing, the call stack and recursion step by step
2. [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds3/index.html) (free, Python). Its chapters on algorithm analysis, basic data structures, recursion, searching and sorting, trees and graphs line up with stages 0, 3, 6, 5/6, 8/9 and 11
3. [NeetCode](https://neetcode.io/roadmap) video explanations after you've solved a problem, as the "alternative solution"

## Why the method looks like this

| Choice | Evidence |
| --- | --- |
| Recall and spaced re-solving instead of re-reading | Practice testing and spacing are the only two techniques rated "high utility" in a large review ([Dunlosky et al. 2013](https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html)). Testing beat restudying on delayed tests ([Roediger and Karpicke 2006](https://pubmed.ncbi.nlm.nih.gov/16507066/)). The exact intervals are a heuristic ([Cepeda et al. 2006](https://pubmed.ncbi.nlm.nih.gov/16719566/)) |
| Mixed review with hidden labels | Interleaving helps most when categories look similar, g = 0.42 overall and 0.34 for maths ([Brunmair and Richter 2019](https://www.psychologie.uni-wuerzburg.de/fileadmin/06020400/2019/Brunmair_Richter_in_press__2019_META-ANALYSIS_OF_INTERLEAVED_LEARNING.pdf)). Two pointers, sliding window and binary search are exactly such look-alikes |
| Explore before the primer, only for new patterns | Problem solving followed by instruction helps conceptual understanding and transfer, g = 0.36, but not procedural skill ([Sinha and Kapur 2021](https://journals.sagepub.com/doi/10.3102/00346543211019105)) |
| Worked examples at the start of a stage, fewer later | Guidance that helps beginners gets in the way once you know the material, so it gets faded by performance ([Kalyuga 2007](https://link.springer.com/article/10.1007/s10648-007-9054-3)) |
| One new mechanic at a time | Top-k Words asked for counting, lambdas, tuple keys and Big-O at once, which is the overload this order now avoids |

## Course sources

[MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/calendar), [MIT 6.100L](https://www.ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/calendar), [Stanford CS106B](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1258/lecture_index), [Berkeley CS61B](https://sp24.datastructur.es/), [Princeton COS 226](https://www.cs.princeton.edu/courses/archive/spring23/cos226/lectures.php), [UCPH Algoritmer og datastrukturer](https://kurser.ku.dk/course/ndaa04010u), [Tech Interview Handbook](https://www.techinterviewhandbook.org/coding-interview-study-plan/), [NeetCode roadmap order](https://github.com/bhanuprasadChesetti/neetcode-dsa-roadmap).
