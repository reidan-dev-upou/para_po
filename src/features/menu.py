"""Menu option handlers: find route, admin mode, and the rest of the
main menu's actions.
"""

from src.lib.constants import GROUP_NAME, MENU_SETUP_HEADER


def update_setup_header():
    """Fill in the setup header template with real values.

    Returns the setup header text, ready to print.
    """
    setup_header = MENU_SETUP_HEADER

    setup_header_dict = {
        "GROUP_NAME": GROUP_NAME,
        "MEMBER_NAMES": "AA, BB, CC",
        "GROUP_SEED": "00000",
        "BASE_FARE": "XXX",
        "EXTRA_FARE": "YY",
        "DISCOUNT_PERCENTAGE": "Z",
        "DATA_STOPS": "DD",
        "DATA_ROUTES": "EE",
    }

    for placeholder, actual_value in setup_header_dict.items():
        # replace() returns a new string, it doesn't change setup_header in place
        setup_header = setup_header.replace(placeholder, str(actual_value))

    return setup_header

