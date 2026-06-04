"""Tests for Assignment 14 — Advanced Features."""
import io
import sys
import unittest
import solution

TASKS = [
    {"name": "Report",   "status": "completed", "duration": 60},
    {"name": "Email",    "status": "pending",   "duration": 5},
    {"name": "Meeting",  "status": "completed", "duration": 90},
]


class TestLogCallDecorator(unittest.TestCase):
    def test_output_contains_function_name(self):
        @solution.log_call
        def sample():
            return 42

        captured = io.StringIO()
        sys.stdout = captured
        result = sample()
        sys.stdout = sys.__stdout__
        self.assertIn("sample", captured.getvalue())

    def test_return_value_preserved(self):
        @solution.log_call
        def add(a, b):
            return a + b

        # suppress print
        sys.stdout = io.StringIO()
        result = add(2, 3)
        sys.stdout = sys.__stdout__
        self.assertEqual(result, 5)


class TestTaskGenerator(unittest.TestCase):
    def test_yields_all_tasks(self):
        gen = solution.task_generator(TASKS)
        results = list(gen)
        self.assertEqual(len(results), 3)

    def test_yields_correct_order(self):
        gen = solution.task_generator(TASKS)
        self.assertEqual(next(gen)["name"], "Report")


class TestCompletedNames(unittest.TestCase):
    def test_filters_correctly(self):
        result = solution.completed_names(TASKS)
        self.assertEqual(sorted(result), ["Meeting", "Report"])

    def test_empty_list(self):
        self.assertEqual(solution.completed_names([]), [])


class TestDurationMap(unittest.TestCase):
    def test_keys_are_names(self):
        result = solution.duration_map(TASKS)
        self.assertIn("Report", result)
        self.assertIn("Email", result)

    def test_values_are_durations(self):
        result = solution.duration_map(TASKS)
        self.assertEqual(result["Report"], 60)
        self.assertEqual(result["Meeting"], 90)


if __name__ == "__main__":
    unittest.main()
