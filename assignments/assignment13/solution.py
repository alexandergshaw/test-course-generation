# Assignment 13 — Inheritance & Polymorphism
# ============================================


class Task:
    """Base Task class (do not modify)."""

    def __init__(self, name: str, duration: float, status: str = "pending"):
        self.name = name
        self.duration = duration
        self.status = status

    def complete(self) -> None:
        self.status = "completed"

    def __str__(self) -> str:
        return f"[{self.status}] {self.name} ({self.duration} min)"


class RecurringTask(Task):
    """A task that repeats at a given frequency (e.g., 'daily', 'weekly')."""

    def __init__(self, name: str, duration: float, frequency: str, status: str = "pending"):
        # TODO: call super().__init__ and store frequency
        pass

    def __str__(self) -> str:
        """Append '(recurring: <frequency>)' to the parent string."""
        # TODO: implement
        return ""


class PriorityTask(Task):
    """A high-priority task with a numeric priority level (1-10)."""

    def __init__(self, name: str, duration: float, priority: int, status: str = "pending"):
        # TODO: call super().__init__ and store priority; set completed_at = False
        pass

    def complete(self) -> None:
        """Mark complete and set self.completed_at = True."""
        # TODO: call super().complete() and set completed_at
        pass

    def __str__(self) -> str:
        """Prepend '[P<priority>]' to the representation."""
        # TODO: implement
        return ""
