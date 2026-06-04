# Assignment 2 — Calculator: Arithmetic Utilities

**Week 2 | Topic: Operators, Data Types & Error Handling**

You will build a small calculator module that powers the numeric sections of the Productivity Tracker dashboard (e.g., computing completion percentages).

---

## Learning Goals

- Use Python's arithmetic operators (`+`, `-`, `*`, `/`).
- Return values from functions.
- Raise a `ValueError` to handle invalid input.

---

## Instructions

### Step 1 — Open `solution.py`

In the **Explorer** panel, open `assignments/assignment2/solution.py`.

You will see four stubbed functions: `add`, `subtract`, `multiply`, and `divide`.

---

### Step 2 — Implement `add`

Return the sum of `a` and `b`.

```python
def add(a: float, b: float) -> float:
    return a + b
```

---

### Step 3 — Implement `subtract`

Return `a` minus `b`.

---

### Step 4 — Implement `multiply`

Return the product of `a` and `b`.

---

### Step 5 — Implement `divide`

Return `a` divided by `b`. If `b` is zero, **raise** a `ValueError`:

```python
if b == 0:
    raise ValueError("Cannot divide by zero.")
return a / b
```

---

### Step 6 — Save, Test, and Submit

1. Save the file (**Ctrl+S** / **Cmd+S**).
2. Open the **Testing** panel and click **▶ Run All Tests**.
3. All 8 tests should be green ✅.
4. Stage → commit (`assignment2: implement calculator`) → push → open PR.

---

## ✅ Completion Checklist

- [ ] `add`, `subtract`, `multiply`, `divide` all return the correct value.
- [ ] `divide(5, 0)` raises `ValueError`.
- [ ] All tests pass.
- [ ] PR submitted on GitHub.
- [ ] Dashboard card for Assignment 2 shows ✅.
