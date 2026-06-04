# Review 15 — File I/O, OOP & Advanced Python
# ==============================================
import json
import functools


def retry(times: int):
    """
    Decorator factory: retry the decorated function up to `times` times if it
    raises an exception. After all retries are exhausted, re-raise the last exception.
    """
    # TODO: implement
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            pass  # TODO
        return wrapper
    return decorator


def read_json_safe(filepath: str, default=None):
    """
    Load and return JSON from filepath. If the file does not exist or JSON is
    invalid, return `default` instead of raising.
    """
    # TODO: implement
    return default


class Serialisable:
    """Mixin that adds to_dict() and from_dict() class method."""

    def to_dict(self) -> dict:
        """Return the instance's __dict__ as a plain dict."""
        # TODO: implement
        return {}

    @classmethod
    def from_dict(cls, data: dict):
        """Create an instance from a dict. Use **data to pass kwargs."""
        # TODO: implement
        return cls(**data)


class Product(Serialisable):
    """Simple product class used to test Serialisable."""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


def pipeline(data: list, *funcs):
    """
    Apply each function in funcs to data sequentially, passing the result of
    one function as the input to the next.
    Example: pipeline([1,2,3], lambda x: [i*2 for i in x], sum) → 12
    """
    # TODO: implement
    return data
