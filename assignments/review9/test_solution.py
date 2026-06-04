"""Tests for Review 9 — Loops, Functions & Data Structures."""
import unittest
import solution


class TestReview9(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(solution.flatten([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_flatten_empty(self):
        self.assertEqual(solution.flatten([]), [])

    def test_word_frequency(self):
        self.assertEqual(solution.word_frequency("hi hi there"), {"hi": 2, "there": 1})

    def test_word_frequency_empty(self):
        self.assertEqual(solution.word_frequency(""), {})

    def test_running_total(self):
        self.assertEqual(solution.running_total([1, 2, 3]), [1, 3, 6])

    def test_running_total_single(self):
        self.assertEqual(solution.running_total([5]), [5])

    def test_merge_dicts_no_overlap(self):
        self.assertEqual(solution.merge_dicts({"a": 1}, {"b": 2}), {"a": 1, "b": 2})

    def test_merge_dicts_d2_wins(self):
        result = solution.merge_dicts({"a": 1}, {"a": 99})
        self.assertEqual(result["a"], 99)

    def test_deduplicate(self):
        self.assertEqual(solution.deduplicate([3, 1, 2, 1, 3]), [3, 1, 2])

    def test_deduplicate_empty(self):
        self.assertEqual(solution.deduplicate([]), [])


if __name__ == "__main__":
    unittest.main()
