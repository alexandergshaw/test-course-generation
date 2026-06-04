"""Tests for Exam 10 — Test 2 Practice."""
import unittest
import solution


class TestExam10(unittest.TestCase):
    def test_squares_up_to(self):
        self.assertEqual(solution.squares_up_to(5), [1, 4, 9, 16, 25])

    def test_squares_up_to_one(self):
        self.assertEqual(solution.squares_up_to(1), [1])

    def test_count_above_average(self):
        self.assertEqual(solution.count_above_average([1, 2, 3, 4, 5]), 2)

    def test_count_above_average_all_same(self):
        self.assertEqual(solution.count_above_average([5, 5, 5]), 0)

    def test_invert_dict(self):
        self.assertEqual(solution.invert_dict({"a": 1, "b": 2}), {1: "a", 2: "b"})

    def test_invert_dict_empty(self):
        self.assertEqual(solution.invert_dict({}), {})

    def test_longest_word(self):
        self.assertEqual(solution.longest_word("I love Python programming"), "programming")

    def test_longest_word_single(self):
        self.assertEqual(solution.longest_word("hello"), "hello")

    def test_two_sum_found(self):
        self.assertEqual(solution.two_sum([2, 7, 11, 15], 9), (0, 1))

    def test_two_sum_not_found(self):
        self.assertEqual(solution.two_sum([1, 2, 3], 100), (-1, -1))


if __name__ == "__main__":
    unittest.main()
