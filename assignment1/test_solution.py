import unittest

from solution import calculate_total_time, check_assignment_completion


class Assignment1Tests(unittest.TestCase):
    def test_calculate_total_time(self):
        self.assertEqual(calculate_total_time([10, 20, 30]), 60)

    def test_completion_check(self):
        self.assertTrue(check_assignment_completion())


if __name__ == "__main__":
    unittest.main()
