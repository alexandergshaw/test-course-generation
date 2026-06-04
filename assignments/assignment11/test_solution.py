"""Tests for Assignment 11 — File I/O."""
import os
import tempfile
import unittest
import solution

TASKS = [
    {"name": "Report",   "status": "completed", "duration": "60"},
    {"name": "Exercise", "status": "pending",   "duration": "45"},
]


class TestFileIO(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()

    def _path(self, filename):
        return os.path.join(self.tmp_dir, filename)

    def test_csv_roundtrip(self):
        path = self._path("tasks.csv")
        solution.write_tasks_to_csv(TASKS, path)
        self.assertTrue(os.path.isfile(path))
        loaded = solution.read_tasks_from_csv(path)
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0]["name"], "Report")
        self.assertEqual(loaded[1]["status"], "pending")

    def test_csv_has_header(self):
        path = self._path("tasks_header.csv")
        solution.write_tasks_to_csv(TASKS, path)
        with open(path) as f:
            first_line = f.readline().strip()
        for key in TASKS[0].keys():
            self.assertIn(key, first_line)

    def test_json_roundtrip(self):
        path = self._path("tasks.json")
        solution.save_tasks_to_json(TASKS, path)
        self.assertTrue(os.path.isfile(path))
        loaded = solution.load_tasks_from_json(path)
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0]["name"], "Report")

    def test_json_is_valid(self):
        import json
        path = self._path("tasks_valid.json")
        solution.save_tasks_to_json(TASKS, path)
        with open(path) as f:
            data = json.load(f)
        self.assertIsInstance(data, list)


if __name__ == "__main__":
    unittest.main()
