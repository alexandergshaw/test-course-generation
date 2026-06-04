"""Tests for Assignment 3 — Decision Logic."""
import unittest
import solution


class TestDecisionLogic(unittest.TestCase):
    def test_classify_score_A(self):
        self.assertEqual(solution.classify_score(95), "A")

    def test_classify_score_B(self):
        self.assertEqual(solution.classify_score(85), "B")

    def test_classify_score_C(self):
        self.assertEqual(solution.classify_score(75), "C")

    def test_classify_score_D(self):
        self.assertEqual(solution.classify_score(65), "D")

    def test_classify_score_F(self):
        self.assertEqual(solution.classify_score(55), "F")

    def test_is_productive_day_true(self):
        self.assertTrue(solution.is_productive_day(8, 8))

    def test_is_productive_day_false(self):
        self.assertFalse(solution.is_productive_day(3, 8))

    def test_prioritise_do_first(self):
        self.assertEqual(solution.prioritise_task(9, 9), "Do First")

    def test_prioritise_schedule(self):
        self.assertEqual(solution.prioritise_task(4, 9), "Schedule")

    def test_prioritise_delegate(self):
        self.assertEqual(solution.prioritise_task(9, 4), "Delegate")

    def test_prioritise_eliminate(self):
        self.assertEqual(solution.prioritise_task(3, 3), "Eliminate")


if __name__ == "__main__":
    unittest.main()
