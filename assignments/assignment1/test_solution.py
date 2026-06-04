"""Tests for Assignment 1 — Hello World."""
import unittest
import solution


class TestHelloWorld(unittest.TestCase):
    def test_get_greeting(self):
        self.assertEqual(solution.get_greeting("Ada Lovelace"), "Hello, Ada Lovelace!")

    def test_get_greeting_different_name(self):
        self.assertEqual(solution.get_greeting("Alan Turing"), "Hello, Alan Turing!")

    def test_get_welcome_message(self):
        msg = solution.get_welcome_message("Ada", "Python Foundations")
        self.assertIn("Ada", msg)
        self.assertIn("Python Foundations", msg)

    def test_get_welcome_message_non_empty(self):
        self.assertGreater(len(solution.get_welcome_message("Ada", "Python Foundations")), 0)


if __name__ == "__main__":
    unittest.main()
