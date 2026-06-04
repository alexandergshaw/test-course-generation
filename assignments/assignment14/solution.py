# Assignment 14 — Advanced Features
# ====================================
import functools


def log_call(func):
    """
    Decorator that prints 'Calling <function_name>' before calling the function,
    then returns the function's result unchanged.
    """
    # TODO: implement using functools.wraps
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pass  # TODO: print message and call func
    return wrapper


def task_generator(tasks: list):
    """
    Generator that yields one task dict at a time from the tasks list.
    Use the 'yield' keyword.
    """
    # TODO: implement
    pass


def completed_names(tasks: list) -> list:
    """
    Return a list of the 'name' field for every task with status == 'completed'.
    Use a list comprehension.
    """
    # TODO: implement as a one-liner list comprehension
    return []


def duration_map(tasks: list) -> dict:
    """
    Return a dict mapping each task's 'name' to its 'duration'.
    Use a dict comprehension.
    """
    # TODO: implement as a one-liner dict comprehension
    return {}
