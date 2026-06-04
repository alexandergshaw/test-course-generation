"""Tests for Exam 16 — Final Exam Practice."""
import json
import os
import tempfile
import unittest
import solution

TASKS = [
    {"name": "Report",   "status": "completed", "duration": 60,  "category": "work"},
    {"name": "Email",    "status": "pending",   "duration": 5,   "category": "work"},
    {"name": "Exercise", "status": "completed", "duration": 45,  "category": "personal"},
    {"name": "Reading",  "status": "pending",   "duration": 30,  "category": "personal"},
    {"name": "Meeting",  "status": "completed", "duration": 90,  "category": "work"},
]


class TestAnalyseTasks(unittest.TestCase):
    def setUp(self):
        self.result = solution.analyse_tasks(TASKS)

    def test_total(self):
        self.assertEqual(self.result["total"], 5)

    def test_completed(self):
        self.assertEqual(self.result["completed"], 3)

    def test_pending(self):
        self.assertEqual(self.result["pending"], 2)

    def test_total_duration(self):
        self.assertAlmostEqual(self.result["total_duration"], 230.0)

    def test_average_duration(self):
        self.assertAlmostEqual(self.result["average_duration"], 46.0)

    def test_by_category(self):
        self.assertEqual(self.result["by_category"]["work"], 3)
        self.assertEqual(self.result["by_category"]["personal"], 2)

    def test_empty(self):
        r = solution.analyse_tasks([])
        self.assertEqual(r["total"], 0)
        self.assertAlmostEqual(r["average_duration"], 0.0)


class TestTaskReport(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False)
        self.tmp.close()

    def tearDown(self):
        if os.path.exists(self.tmp.name):
            os.unlink(self.tmp.name)

    def test_save_and_load(self):
        report = solution.TaskReport(TASKS)
        report.save(self.tmp.name)
        loaded = solution.TaskReport.load(self.tmp.name)
        self.assertEqual(len(loaded.tasks), 5)

    def test_completed_names(self):
        report = solution.TaskReport(TASKS)
        names = report.completed_names()
        self.assertIn("Report", names)
        self.assertNotIn("Email", names)


class TestMemoize(unittest.TestCase):
    def test_caches_result(self):
        calls = []

        @solution.memoize
        def slow_add(a, b):
            calls.append(1)
            return a + b

        self.assertEqual(slow_add(1, 2), 3)
        self.assertEqual(slow_add(1, 2), 3)
        self.assertEqual(len(calls), 1)


class TestFibonacciGen(unittest.TestCase):
    def test_basic(self):
        result = list(solution.fibonacci_gen(20))
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13])

    def test_zero(self):
        result = list(solution.fibonacci_gen(0))
        self.assertEqual(result, [0])


class TestLoadAndFilter(unittest.TestCase):
    def test_filters_correctly(self):
        tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
        json.dump(TASKS, tmp)
        tmp.close()
        result = solution.load_and_filter(tmp.name, "completed")
        os.unlink(tmp.name)
        self.assertEqual(len(result), 3)

    def test_missing_file(self):
        self.assertEqual(solution.load_and_filter("/no/such/file.json", "completed"), [])


class TestFormatReport(unittest.TestCase):
    def test_contains_title(self):
        s = solution.format_report("Weekly Summary", {"total": 10})
        self.assertIn("Weekly Summary", s)

    def test_contains_stats(self):
        s = solution.format_report("Report", {"total": 10, "completed": 7})
        self.assertIn("10", s)
        self.assertIn("7", s)


if __name__ == "__main__":
    unittest.main()
