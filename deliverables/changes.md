# Changes (current WIP on main)

## `main.py`
- Removed `load_setup()` call + import (deleted, not moved)

## `src/features/menu.py`
- `update_setup_header()` now uses real values instead of placeholders:
  - `get_group_seed()`, `get_group_settings()` → from `src/lib/setup.py`
  - `read_members_info()` → from `src/lib/io/members.py`
  - `read_routes()`, `read_stops()` → from `src/lib/io/routes.py`, `src/lib/io/stops.py`

## `src/features/menu_option_1.py`
- `show_menu_1()`: stub text changed to `"--- FIND A ROUTE ---"` (still not wired to real logic)
- `save_trip_history()` → `src/lib/io/trip_history.py` as `add_trip_history()`
- `compute_group_seed()` → `src/lib/setup.py` as `get_group_seed()` (now reads `members.csv` itself)
- `get_group_settings(seed)` → `src/lib/setup.py` as `get_group_settings()` (no param, calls `get_group_seed()` internally)
- `calculate_route_distance()` → **removed** (not used anywhere yet)
- `main()` (smoke test) → **removed**

## `src/features/menu_option_2.py`
- `read_stops` import: `src/lib/io` → `src/lib/io/stops.py`

## `src/features/menu_option_3.py`
- `read_stops`, `read_routes` imports: `src/lib/io` → `src/lib/io/stops.py`, `src/lib/io/routes.py`
- `write_csv` import dropped (add/remove flows still just print placeholders)

## `src/lib/setup.py`
- `load_setup()` → **removed** (menu.py calls the two functions below directly)
- `get_group_settings()` — real implementation, moved in from `menu_option_1.py`
- `get_group_seed()` — real implementation, moved in from `menu_option_1.py`'s `compute_group_seed()`

## `src/lib/io.py` → split into `src/lib/io/` package
| old | new |
|---|---|
| `read_menu_input()`, `read_csv()` | `src/lib/io/__init__.py` (unchanged) |
| `write_csv()` | `__init__.py` as `overwrite_csv()` + `append_csv()` |
| `read_routes()` | `src/lib/io/routes.py` (+ new `overwrite_routes()`, `add_route()`, `remove_route()`) |
| `read_stops()` | `src/lib/io/stops.py` (+ new `overwrite_stops()`) |
| `read_members_info()` | `src/lib/io/members.py` (unchanged) |
| *(new)* | `src/lib/io/trip_history.py`: `read_trip_history()`, `add_trip_history()` |

## `tests/lib/test_io.py` → split into `tests/lib/io/`
- Same split as above: `test_members.py`, `test_routes.py`, `test_stops.py`, `test_trip_history.py`

## `README.md`
- Documents the new `src/lib/io/` package split

## `deliverables/v02/screenshots/` (new)
- Main menu + admin mode flow (login, add/remove stop, add/remove segment)
- Options 1, 2, 4 skipped — same WIP stub as v01
