"""
A tiny test helper for tests: no pytest needed.
"""

import operator as operator_module

_MAX_REPR_LEN = 50

# Author: Dan Pablo
def _short_repr(value):
    """Return repr(value) (value's debug string), trimmed to _MAX_REPR_LEN chars."""
    text = repr(value)
    if len(text) > _MAX_REPR_LEN:
        text = text[:_MAX_REPR_LEN] + "..."
    return text


_COMPARISONS = {
    "==": operator_module.eq,
    "!=": operator_module.ne,
    "<": operator_module.lt,
    "<=": operator_module.le,
    ">": operator_module.gt,
    ">=": operator_module.ge,
    "in": lambda actual, expected: actual in expected,
    "not in": lambda actual, expected: actual not in expected,
}

# Author: Dan Pablo
def run_test(actual, expected, test_name, comparison="=="):
    """Compare actual to expected and print PASS/FAIL/ERROR for test_name.

    actual may be a value, or a zero-arg function if getting it can raise.
    comparison: one of "==", "!=", "<", "<=", ">", ">=", "in", "not in".
    """
    compare = _COMPARISONS[comparison]
    try:
        # call actual() here so a raised error is caught below, not crashing the test file
        if callable(actual):
            actual = actual()
        passed = compare(actual, expected)
    except Exception as error:
        print(f"  🔴 FAIL: ERROR! {test_name} | {type(error).__name__}: {error}")
        return
    if passed:
        print(f"  🟢 PASS: {test_name}")
    else:
        print(f"  🔴 FAIL: {test_name} (expected {_short_repr(actual)} {comparison} {_short_repr(expected)})")
