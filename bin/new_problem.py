"""Scaffold a new problem folder.

Usage:
    python bin/new_problem.py 004 two-sum

Creates problems/004-two-sum/ with problem.md, two_sum.py,
test_two_sum.py and notes.md. Existing files are never overwritten.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NOTES = """# Notes · {title}

## Approach
How I solved it, in 2 to 4 sentences.

## Complexity
- Time: O(?)
- Space: O(?)

## What tripped me up


## Hints used
0 / 1 / 2 / 3
"""

PROBLEM = """# {number} · {title}

**Pattern:**
**Difficulty:**

## Task


## Examples

```python
```

## Before you code (on paper)

1.

## Run the tests

```bash
pytest problems/{folder} -v
```
"""

SOLUTION = """def {module}():
    raise NotImplementedError
"""

TEST = """from {module} import {module}


def test_example():
    assert {module}() == ...
"""


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)

    number, slug = sys.argv[1].zfill(3), sys.argv[2].lower()
    folder = f"{number}-{slug}"
    module = slug.replace("-", "_")
    title = slug.replace("-", " ").title()
    values = dict(number=number, title=title, folder=folder, module=module)

    target = ROOT / "problems" / folder
    target.mkdir(parents=True, exist_ok=True)

    files = {
        "problem.md": PROBLEM,
        f"{module}.py": SOLUTION,
        f"test_{module}.py": TEST,
        "notes.md": NOTES,
    }
    for name, template in files.items():
        path = target / name
        if path.exists():
            print(f"skip    {path.relative_to(ROOT)} (exists)")
            continue
        path.write_text(template.format(**values))
        print(f"create  {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
