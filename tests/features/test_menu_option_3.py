"""
Tests for src/features/menu_option_3.py.
Run with: python3 -m tests.features.test_menu_option_3
"""

from src.lib.assertions import run_test
from src.features.menu_option_3 import admin_mode_password_checker

run_test(
    actual=admin_mode_password_checker(admin_mode_user_attempt="Hex"),
    expected=True,
    test_name="admin_mode_password_checker checks if password is 'Hex'",
)

run_test(
    actual=admin_mode_password_checker(admin_mode_user_attempt="12345"),
    expected=False,
    test_name="admin_mode_password_checker rejects a wrong password",
)

run_test(
    actual=admin_mode_password_checker(admin_mode_user_attempt=""),
    expected=False,
    test_name="admin_mode_password_checker rejects an empty password",
)

run_test(
    actual=admin_mode_password_checker(admin_mode_user_attempt="hex"),
    expected=False,
    test_name="admin_mode_password_checker rejects lowercase hex",
)