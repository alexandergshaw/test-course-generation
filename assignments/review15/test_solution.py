"""Tests for Review 15 — File I/O, OOP & Advanced Python."""
import json
import os
import tempfile
import unittest
import solution


class TestRetryDecorator(unittest.TestCase):
    def test_succeeds_first_try(self):
        calls = []

        @solution.retry(3)
        def ok():
            calls.append(1)
            return "done"

        self.assertEqual(ok(), "done")
        self.assertEqual(len(calls), 1)

    def test_retries_on_exception(self):
        calls = []

        @solution.retry(3)
        def flaky():
            calls.append(1)
            if len(calls) < 3:
                raise ValueError("not yet")
            return "ok"

        result = flaky()
        self.assertEqual(result, "ok")
        self.assertEqual(len(calls), 3)

    def test_raises_after_exhausted(self):
        @solution.retry(2)
        def always_fails():
            raise RuntimeError("fail")

        with self.assertRaises(RuntimeError):
            always_fails()


class TestReadJsonSafe(unittest.TestCase):
    def test_valid_json(self):
        tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
        json.dump({"key": "value"}, tmp)
        tmp.close()
        result = solution.read_json_safe(tmp.name)
        os.unlink(tmp.name)
        self.assertEqual(result, {"key": "value"})

    def test_missing_file_returns_default(self):
        result = solution.read_json_safe("/nonexistent/path.json", default=[])
        self.assertEqual(result, [])


class TestSerialisable(unittest.TestCase):
    def test_to_dict(self):
        p = solution.Product("Widget", 9.99)
        d = p.to_dict()
        self.assertEqual(d["name"], "Widget")
        self.assertAlmostEqual(d["price"], 9.99)

    def test_from_dict(self):
        p = solution.Product.from_dict({"name": "Gadget", "price": 4.99})
        self.assertEqual(p.name, "Gadget")


class TestPipeline(unittest.TestCase):
    def test_single_function(self):
        result = solution.pipeline([1, 2, 3], sum)
        self.assertEqual(result, 6)

    def test_multiple_functions(self):
        result = solution.pipeline([1, 2, 3], lambda x: [i * 2 for i in x], sum)
        self.assertEqual(result, 12)


if __name__ == "__main__":
    unittest.main()
