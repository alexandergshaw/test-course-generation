# Assignment 11 — File I/O: Persist Task Data

**Week 11 | Topic: Reading and Writing Files, CSV, JSON**

Persist the dashboard's task data to disk so it survives between sessions.

---

## Learning Goals

- Open, read, and write text files using `open()`.
- Parse and generate CSV data using the `csv` module.
- Parse and generate JSON data using the `json` module.

---

## Instructions

### Step 1 — Open `solution.py`

Open `assignments/assignment11/solution.py`. You have four stub functions.

---

### Step 2 — Implement Each Function

| Function | Concept |
|---|---|
| `write_tasks_to_csv` | Write a list of dicts to a CSV file |
| `read_tasks_from_csv` | Read a CSV file back into a list of dicts |
| `save_tasks_to_json` | Serialise a list to a JSON file |
| `load_tasks_from_json` | Deserialise a JSON file back to a list |

> 💡 Use `import csv` and `import json` at the top of the file.

---

### Step 3 — Save, Test, and Submit

1. Save the file.
2. Run all tests — all should be green ✅.
3. Stage → commit (`assignment11: implement file i/o`) → push → PR.

---

## ✅ Completion Checklist

- [ ] All four functions implemented correctly.
- [ ] All tests pass.
- [ ] PR submitted on GitHub.
- [ ] Dashboard card for Assignment 11 shows ✅.
