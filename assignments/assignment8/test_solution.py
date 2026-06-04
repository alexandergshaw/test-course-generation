"""Tests for Assignment 8 — Data Structures."""
import unittest
import solution

TASKS = [
    {"name": "Report",   "status": "completed", "category": "work",     "duration": 60},
    {"name": "Email",    "status": "pending",   "category": "work",     "duration": 5},
    {"name": "Exercise", "status": "completed", "category": "personal", "duration": 45},
    {"name": "Reading",  "status": "pending",   "category": "personal", "duration": 30},
    {"name": "Meeting",  "status": "completed", "category": "work",     "duration": 90},
]


class TestDataStructures(unittest.TestCase):
    def test_filter_by_status_completed(self):
        result = solution.filter_by_status(TASKS, "completed")
        self.assertEqual(len(result), 3)

    def test_filter_by_status_pending(self):
        result = solution.filter_by_status(TASKS, "pending")
        self.assertEqual(len(result), 2)

    def test_filter_by_status_empty(self):
        self.assertEqual(solution.filter_by_status(TASKS, "cancelled"), [])

    def test_group_by_category_keys(self):
        result = solution.group_by_category(TASKS)
        self.assertIn("work", result)
        self.assertIn("personal", result)

    def test_group_by_category_counts(self):
        result = solution.group_by_category(TASKS)
        self.assertEqual(len(result["work"]), 3)
        self.assertEqual(len(result["personal"]), 2)

    def test_unique_categories(self):
        result = solution.unique_categories(TASKS)
        self.assertEqual(result, {"work", "personal"})

    def test_top_n_tasks(self):
        result = solution.top_n_tasks(TASKS, 2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], "Meeting")

    def test_top_n_tasks_exceeds_length(self):
        result = solution.top_n_tasks(TASKS, 100)
        self.assertEqual(len(result), len(TASKS))


if __name__ == "__main__":
    unittest.main()
