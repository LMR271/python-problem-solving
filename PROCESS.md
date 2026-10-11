# My Problem-Solving Process

Based on the **UMPIRE method** (a six-step routine used in interview prep: Understand, Match, Plan, Implement, Review, Evaluate). The point is to never stare at an empty file. There is always a next step.

## 1. Understand

Goal: know exactly what is asked before thinking about code.

- Restate the problem in one sentence, in my own words.
- Write down the **input and output types** (what goes in, what comes out).
- Solve 2 or 3 examples **by hand, on paper**. Write down every single step I did. Those steps are the first draft of the algorithm.
- List **edge cases** (unusual inputs that often break code): empty input, one element, duplicates, ties, negative numbers, very large input.

If I can't solve an example by hand, I can't code it yet. Go back here.

## 2. Match

Goal: does this look like a problem I've seen?

Ask:
- Am I counting or looking things up? → **hash map** (`dict`, `Counter`, `set`)
- Do things need to be matched or undone in reverse order? → **stack** (last in, first out)
- Am I comparing from both ends, or scanning a sorted list? → **two pointers**
- Am I looking at a contiguous chunk of a list or string? → **sliding window**
- Can the problem be split into smaller copies of itself? → **recursion** / **dynamic programming**

## 3. Plan

Goal: a solution in plain words or **pseudocode** (code-like steps without Python syntax) before typing any real code.

- First plan the **brute force** solution (the simplest correct approach, however slow). Correct beats clever.
- Walk through one example with the plan. Does it give the right answer?

## 4. Implement

- Translate the plan line by line.
- Run the tests early and often: `pytest problems/<folder> -v`.
- If a test fails, read the failure message carefully before changing anything.

## 5. Review

- Read the code top to bottom as if someone else wrote it.
- Would a clearer name or a smaller helper function make it easier to follow?
- Trace a tricky edge case through the code by hand.

## 6. Evaluate

- **Time complexity** (how runtime grows as the input grows, written in Big-O notation like O(n)).
- **Space complexity** (how much extra memory grows as the input grows).
- Can I do better? If yes, that's the optimized version. Keep the tests green while refactoring.
- Fill in `notes.md`.

## When stuck

- Timebox about 25 minutes without progress, then ask for the next hint.
- Hint ladder: **Hint 1** a nudge, **Hint 2** the technique or data structure, **Hint 3** pseudocode.
- Log which hints I used in `notes.md`. That is how I see progress over time.
