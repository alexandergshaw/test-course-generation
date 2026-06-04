"""Tests for Exam 5 — Test 1 Practice."""
import unittest
import solution


class TestExam5(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(solution.reverse_string("hello"), "olleh")

    def test_reverse_string_empty(self):
        self.assertEqual(solution.reverse_string(""), "")

    def test_is_palindrome_true(self):
        self.assertTrue(solution.is_palindrome("racecar"))

    def test_is_palindrome_false(self):
        self.assertFalse(solution.is_palindrome("hello"))

    def test_is_palindrome_spaces(self):
        self.assertTrue(solution.is_palindrome("A man a plan a canal Panama"))

    def test_fizzbuzz_fizz(self):
        self.assertEqual(solution.fizzbuzz(9), "Fizz")

    def test_fizzbuzz_buzz(self):
        self.assertEqual(solution.fizzbuzz(10), "Buzz")

    def test_fizzbuzz_fizzbuzz(self):
        self.assertEqual(solution.fizzbuzz(15), "FizzBuzz")

    def test_fizzbuzz_number(self):
        self.assertEqual(solution.fizzbuzz(7), "7")

    def test_calculate_average(self):
        self.assertAlmostEqual(solution.calculate_average([1, 2, 3, 4, 5]), 3.0)

    def test_calculate_average_single(self):
        self.assertAlmostEqual(solution.calculate_average([42]), 42.0)

    def test_letter_grade_A(self):
        self.assertEqual(solution.letter_grade(93), "A")

    def test_letter_grade_F(self):
        self.assertEqual(solution.letter_grade(40), "F")


if __name__ == "__main__":
    unittest.main()
