"""Tests for Assignment 7 — Functions."""
import unittest
import solution


class TestFunctions(unittest.TestCase):
    def test_completion_rate_normal(self):
        self.assertAlmostEqual(solution.completion_rate(7, 10), 70.0)

    def test_completion_rate_zero_total(self):
        self.assertAlmostEqual(solution.completion_rate(0, 0), 0.0)

    def test_completion_rate_full(self):
        self.assertAlmostEqual(solution.completion_rate(5, 5), 100.0)

    def test_task_summary_contains_name(self):
        result = solution.task_summary("Alice", 7, 10)
        self.assertIn("Alice", result)

    def test_task_summary_contains_rate(self):
        result = solution.task_summary("Alice", 7, 10)
        self.assertIn("70.0", result)

    def test_task_summary_custom_goal(self):
        result = solution.task_summary("Bob", 5, 10, goal=8)
        self.assertIn("8", result)

    def test_min_max(self):
        self.assertEqual(solution.min_max([3, 1, 4, 1, 5]), (1, 5))

    def test_min_max_single(self):
        self.assertEqual(solution.min_max([7]), (7, 7))

    def test_apply_bonus_default(self):
        self.assertAlmostEqual(solution.apply_bonus(80.0), 80.0)

    def test_apply_bonus_multiplier(self):
        self.assertAlmostEqual(solution.apply_bonus(80.0, 1.5), 120.0)


if __name__ == "__main__":
    unittest.main()
