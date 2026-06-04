# Assignment 1 — Hello World: Display User Stats

**Week 1 | Topic: Variables, Strings & Basic Output**

In this assignment you will write your first Python functions and see the results appear on the **Personal Productivity Tracker** dashboard.

---

## Learning Goals

- Declare string variables.
- Use f-strings (or string concatenation) to build messages.
- Write and call a simple Python function.

---

## Background

The dashboard displays a personalised greeting card at the top of the page. Your job is to write the two functions that power it.

---

## Instructions

### Step 1 — Open `solution.py`

In the **Explorer** panel, open `assignments/assignment1/solution.py`.

You will see two stubbed-out functions:

```python
def get_greeting(name: str) -> str:
    ...

def get_welcome_message(name: str, course: str) -> str:
    ...
```

---

### Step 2 — Implement `get_greeting`

Replace the `return ""` stub so that the function returns a string in this exact format:

```
Hello, <name>!
```

**Example:** `get_greeting("Ada Lovelace")` → `"Hello, Ada Lovelace!"`

> 💡 **Hint:** Use an f-string: `f"Hello, {name}!"`

---

### Step 3 — Implement `get_welcome_message`

Replace the `return ""` stub so that the function returns a message that contains both the student's `name` **and** the `course` name.

**Example:** `get_welcome_message("Ada", "Python Foundations")` → `"Welcome to Python Foundations, Ada!"`

---

### Step 4 — Save the file

Press **Ctrl+S** (Windows/Linux) or **Cmd+S** (Mac).

---

### Step 5 — Run the Tests

1. Open the **Testing** panel (🧪 icon in the Activity Bar).
2. Click **▶ Run All Tests**.
3. Verify that all tests under `assignment1` show a green ✅.

If any test shows a red ❌, re-read the error message and adjust your code.

---

### Step 6 — Commit, Push & Open a Pull Request

1. Open the **Source Control** panel (🔀 icon).
2. Stage `solution.py` by clicking the **`+`** next to it.
3. Type a commit message: `assignment1: implement hello world functions`
4. Press **Ctrl+Enter** / **Cmd+Enter** to commit.
5. Click **Sync Changes** to push.
6. Go to GitHub, click **"Compare & pull request"**, and submit your PR.

---

## ✅ Completion Checklist

- [ ] `get_greeting` returns `"Hello, <name>!"`.
- [ ] `get_welcome_message` returns a string containing both `name` and `course`.
- [ ] All tests pass (green ✅ in Testing panel).
- [ ] PR submitted on GitHub.
- [ ] Dashboard card for Assignment 1 shows ✅.
