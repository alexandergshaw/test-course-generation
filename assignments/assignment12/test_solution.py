"""Tests for Assignment 12 — OOP Classes."""
import unittest
import solution


class TestTask(unittest.TestCase):
    def test_task_init(self):
        t = solution.Task("Report", 60)
        self.assertEqual(t.name, "Report")
        self.assertEqual(t.duration, 60)
        self.assertEqual(t.status, "pending")

    def test_task_complete(self):
        t = solution.Task("Report", 60)
        t.complete()
        self.assertEqual(t.status, "completed")

    def test_task_str_pending(self):
        t = solution.Task("Report", 60)
        s = str(t)
        self.assertIn("pending", s)
        self.assertIn("Report", s)

    def test_task_str_completed(self):
        t = solution.Task("Report", 60)
        t.complete()
        s = str(t)
        self.assertIn("completed", s)


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = solution.TaskManager()
        t1 = solution.Task("Report", 60)
        t1.complete()
        t2 = solution.Task("Email", 5)
        t3 = solution.Task("Meeting", 90)
        t3.complete()
        for t in [t1, t2, t3]:
            self.manager.add_task(t)

    def test_add_task(self):
        self.assertEqual(len(self.manager.tasks), 3)

    def test_get_completed(self):
        self.assertEqual(len(self.manager.get_completed()), 2)

    def test_total_duration(self):
        self.assertAlmostEqual(self.manager.total_duration(), 155.0)

    def test_summary_contains_fractions(self):
        s = self.manager.summary()
        self.assertIn("2", s)
        self.assertIn("3", s)


if __name__ == "__main__":
    unittest.main()
