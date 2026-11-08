"""Tests for src/features/menu.py. Run with: python3 -m tests.features.test_menu"""

from src.lib.assertions import run_test
from src.features.menu import update_setup_header

header = update_setup_header()

run_test(
    actual=isinstance(header, str),
    expected=True,
    test_name="update_setup_header returns a string",
)

run_test(
    actual="Team HEXxx",
    expected=header,
    test_name="update_setup_header includes the group name",
    comparison="in",
)

run_test(
    actual="GROUP_NAME",
    expected=header,
    test_name="update_setup_header replaces all placeholders",
    comparison="not in",
)
