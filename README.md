# Python Problem Solving

![tests](https://github.com/LMR271/python-problem-solving/actions/workflows/tests.yml/badge.svg)

A structured log of how I practice algorithmic problem solving in Python. Every problem comes with tests, and every solution comes with notes on how I got there, what complexity it has and what tripped me up.

The focus is the **process**, not just the answer. See [PROCESS.md](PROCESS.md) for the method I follow on every problem.

## Repo layout

```
problems/
  001-top-k-words/
    problem.md              task, examples, questions to answer before coding
    top_k_words.py          my solution
    test_top_k_words.py     tests (edge cases included)
    notes.md                approach, complexity, lessons learned
bin/new_problem.py          scaffolds a new problem folder
PROCESS.md                  my problem-solving method
```

## Running the tests

```bash
conda env create -f environment.yml   # first time only
conda activate pps

pytest                                  # all problems
pytest problems/001-top-k-words -v      # one problem
```

Unsolved problems show up as **skipped** ("not solved yet"), so the test suite stays green while I work through the list.

## Progress

| #   | Problem                                          | Pattern       | Difficulty | Status |
| --- | ------------------------------------------------ | ------------- | ---------- | ------ |
| 001 | [Top-k Words](problems/001-top-k-words)          | Hash map      | Easy       | ✅     |
| 002 | [Balanced Brackets](problems/002-balanced-brackets) | Stack      | Easy       | ⬜      |
| 003 | [Clean Palindrome](problems/003-clean-palindrome) | Two pointers | Easy       | ⬜      |
