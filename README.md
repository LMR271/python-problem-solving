# Python Problem Solving

![tests](https://github.com/LMR271/python-problem-solving/actions/workflows/tests.yml/badge.svg)

A structured log of how I'm learning data structures, algorithms and problem solving in Python, from basic loops up to the standard interview patterns. Every problem has tests, and every solution has notes on how I got there, its complexity and what tripped me up.

1. [ROADMAP.md](ROADMAP.md) is the learning path, ordered so every stage builds on the ones before it
2. [PROCESS.md](PROCESS.md) is the method I follow on every problem
3. [REVIEW.md](REVIEW.md) is my spaced-repetition log

## Progress

| Stage | Topic | Solved |
| --- | --- | --- |
| 0 | [Python warm-ups and Big-O](problems/stage-0-python-warmups) | 2 / 9 |
| 1 | [Arrays and hashing, sort keys](problems/stage-1-arrays-hashing) | 1 / 6 |
| 2 | [Two pointers](problems/stage-2-two-pointers) | 0 / 5 |
| 3 | [Stack](problems/stage-3-stack) | 0 / 4 |
| 4 to 12 | Sliding window, binary search, recursion, linked lists, trees, heaps, backtracking, graphs, DP | see roadmap |

## Repo layout

```
problems/
  stage-1-arrays-hashing/
    README.md                   concept primer for the stage
    03-two-sum/
      problem.md                task, examples, paper questions, hidden hints
      two_sum.py                my solution
      test_two_sum.py           tests
      notes.md                  key idea, pattern trigger, complexity, bugs
bin/new_problem.py              scaffolds a new problem folder
```

## Running the tests

```bash
conda env create -f environment.yml   # first time only
conda activate pps

pytest                                                  # everything
pytest problems/stage-0-python-warmups -v               # one stage
pytest problems/stage-0-python-warmups/01-sum-list -v   # one problem
```

Unsolved problems show up as **skipped** ("not solved yet"), so the suite stays green while I work through the list.
