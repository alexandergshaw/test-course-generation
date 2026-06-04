"""Assignment 1 solution: basic calculator logic for the dashboard."""


def calculate_total_time(task_minutes: list[int]) -> int:
    """Return the total focused minutes from a list of task durations."""
    return sum(task_minutes)


def check_assignment_completion() -> bool:
    """Predefined completion check used by dashboard unlock logic."""
    return calculate_total_time([25, 30, 45]) == 100
