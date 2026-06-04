# Assignment 3 — Decision Logic: Conditional Rendering

**Week 3 | Topic: if / elif / else, Comparison Operators**

You will write functions that evaluate conditions and return labels, feeding the dashboard's colour-coded priority cards.

---

## Learning Goals

- Write multi-branch `if / elif / else` statements.
- Compare values using `>=`, `<`, `and`.
- Return meaningful string labels from functions.

---

## Instructions

### Step 1 — Open `solution.py`

Open `assignments/assignment3/solution.py` in the Explorer panel.

You will see three stub functions.

---

### Step 2 — Implement `classify_score`

Map an integer score to a letter grade:

| Range | Grade |
|-------|-------|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| 0–59 | F |

Use an `if / elif / else` chain.

---

### Step 3 — Implement `is_productive_day`

Return `True` if `tasks_completed >= target`, otherwise `False`.

---

### Step 4 — Implement `prioritise_task`

Use the Eisenhower Matrix rules described in the docstring:

| Urgency ≥ 7? | Importance ≥ 7? | Label |
|---|---|---|
| Yes | Yes | Do First |
| No | Yes | Schedule |
| Yes | No | Delegate |
| No | No | Eliminate |

---

### Step 5 — Save, Test, and Submit

1. Save the file.
2. Run all tests in the **Testing** panel — all 11 tests should be green ✅.
3. Stage → commit (`assignment3: implement decision logic`) → push → open PR.

---

## ✅ Completion Checklist

- [ ] `classify_score` returns the correct letter for each range.
- [ ] `is_productive_day` returns the correct boolean.
- [ ] `prioritise_task` returns the correct Eisenhower label.
- [ ] All tests pass.
- [ ] PR submitted on GitHub.
- [ ] Dashboard card for Assignment 3 shows ✅.
