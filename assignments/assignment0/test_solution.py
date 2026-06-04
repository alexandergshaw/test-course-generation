"""Tests for Assignment 0 — Onboarding."""
import unittest
import solution


class TestOnboarding(unittest.TestCase):
    def test_student_name_is_set(self):
        """student_name must not be the placeholder."""
        self.assertNotEqual(
            solution.student_name.strip(),
            "Your Name Here",
            "Replace 'Your Name Here' with your actual name in solution.py.",
        )

    def test_student_name_is_non_empty(self):
        """student_name must be a non-empty string."""
        self.assertIsInstance(solution.student_name, str)
        self.assertGreater(
            len(solution.student_name.strip()),
            0,
            "student_name must not be empty.",
        )

    def test_student_name_has_two_parts(self):
        """student_name should contain at least a first and last name."""
        parts = solution.student_name.strip().split()
        self.assertGreaterEqual(
            len(parts),
            2,
            "Please enter both your first and last name.",
        )


if __name__ == "__main__":
    unittest.main()
