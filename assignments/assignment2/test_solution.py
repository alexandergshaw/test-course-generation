"""Tests for Assignment 2 — Calculator."""
import unittest
import solution


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertAlmostEqual(solution.add(3, 4), 7)

    def test_add_floats(self):
        self.assertAlmostEqual(solution.add(1.5, 2.5), 4.0)

    def test_subtract(self):
        self.assertAlmostEqual(solution.subtract(10, 3), 7)

    def test_subtract_negative(self):
        self.assertAlmostEqual(solution.subtract(3, 10), -7)

    def test_multiply(self):
        self.assertAlmostEqual(solution.multiply(4, 5), 20)

    def test_multiply_by_zero(self):
        self.assertAlmostEqual(solution.multiply(99, 0), 0)

    def test_divide(self):
        self.assertAlmostEqual(solution.divide(10, 2), 5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            solution.divide(5, 0)


if __name__ == "__main__":
    unittest.main()
