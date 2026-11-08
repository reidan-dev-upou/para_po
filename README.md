# para_po

Para Po! Jeepney Route Finder — CMSC-202 Final Project, Team HEX.

## Project structure

```
main.py             entry point, run only
src/
  features/          menu-option handlers
  ui/                 display/menu output
  libs/               constants and setup helpers
data/                 stops.csv, routes.csv (route network), trip_history.csv (generated)
contribution_logs/     each member's own work log, see its README
deliverables/          files for course submission (design doc, logs, course-facing README)
```

## Running it

```
python main.py
```

## Contributing

- Log your own work in `contribution_logs/contribution_log_<YOUR NAME>.csv` as you go. See `contribution_logs/README.md`.
- Don't edit `deliverables/contribution_log.csv` directly, it's collated from everyone's file later.
- Add an entry to `deliverables/version_log.txt` whenever a working version is combined/merged.
