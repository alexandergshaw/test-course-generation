# Python Foundations: Building a Personal Data Management Dashboard

Welcome to **Python Foundations**! In this course you will learn Python programming by building a **Personal Productivity Tracker** — a real web dashboard that persists data, visualises task completion, and grows more powerful as you complete each assignment.

---

## 📅 Course Schedule & Exam Dates

| Week | Folder | Topic | Type |
|------|--------|-------|------|
| 0 | `assignments/assignment0` | Onboarding & Setup | Setup |
| 1 | `assignments/assignment1` | Hello World — Display User Stats | Assignment |
| 2 | `assignments/assignment2` | Calculator — Arithmetic Utilities | Assignment |
| 3 | `assignments/assignment3` | Decision Logic — Conditional Rendering | Assignment |
| **4** | `assignments/review4` | **Review: Fundamentals & Control Flow** | **Review** |
| **5** | `assignments/exam5` | **Test 1 Practice** *(Exam Week)* | **Exam** |
| 6 | `assignments/assignment6` | Loops — Task Iteration | Assignment |
| 7 | `assignments/assignment7` | Functions — Reusable Helpers | Assignment |
| 8 | `assignments/assignment8` | Data Structures — Lists & Dicts | Assignment |
| **9** | `assignments/review9` | **Review: Loops, Functions & Data Structures** | **Review** |
| **10** | `assignments/exam10` | **Test 2 Practice** *(Exam Week)* | **Exam** |
| 11 | `assignments/assignment11` | File I/O — Persist Task Data | Assignment |
| 12 | `assignments/assignment12` | OOP Classes — Task Manager Class | Assignment |
| 13 | `assignments/assignment13` | Inheritance & Polymorphism | Assignment |
| 14 | `assignments/assignment14` | Advanced Features — Decorators & Generators | Assignment |
| **15** | `assignments/review15` | **Review: File I/O, OOP & Advanced** | **Review** |
| **16** | `assignments/exam16` | **Final Exam Practice** *(Exam Week)* | **Exam** |

---

## 🗓️ Key Exam Dates

| Exam | Week | Topics Covered |
|------|------|----------------|
| **Test 1** | Week 5 | Variables, data types, operators, conditionals, basic I/O |
| **Test 2** | Week 10 | Loops (`for`/`while`), functions, lists, dictionaries, tuples |
| **Final Exam** | Week 16 | File I/O, OOP (classes, inheritance, polymorphism), decorators, generators, comprehensive project |

---

## 🚀 Getting Started

1. Open this repository in **GitHub Codespaces** (click the green **Code** button → **Codespaces** tab → **Create codespace**).
2. Follow the instructions in `assignments/assignment0/INSTRUCTIONS.md` — this walks you through a complete onboarding with no terminal commands required.
3. After completing each assignment, the corresponding card in the **Dashboard** (`/dashboard`) unlocks automatically.

---

## 🏗️ Project Structure

```
/
├── app/                    # Next.js App Router pages
│   ├── layout.tsx
│   ├── page.tsx
│   ├── dashboard/
│   │   └── page.tsx        # Main student dashboard
│   └── api/
│       └── check-assignment/
│           └── route.ts    # API route: runs Python tests & returns status
├── lib/
│   └── assignment_loader.py  # Dynamically imports & verifies student solutions
├── assignments/
│   ├── assignment0/        # Onboarding
│   ├── assignment1/        # Hello World
│   ├── assignment2/        # Calculator
│   ├── assignment3/        # Decision Logic
│   ├── review4/            # Review week
│   ├── exam5/              # Exam week
│   ├── assignment6/        # Loops
│   ├── assignment7/        # Functions
│   ├── assignment8/        # Data Structures
│   ├── review9/            # Review week
│   ├── exam10/             # Exam week
│   ├── assignment11/       # File I/O
│   ├── assignment12/       # OOP Classes
│   ├── assignment13/       # Inheritance & Polymorphism
│   ├── assignment14/       # Advanced Features
│   ├── review15/           # Review week
│   └── exam16/             # Final Exam
├── package.json
├── next.config.js
└── README.md
```

---

## 🧪 How Assignments Are Graded

Each assignment folder contains:

- **`INSTRUCTIONS.md`** — step-by-step guide (no terminal commands).
- **`solution.py`** — the file you edit with your code.
- **`test_solution.py`** — unit tests that verify your solution.

When your tests pass, the matching card in the dashboard unlocks. You can see your overall progress at any time by opening the **Dashboard** page in the running Next.js preview.

---

## 📦 Deployment

This project is pre-configured for **zero-configuration deployment on Vercel**. Push to `main` and Vercel will automatically build and deploy.

---

## 🙋 Need Help?

- Open a **GitHub Discussion** in this repository.
- Ask your instructor by opening a **GitHub Issue** tagged `question`.
