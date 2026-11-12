# para_po

Para Po! Jeepney Route Finder. CMSC-202 Final Project, Team HEX.

## Project structure

```
para_po/
├── main.py              entry point, run this
├── src/                 program code
│   ├── features/
│   │   ├── menu.py          menu loop and setup header
│   │   └── menu_option_N.py one file per menu option, logic and screen text together
│   └── lib/
│       ├── constants.py fixed values: file paths, group settings
│       ├── setup.py     one-time startup helpers
│       ├── io.py        reading and writing data files
│       ├── utils.py     small shared helpers (input validation, formatting)
│       └── assertions.py run_test(), the test helper, see Tests below
├── tests/               one test_<name>.py per file it tests, same folder shape as src/
├── data/                data files
├── contribution_logs/   work logs
└── deliverables/        submission files
```

- `data/`: `stops.csv`, `routes.csv` (route network), `trip_history.csv` (generated at runtime)
- `contribution_logs/`: each member's own work log, see its README for how to fill it
- `deliverables/`: design doc, logs, and the course-facing README for submission
  - `deliverables/algorithms/`: the algorithms design deliverable (flowchart or
    pseudocode), one folder per `src/features/menu*.py` file it covers
    (`menu`, `menu_option_1` to `menu_option_4`)

## Writing a function

- Put it in the right file: a menu option (logic and screen text together)
  goes in its own `src/features/menu_option_N.py`, the menu loop itself in
  `src/features/menu.py`, a fixed value in `src/lib/constants.py`, file
  reading/writing in `src/lib/io.py`, and a small shared helper in
  `src/lib/utils.py`.
- Name it in `snake_case`, as `<ACTION>_<WHAT IT ACTS ON>`, for example
  `get_value_a` or `write_output`. Not `doStuff` or `function1`.
- Give it a docstring explaining what it does, its parameters, and what
  it returns.
- Add an author tag, `# Author: <your name>`, right above the function.
- Name variables to say what they hold, not `a`, `b`, `x`, or `temp`.
- Add a `#` comment inside the function wherever a step isn't obvious
  from the code alone, describing what that step is doing.

```python
# Author: Juan Dela Cruz
def add_numbers(first_number, second_number):
    """Add two numbers together.

    first_number: the first number to add.
    second_number: the second number to add.

    Returns the sum of the two numbers.
    """
    # add the two numbers and return the total
    return first_number + second_number
```

## Running it

```
python main.py
```

## Tests

### Running a test

Run it as a module from the project root, not by its file path:

```
python3 -m tests.features.test_menu
```

Each check prints 🟢 PASS or 🔴 FAIL with the test's name.

### Adding a test

1. Create `tests/<folder>/test_<name>.py`, matching the path of the file
   you're testing under `src/` (for example, `src/features/menu.py` gets
   `tests/features/test_menu.py`).
2. Import `run_test` from `src.lib.assertions`, and the function you're
   testing.
3. Call `run_test(actual, expected, test_name)` for each check. It
   defaults to `comparison="=="`; the full list of comparisons is:

   | `comparison` | Checks that... |
   |---|---|
   | `"=="` (default) | `actual` equals `expected` |
   | `"!="` | `actual` does not equal `expected` |
   | `"<"` | `actual` is less than `expected` |
   | `"<="` | `actual` is less than or equal to `expected` |
   | `">"` | `actual` is greater than `expected` |
   | `">="` | `actual` is greater than or equal to `expected` |
   | `"in"` | `actual` is contained in `expected` (e.g. a substring check) |
   | `"not in"` | `actual` is not contained in `expected` |

Cover the normal case and the edge/invalid-input cases, not just the
happy path. The `Quality and Testing Lead` will check that all cases are
covered.

```python
"""Tests for src/lib/utils.py. Run with: python3 -m tests.lib.test_utils"""

from src.lib.assertions import run_test
from src.lib.utils import add_numbers

run_test(
    actual=add_numbers(first_number=2, second_number=3),
    expected=5,
    test_name="add_numbers adds two positive numbers",
)

run_test(
    actual=add_numbers(first_number=2, second_number=3),
    expected=[4, 5, 6],
    test_name="add_numbers result is one of the expected values",
    comparison="in",
)
```

## Setup (one time)

Type all the `git ...` commands below into a terminal (Terminal on Mac,
Command Prompt or Git Bash on Windows), not into your code editor.

1. Make sure Git is installed on your computer. Run `git --version` in a
   terminal; if it shows a version number, you're set. If not, install it
   from [git-scm.com](https://git-scm.com/downloads).
2. Register a GitHub account at github.com if you don't have one yet.
3. Make sure you're added as a collaborator on this repo by the `Integration Lead`.
4. Clone the repo to your computer:
   ```
   git clone https://github.com/reidan-dev-upou/para_po.git
   cd para_po
   ```
5. Create your own branch, named `dev_<YOUR NAME>`:
   ```
   git checkout -b dev_<YOUR NAME>
   ```
   For example, if your name is Dan: `git checkout -b dev_DAN`
6. Do all your work on that branch, never on `main`.

⚠️ Before you start working each time, run `git branch` and check that the
branch with a `*` next to it is your `dev_<YOUR NAME>` branch, not `main`.

```
$ git branch
* dev_DAN
  main
```

## Workflow (every time you work)

1. Make your changes (edit or add files).
2. Stage the files you changed:
   ```
   git add <file>
   ```
   For example: `git add src/features/menu.py`

   If you changed several files and want to stage all of them at once:
   ```
   git add .
   ```
3. Commit what you staged:
   ```
   git commit -m "<ACTION> <ITEM WORKED ON>"
   ```
   Keep the message short and specific, same style as the contribution log,
   for example `git commit -m "Add find_all_paths function"`.
4. Push your branch:
   ```
   git push origin dev_<YOUR NAME>
   ```
   For example: `git push origin dev_DAN`
5. Repeat steps 1 to 4 as you keep working.

Every end of week (Friday/Saturday, or sooner if needed), the `Integration
Lead` merges everyone's branch into `main`. Only the `Integration Lead`
works directly on `main`.

Once the lead finishes merging, they'll tell you to pull the latest `main`
into your branch:
```
git checkout dev_<YOUR NAME>
git pull origin main
```

⚠️ Do not make or commit any changes on your branch while the lead is
merging, to avoid merge conflicts. If a conflict happens anyway, stop and
contact the `Integration Lead` instead of resolving it yourself.

Then go back to step 1 and repeat.

## Contributing

- Log your own work in `contribution_logs/contribution_log_<YOUR NAME>.csv` as you go. See `contribution_logs/README.md`.
- Don't edit `deliverables/contribution_log.csv` directly, it's collated from everyone's file later.
- Add an entry to `deliverables/version_log.txt` whenever a working version is combined/merged.
