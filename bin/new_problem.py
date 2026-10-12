"""Scaffold a new problem folder inside a stage.

Usage:
    python bin/new_problem.py <stage-folder> <number> <slug>

Example:
    python bin/new_problem.py stage-2-two-pointers 02 two-sum-sorted

Creates problems/stage-2-two-pointers/02-two-sum-sorted/ with problem.md,
two_sum_sorted.py, test_two_sum_sorted.py and notes.md.
Existing files are never overwritten. Module names must be unique across
the whole repo, because pytest imports every test file side by side.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NOTES = """# Notes · {title}

## Key idea (one line)
The sentence I'd say to recall the whole solution.

## Pattern trigger
"When I see ..., I think ..."

## Approach
How I solved it, in 2 to 4 sentences.

## Complexity
- Time: O(?) because ...
- Space: O(?) because ...

## Bug I made / what tripped me up


## Alternative I read afterwards


## Hints used
0 / 1 / 2 / 3
"""

PROBLEM = """# {title}

**Stage:** {stage} · **Difficulty:** · **New concept:**

## Task


## Examples

```python
```

## Before you code (on paper)

1.

## Hints

<details>
<summary>Hint 1 · a nudge</summary>

</details>

<details>
<summary>Hint 2 · the tool</summary>

</details>

<details>
<summary>Hint 3 · pseudocode</summary>

</details>

## Run the tests

```bash
pytest {path} -v
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
    if len(sys.argv) != 4:
        sys.exit(__doc__)

    stage, number, slug = sys.argv[1], sys.argv[2].zfill(2), sys.argv[3].lower()
    stage_dir = ROOT / "problems" / stage
    if not stage_dir.is_dir():
        sys.exit(f"Unknown stage folder: {stage}")

    module = slug.replace("-", "_")
    clash = [p for p in (ROOT / "problems").rglob(f"{module}.py")]
    if clash:
        sys.exit(f"Module name {module}.py already exists at {clash[0].relative_to(ROOT)}")

    folder = f"{number}-{slug}"
    target = stage_dir / folder
    target.mkdir(exist_ok=True)
    values = dict(
        title=slug.replace("-", " ").title(),
        stage=stage,
        path=f"problems/{stage}/{folder}",
        module=module,
    )

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
