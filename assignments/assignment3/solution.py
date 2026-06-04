# Assignment 3 — Decision Logic
# ==============================
# Implement each function using if/elif/else statements.


def classify_score(score: int) -> str:
    """
    Classify an integer score (0-100) into a letter grade.
    90-100 → 'A', 80-89 → 'B', 70-79 → 'C', 60-69 → 'D', below 60 → 'F'.
    """
    # TODO: implement
    return ""


def is_productive_day(tasks_completed: int, target: int) -> bool:
    """Return True if tasks_completed >= target, False otherwise."""
    # TODO: implement
    return False


def prioritise_task(urgency: int, importance: int) -> str:
    """
    Return a priority label based on Eisenhower matrix rules.
    urgency >= 7 and importance >= 7 → 'Do First'
    urgency < 7 and importance >= 7 → 'Schedule'
    urgency >= 7 and importance < 7 → 'Delegate'
    otherwise                        → 'Eliminate'
    (urgency and importance are integers 1-10)
    """
    # TODO: implement
    return ""
