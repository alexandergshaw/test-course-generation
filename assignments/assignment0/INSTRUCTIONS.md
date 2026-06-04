# Assignment 0 — Onboarding & Setup

Welcome to **Python Foundations: Building a Personal Data Management Dashboard**! 🎉

This assignment has **no coding challenge** — its only goal is to make sure you are comfortable with the tools you will use every week. Follow every step carefully. All actions use the **GitHub Codespaces** graphical interface; you will not need to type any terminal commands.

---

## What You Will Learn

- How to open this repository in GitHub Codespaces.
- How to edit a file using the built-in code editor.
- How to stage and commit changes using the **Source Control** panel.
- How to push your work and open a **Pull Request** on GitHub.
- How to run the unit tests using the **Testing** panel.
- How the **Dashboard** unlocks once your tests pass.

---

## Step-by-Step Instructions

### Step 1 — Open the Repository in GitHub Codespaces

1. Go to the repository page on GitHub (you are probably already there!).
2. Click the green **`< > Code`** button near the top-right of the page.
3. Select the **Codespaces** tab in the dropdown.
4. Click **"Create codespace on main"**.
5. Wait for the Codespace to finish building (this usually takes about 60 seconds). When it is ready, a Visual Studio Code environment opens directly in your browser.

> 💡 **Tip:** You can also open the Codespace in the desktop VS Code app by clicking the three-dot menu (⋯) on the Codespace card and choosing **"Open in Visual Studio Code"**.

---

### Step 2 — Explore the Project Structure

Once the Codespace opens, look at the **Explorer** panel on the left side (it shows the file tree).

Find and expand the following folders:
- 📁 **`assignments/`** — all course assignments live here.
- 📁 **`app/`** — the Next.js dashboard front-end.
- 📁 **`lib/`** — shared Python utilities.

For this assignment you will only work inside `assignments/assignment0/`.

---

### Step 3 — Open Your Solution File

1. In the Explorer panel, click on **`assignments`** → **`assignment0`** → **`solution.py`**.
2. The file opens in the editor. You will see a placeholder comment and a variable called `student_name`.

---

### Step 4 — Edit `solution.py`

1. Find this line in `solution.py`:

   ```python
   student_name = "Your Name Here"
   ```

2. Replace `Your Name Here` with **your actual first and last name**, keeping the quotation marks.  
   Example: `student_name = "Ada Lovelace"`

3. Save the file using **File → Save** from the menu bar, or press `Ctrl+S` (Windows/Linux) / `Cmd+S` (Mac).

---

### Step 5 — Run the Tests Using the Testing Panel

1. Click the **beaker icon** (🧪) in the left Activity Bar to open the **Testing** panel. *(If you don't see it, go to **View → Testing**.)*
2. You should see **`test_solution.py`** listed under `assignment0`.
3. Click the **▶ Run All Tests** button (the play button at the top of the Testing panel).
4. After a few seconds the results appear:
   - ✅ **Green checkmark** = test passed.
   - ❌ **Red X** = test failed — go back to Step 4 and check your `student_name` value.

> 💡 **Tip:** If the Testing panel does not discover any tests, click the **refresh** (↺) icon inside the panel.

---

### Step 6 — Open the Source Control Panel

1. Click the **branch icon** (🔀) in the left Activity Bar to open the **Source Control** panel. *(Go to **View → Source Control** if you don't see it.)*
2. You will see `solution.py` listed under **Changes**, because you edited it.

---

### Step 7 — Stage Your Changes

1. Hover over `solution.py` in the **Changes** list.
2. Click the **`+`** (plus/stage) icon that appears to the right of the file name.  
   The file moves from **Changes** to **Staged Changes**.

---

### Step 8 — Write a Commit Message

1. Click inside the text box at the top of the Source Control panel that says **"Message (Ctrl+Enter to commit)"**.
2. Type a short, descriptive message, for example:

   ```
   assignment0: add student name
   ```

3. Do **not** press Enter yet.

---

### Step 9 — Commit Your Changes

1. Press **`Ctrl+Enter`** (Windows/Linux) or **`Cmd+Enter`** (Mac) to commit, **or** click the blue **✔ Commit** button.
2. A dialog may appear asking you to set your name and email for Git — enter the same name and your school email address.

---

### Step 10 — Push and Open a Pull Request

1. After committing, the Source Control panel shows a **Sync Changes** or **Publish Branch** button. Click it.
   - If prompted, choose **"Push"** to send your branch to GitHub.
2. Open your repository on **GitHub.com** (you can right-click → Open in Browser, or navigate to it in a new tab).
3. GitHub will show a yellow banner saying **"Compare & pull request"** — click it.
4. Fill in the Pull Request form:
   - **Title:** `Assignment 0 — Onboarding` (already suggested).
   - **Description:** Briefly describe what you did (e.g., "Added my student name to solution.py").
5. Click **"Create pull request"**.

> 🎉 You have just submitted your first assignment via a GitHub Pull Request!

---

### Step 11 — Check Your Dashboard

1. The repository is pre-configured to deploy to **Vercel**. Once your PR is merged (or when you navigate to the preview URL in Codespaces), open the **Dashboard** page.
2. The **Assignment 0 — Onboarding & Setup** card should now show a ✅ green border, confirming your solution passed.

> 💡 **How it works:** When you click the Dashboard link, the server runs `lib/assignment_loader.py assignment0` behind the scenes. This script imports your `solution.py` and runs `test_solution.py`. If every test passes, the card unlocks.

---

## ✅ Completion Checklist

Before moving on to Assignment 1, make sure you can check every box:

- [ ] I opened the repository in GitHub Codespaces.
- [ ] I edited `solution.py` and replaced `"Your Name Here"` with my real name.
- [ ] All tests in `test_solution.py` show a green ✅ in the Testing panel.
- [ ] I staged, committed, and pushed my changes using the Source Control panel.
- [ ] I opened a Pull Request on GitHub.
- [ ] My Assignment 0 card shows ✅ on the Dashboard.

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Codespace will not start | Refresh the page and try again. If it persists, delete the Codespace and create a new one. |
| Tests are not discovered | Open the Testing panel, click the refresh icon, and wait a few seconds. |
| `student_name` test still fails | Make sure you have not accidentally deleted the quotation marks or the variable name. The value must be a non-empty string. |
| "Publish Branch" button is missing | Make sure you committed first (Step 9). The button appears after the first commit. |
| Dashboard card is still locked | Make sure your PR has been merged into `main`, then reload the Dashboard page. |

---

*Next up: **Assignment 1 — Hello World** →* `assignments/assignment1/INSTRUCTIONS.md`
