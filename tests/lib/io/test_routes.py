"""
Tests for src/lib/io/routes.py.
Run with: python3 -m tests.lib.io.test_routes
"""

from src.lib.assertions import run_test
from src.lib.io import routes as routes_module
from src.lib.constants import DATA_DIR

_TEST_DATA_DIR = DATA_DIR / "_test_routes_dir"


def _with_test_routes_file(test_function):
    """Point the module's DATA_DIR at a throwaway folder, run test_function, then clean up."""
    _TEST_DATA_DIR.mkdir(exist_ok=True)
    original_data_dir = routes_module.DATA_DIR
    routes_module.DATA_DIR = _TEST_DATA_DIR
    try:
        test_function()
    finally:
        routes_module.DATA_DIR = original_data_dir
        (_TEST_DATA_DIR / "routes.csv").unlink(missing_ok=True)
        _TEST_DATA_DIR.rmdir()


def _test_add_and_remove_route():
    route = {"route_name": "R1", "stop_a": "A", "stop_b": "B", "distance_km": "1.5"}
    other_route = {"route_name": "R1", "stop_a": "B", "stop_b": "C", "distance_km": "2.0"}

    routes_module.add_route(route)
    run_test(routes_module.read_routes(), [route], "add_route saves a valid new segment")

    routes_module.add_route(route)
    run_test(routes_module.read_routes(), [route], "add_route rejects a duplicate segment")

    routes_module.add_route({"route_name": "R1", "stop_a": "A", "stop_b": "A", "distance_km": "1"})
    run_test(routes_module.read_routes(), [route], "add_route rejects a stop connected to itself")

    routes_module.add_route({"route_name": "R1", "stop_a": "A", "stop_b": "C", "distance_km": "0"})
    run_test(routes_module.read_routes(), [route], "add_route rejects a non-positive distance")

    routes_module.add_route(other_route)
    run_test(routes_module.read_routes(), [route, other_route], "add_route saves a second segment")

    routes_module.remove_route(route)
    run_test(routes_module.read_routes(), [other_route], "remove_route removes the matching segment")

    routes_module.remove_route(route)
    run_test(routes_module.read_routes(), [other_route], "remove_route leaves data untouched when segment is already gone")


if __name__ == "__main__":
    _with_test_routes_file(_test_add_and_remove_route)
