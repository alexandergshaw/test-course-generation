# Assignment 11 — File I/O
# ==========================
import csv
import json


def write_tasks_to_csv(tasks: list, filepath: str) -> None:
    """
    Write a list of task dicts to a CSV file at filepath.
    The CSV must include a header row with the dict keys.
    """
    # TODO: implement
    pass


def read_tasks_from_csv(filepath: str) -> list:
    """
    Read a CSV file created by write_tasks_to_csv and return a list of dicts.
    """
    # TODO: implement
    return []


def save_tasks_to_json(tasks: list, filepath: str) -> None:
    """
    Serialise the tasks list to a JSON file at filepath (pretty-printed, indent=2).
    """
    # TODO: implement
    pass


def load_tasks_from_json(filepath: str) -> list:
    """
    Load and return the list of tasks from a JSON file created by save_tasks_to_json.
    """
    # TODO: implement
    return []
