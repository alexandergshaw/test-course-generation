# Assignment 12 — OOP Classes

**Week 12 | Topic: Classes, `__init__`, Instance Methods, `__str__`**

Model the Task Manager as a Python class to encapsulate data and behaviour.

---

## Learning Goals

- Define a class with `__init__` and instance variables.
- Write instance methods that read and modify `self`.
- Implement `__str__` for a human-readable representation.
- Understand the difference between class and instance variables.

---

## Instructions

### Step 1 — Open `solution.py`

Open `assignments/assignment12/solution.py`. You will find a `Task` class and a `TaskManager` class with stubs.

---

### Step 2 — Implement the `Task` Class

- `__init__(self, name, duration, status='pending')` — store as instance variables.
- `complete(self)` — set `self.status` to `'completed'`.
- `__str__(self)` — return `"[completed] Report (60 min)"` style string.

---

### Step 3 — Implement the `TaskManager` Class

- `add_task(self, task)` — append to `self.tasks`.
- `get_completed(self)` — return a filtered list.
- `total_duration(self)` — return sum of durations.
- `summary(self)` — return a string like `"3/5 tasks completed (200 min total)"`.

---

### Step 4 — Save, Test, and Submit

1. Save the file.
2. All tests green ✅.
3. Stage → commit (`assignment12: implement OOP classes`) → push → PR.

---

## ✅ Completion Checklist

- [ ] `Task` class fully implemented.
- [ ] `TaskManager` class fully implemented.
- [ ] All tests pass.
- [ ] PR submitted on GitHub.
- [ ] Dashboard card for Assignment 12 shows ✅.
