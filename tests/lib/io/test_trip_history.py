"""
Tests for src/lib/io/trip_history.py.
Run with: python3 -m tests.lib.io.test_trip_history
"""

from src.lib.assertions import run_test
from src.lib.io import trip_history as mod
from src.lib.constants import DATA_DIR

_TEST_DATA_DIR = DATA_DIR / "_test_trip_history_dir"


def _test_add_trip_history():
    """Point the module's DATA_DIR at a throwaway folder so this never touches the real file."""
    _TEST_DATA_DIR.mkdir(exist_ok=True)
    original_data_dir = mod.DATA_DIR
    mod.DATA_DIR = _TEST_DATA_DIR

    try:
        first_trip = {"date": "2026-11-25", "origin": "A", "destination": "B", "chosen_path": "A > B", "fare": "10"}
        second_trip = {"date": "2026-11-25", "origin": "B", "destination": "C", "chosen_path": "B > C", "fare": "12"}

        mod.add_trip_history(**first_trip)
        run_test(mod.read_trip_history(), [first_trip], "add_trip_history appends the first row with a header")

        mod.add_trip_history(**second_trip)
        run_test(
            mod.read_trip_history(),
            [first_trip, second_trip],
            "add_trip_history appends without touching the existing row",
        )

        mod.add_trip_history(date="", origin="A", destination="B", chosen_path="A > B", fare="10")
        run_test(
            mod.read_trip_history(),
            [first_trip, second_trip],
            "add_trip_history rejects a missing field without appending",
        )
    finally:
        mod.DATA_DIR = original_data_dir
        (_TEST_DATA_DIR / "trip_history.csv").unlink(missing_ok=True)
        _TEST_DATA_DIR.rmdir()


if __name__ == "__main__":
    _test_add_trip_history()
