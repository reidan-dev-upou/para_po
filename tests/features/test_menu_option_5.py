"""
Tests for src/features/menu_option_5.py.
Run with: python3 -m tests.features.test_menu_option_5
"""

from src.lib.assertions import run_test

run_test(
    actual="GROUP_NAME",
    expected=header,
    test_name="update_setup_header replaces all placeholders",
    comparison="not in",
)
