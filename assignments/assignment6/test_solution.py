"""Tests for Assignment 6 — Loops."""
import unittest
import solution

TASKS = [
    {"name": "Write report", "status": "completed", "duration": 60.0},
    {"name": "Send email",   "status": "pending",   "duration": 5.0},
    {"name": "Team meeting", "status": "completed", "duration": 45.0},
    {"name": "Code review",  "status": "completed", "duration": 90.0},
]


class TestLoops(unittest.TestCase):
    def test_count_completed(self):
        self.assertEqual(solution.count_completed(TASKS), 3)

    def test_count_completed_none(self):
        self.assertEqual(solution.count_completed([{"status": "pending"}]), 0)

    def test_sum_durations(self):
        self.assertAlmostEqual(solution.sum_durations(TASKS), 200.0)

    def test_sum_durations_empty(self):
        self.assertAlmostEqual(solution.sum_durations([]), 0.0)

    def test_find_longest_task(self):
        result = solution.find_longest_task(TASKS)
        self.assertEqual(result["name"], "Code review")

    def test_find_longest_task_single(self):
        t = [{"name": "Solo", "duration": 10.0}]
        self.assertEqual(solution.find_longest_task(t)["name"], "Solo")

    def test_generate_daily_targets(self):
        self.assertEqual(solution.generate_daily_targets(1, 10, 2), [1, 3, 5, 7, 9])

    def test_generate_daily_targets_step1(self):
        self.assertEqual(solution.generate_daily_targets(1, 4, 1), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
