# Assignment 0: Onboarding and First Merge

Welcome to the **Python Productivity Hub** project. In this onboarding assignment, you will make a small profile update and ship it through the full GitHub + Vercel workflow using only interface actions.

## Goal
Update the `name` variable in `assignment0/profile.py` and merge your first pull request.

## Step-by-step workflow (UI only)
1. Open the repository on GitHub and select **Fork** in the top-right corner.
2. In your fork, select **Code** and then choose **Create codespace on main**.
3. After Codespaces loads, open the left sidebar and select **Explorer**.
4. Open `assignment0/profile.py`.
5. Change the value of `name` to your own name and save the file.
6. Open the **Testing** panel in Codespaces (beaker icon).
7. Run the assignment tests from the Testing panel and confirm they pass.
8. Open the **Source Control** panel (branch icon).
9. Select **Create Branch** and name it something like `assignment0-onboarding`.
10. Stage your changes using the `+` button next to the file.
11. Enter a commit message and select **Commit**.
12. Select **Publish Branch** / **Push** from the Source Control interface.
13. Return to GitHub and select **Compare & pull request**.
14. Fill in the PR title and description, then open the pull request.
15. Wait for checks to complete, then select **Merge pull request**.
16. Confirm the branch was merged.

## How to verify
1. After merge, open your Vercel project dashboard.
2. Select the latest production deployment.
3. Open the deployment URL and confirm your updated profile appears in the deployed app.
4. In GitHub, verify your merged PR is listed under the repository Pull Requests tab.

## Important rules for this course
- Do not use terminal commands for tests, commits, pushes, or branch creation.
- Use the **Testing** panel for tests.
- Use the **Source Control** panel for stage/commit/push actions.
