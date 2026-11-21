## Assertions Pseudocode

# Covers src/lib/assertions.py: the run_test helper used by every test file to print PASS/FAIL/ERROR.
# This is the test framework used by the Quality Lead. The project spec does not allow pip-installed
# packages, and pytest (the popular test framework) needs to be installed, so this is a small
# custom test framework built to cover what the project actually needs.
# Author: Dan Pablo

START
    LET MAX_REPR_LEN = 50

    FUNC _short_repr(value)
        LET text = REPR(value)
        IF LENGTH(text) > MAX_REPR_LEN THEN
            text = SUBSTRING(text, 0, MAX_REPR_LEN) + "..."
        ENDIF
        RETURN text
    ENDFUNC

    FUNC run_test(actual, expected, test_name, comparison)
        LET compare = COMPARISONS[comparison]

        # actual may be a value or a zero-arg function; calling it here means
        # an error it raises is caught below instead of crashing the test file
        TRY
            IF actual IS CALLABLE THEN
                actual = actual()
            ENDIF
            LET passed = compare(actual, expected)
        EXCEPT error
            PRINT "FAIL: ERROR! " + test_name + " | " + TYPE_OF(error) + ": " + error
            RETURN
        ENDTRY

        IF passed THEN
            PRINT "PASS: " + test_name
        ELSE
            PRINT "FAIL: " + test_name + " (expected " + _short_repr(actual) + " " + comparison + " " + _short_repr(expected) + ")"
        ENDIF
    ENDFUNC
END
