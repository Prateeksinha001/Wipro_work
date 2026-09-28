"""
Custom Robot Framework keyword library.

Any public, module-level function in a .py file imported as a Library
automatically becomes a Robot Framework keyword. Robot converts the
function name from snake_case to Title Case With Spaces, e.g.
`add_two_numbers` becomes the keyword "Add Two Numbers".
"""

import csv
import os


def add_two_numbers(a, b):
    """Custom keyword: adds two numbers and returns the result.

    Usage in a .robot file:
        ${result}=    Add Two Numbers    5    7
    """
    return float(a) + float(b)


def get_test_data_from_csv(filepath):
    """Custom keyword: reads a CSV file of test data and returns it as a
    list of dictionaries (one dict per row), for data-driven tests.

    Usage in a .robot file:
        ${data}=    Get Test Data From Csv    testdata/login_data.csv
        FOR    ${row}    IN    @{data}
            Log    ${row}[email]
        END
    """
    # Resolve the path relative to the project root (one level up from
    # this libraries/ folder), so it works regardless of where `robot`
    # is invoked from.
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(project_root, filepath)

    with open(full_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
