"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum


def test_two_sum():
    test_cases = [
        # Basic example
        {"elements": [2, 7, 11, 15], "target": 9, "answer": [0, 1]},
        # Different order solution
        {"elements": [3, 2, 4], "target": 6, "answer": [1, 2]},
        # Duplicate numbers (same value twice)
        {"elements": [3, 3], "target": 6, "answer": [0, 1]},
        # Multiple duplicates
        {"elements": [1, 3, 3, 4], "target": 6, "answer": [1, 2]},
        # Negative numbers
        {"elements": [-1, -2, -3, -4, -5], "target": -8, "answer": [2, 4]},  # -3 + -5
        # Mix of positive and negative
        {"elements": [-10, 20, 10, -20], "target": 0, "answer": [0, 2]},
        # Contains zero
        {"elements": [0, 4, 3, 0], "target": 0, "answer": [0, 3]},
        # Minimal valid input
        {"elements": [1, 2], "target": 3, "answer": [0, 1]},
        # Large numbers
        {"elements": [1000000, 500000, 500000], "target": 1000000, "answer": [1, 2]},
        # No solution (defensive test)
        {"elements": [1, 2, 3], "target": 10, "answer": []},
    ]

    for test_case in test_cases:
        assert (
            two_sum(test_case["elements"], test_case["target"]) == test_case["answer"]
        )


if __name__ == "__main__":
    pytest.main()
