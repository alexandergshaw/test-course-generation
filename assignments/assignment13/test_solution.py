"""Tests for Assignment 13 — Inheritance & Polymorphism."""
import unittest
import solution


class TestRecurringTask(unittest.TestCase):
    def test_inherits_task(self):
        t = solution.RecurringTask("Exercise", 30, "daily")
        self.assertIsInstance(t, solution.Task)

    def test_frequency_stored(self):
        t = solution.RecurringTask("Exercise", 30, "daily")
        self.assertEqual(t.frequency, "daily")

    def test_default_status(self):
        t = solution.RecurringTask("Exercise", 30, "daily")
        self.assertEqual(t.status, "pending")

    def test_str_contains_recurring(self):
        t = solution.RecurringTask("Exercise", 30, "daily")
        self.assertIn("recurring", str(t))
        self.assertIn("daily", str(t))

    def test_complete_inherited(self):
        t = solution.RecurringTask("Exercise", 30, "daily")
        t.complete()
        self.assertEqual(t.status, "completed")


class TestPriorityTask(unittest.TestCase):
    def test_inherits_task(self):
        t = solution.PriorityTask("Urgent report", 60, 9)
        self.assertIsInstance(t, solution.Task)

    def test_priority_stored(self):
        t = solution.PriorityTask("Urgent report", 60, 9)
        self.assertEqual(t.priority, 9)

    def test_complete_sets_status(self):
        t = solution.PriorityTask("Urgent report", 60, 9)
        t.complete()
        self.assertEqual(t.status, "completed")

    def test_complete_sets_completed_at(self):
        t = solution.PriorityTask("Urgent report", 60, 9)
        t.complete()
        self.assertTrue(t.completed_at)

    def test_str_contains_priority(self):
        t = solution.PriorityTask("Urgent report", 60, 9)
        s = str(t)
        self.assertIn("9", s)


if __name__ == "__main__":
    unittest.main()
