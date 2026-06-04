"""Tests for Review 4 — Fundamentals & Control Flow."""
import unittest
import solution


class TestReview4(unittest.TestCase):
    def test_celsius_to_fahrenheit_boiling(self):
        self.assertAlmostEqual(solution.celsius_to_fahrenheit(100), 212.0)

    def test_celsius_to_fahrenheit_freezing(self):
        self.assertAlmostEqual(solution.celsius_to_fahrenheit(0), 32.0)

    def test_count_vowels(self):
        self.assertEqual(solution.count_vowels("Hello World"), 3)

    def test_count_vowels_empty(self):
        self.assertEqual(solution.count_vowels(""), 0)

    def test_count_vowels_case_insensitive(self):
        self.assertEqual(solution.count_vowels("AEIOU"), 5)

    def test_bmi_underweight(self):
        self.assertEqual(solution.bmi_category(17.0), "Underweight")

    def test_bmi_normal(self):
        self.assertEqual(solution.bmi_category(22.0), "Normal")

    def test_bmi_overweight(self):
        self.assertEqual(solution.bmi_category(27.0), "Overweight")

    def test_bmi_obese(self):
        self.assertEqual(solution.bmi_category(35.0), "Obese")

    def test_clamp_within(self):
        self.assertAlmostEqual(solution.clamp(5, 0, 10), 5)

    def test_clamp_below(self):
        self.assertAlmostEqual(solution.clamp(-5, 0, 10), 0)

    def test_clamp_above(self):
        self.assertAlmostEqual(solution.clamp(15, 0, 10), 10)

    def test_format_task_summary(self):
        result = solution.format_task_summary(7, 10)
        self.assertIn("7", result)
        self.assertIn("10", result)
        self.assertIn("70.0", result)


if __name__ == "__main__":
    unittest.main()
