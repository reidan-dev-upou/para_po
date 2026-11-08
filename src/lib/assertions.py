"""A tiny test helper for tests: no pytest needed."""

import operator as operator_module

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


def run_test(actual, expected, test_name, comparison="=="):
    """Check actual against expected and print the result for test_name.

    comparison: one of "==", "!=", "<", "<=", ">", ">=", "in", "not in".
    """
    compare = _COMPARISONS[comparison]
    if compare(actual, expected):
        print(f"  🟢 PASS: {test_name}")
    else:
        print(f"  🔴 FAIL: {test_name} (expected {actual!r} {comparison} {expected!r})")
