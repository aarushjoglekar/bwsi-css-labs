"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
   test_cases = {
        # Given example
        (-2, 1, -3, 4, -1, 2, 1, -5, 4): 6,   # [4, -1, 2, 1]

        # Single element
        (5,): 5,
        (-5,): -5,

        # All positives
        (1, 2, 3, 4): 10,

        # All negatives
        (-1, -2, -3, -4): -1,

        # Zeros
        (0, 0, 0): 0,
        (-1, 0, -2): 0,

        # Mixed small cases
        (1, -1, 1, -1, 1): 1,
        (2, -1, 2, 3, 4, -5): 10,   # [2, -1, 2, 3, 4]
        (-2, -3, 4, -1, -2, 1, 5, -3): 7,  # [4, -1, -2, 1, 5]

        # Entire array is best
        (3, -1, 2): 4,

        # Large negative dip in middle
        (5, 4, -100, 6, 7): 13,

        # Best subarray at end
        (-10, -2, 3, 5): 8,

        # Best subarray at beginning
        (8, -1, -2, -3): 8,

        # Alternating signs
        (1, -2, 3, -2, 5, -3, 2): 6,  # [3, -2, 5]
    }

   for test_case, answer in test_cases.items():
       assert max_subarray_sum(list(test_case)) == answer

if __name__ == "__main__":
    pytest.main()
