import unittest

from solution import check_assignment_completion


class AssignmentTests(unittest.TestCase):
    def test_completion_check(self):
        self.assertTrue(
            check_assignment_completion(),
            "Complete the assignment requirements before marking as finished.",
        )


if __name__ == "__main__":
    unittest.main()
