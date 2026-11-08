# para_po

Para Po! Jeepney Route Finder. CMSC-202 Final Project, Team HEX.

## Project structure

```
para_po/
├── main.py              entry point, run this
├── src/                 program code
│   ├── features/
│   │   └── menu.py      menu option handlers (find route, admin mode, etc.)
│   ├── ui/
│   │   └── menu.py      screens and menu text
│   └── libs/
│       ├── constants.py fixed values: file paths, group settings
│       └── setup.py     one-time startup helpers
├── data/                data files
├── contribution_logs/   work logs
└── deliverables/        submission files
```

- `data/`: `stops.csv`, `routes.csv` (route network), `trip_history.csv` (generated at runtime)
- `contribution_logs/`: each member's own work log, see its README for how to fill it
- `deliverables/`: design doc, logs, and the course-facing README for submission

## Running it

```
python main.py
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
