# Assignment 12 — OOP Classes
# =============================


class Task:
    """Represents a single productivity task."""

    def __init__(self, name: str, duration: float, status: str = "pending"):
        # TODO: store name, duration, status as instance variables
        pass

    def complete(self) -> None:
        """Mark this task as completed."""
        # TODO: implement
        pass

    def __str__(self) -> str:
        """Return a string like '[completed] Report (60 min)'."""
        # TODO: implement
        return ""


class TaskManager:
    """Manages a collection of Task objects."""

    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task) -> None:
        """Add a Task to the internal list."""
        # TODO: implement
        pass

    def get_completed(self) -> list:
        """Return a list of all completed tasks."""
        # TODO: implement
        return []

    def total_duration(self) -> float:
        """Return the total duration of all tasks."""
        # TODO: implement
        return 0.0

    def summary(self) -> str:
        """Return a summary string like '3/5 tasks completed (200 min total)'."""
        # TODO: implement
        return ""
