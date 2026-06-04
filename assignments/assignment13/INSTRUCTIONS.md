# Assignment 13 — Inheritance & Polymorphism

**Week 13 | Topic: Subclasses, `super()`, Method Overriding, Polymorphism**

Extend the Task Manager with specialised task types that override behaviour.

---

## Learning Goals

- Create a subclass that inherits from a parent class.
- Call `super().__init__()` to reuse parent initialisation.
- Override a method to change its behaviour.
- Use polymorphism to call overridden methods through a common interface.

---

## Instructions

### Step 1 — Open `solution.py`

Open `assignments/assignment13/solution.py`. You will find the base `Task` class (already complete) and two subclass stubs.

---

### Step 2 — Implement `RecurringTask`

- Inherits from `Task`.
- `__init__` takes an extra `frequency` argument (e.g., `'daily'`).
- `__str__` appends `(recurring: daily)` to the parent's string representation.

---

### Step 3 — Implement `PriorityTask`

- Inherits from `Task`.
- `__init__` takes an extra `priority` argument (1-10 integer).
- `complete()` is overridden to also record `self.completed_at = True`.
- `__str__` prepends `[P<priority>]` to the representation.

---

### Step 4 — Save, Test, and Submit

1. Save the file.
2. All tests green ✅.
3. Stage → commit (`assignment13: implement inheritance`) → push → PR.

---

## ✅ Completion Checklist

- [ ] `RecurringTask` correctly extends `Task`.
- [ ] `PriorityTask` correctly overrides `complete` and `__str__`.
- [ ] All tests pass.
- [ ] PR submitted on GitHub.
- [ ] Dashboard card for Assignment 13 shows ✅.
