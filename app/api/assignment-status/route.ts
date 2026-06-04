import { spawnSync } from "child_process";
import { existsSync } from "fs";
import { NextResponse } from "next/server";

const titles = [
  "Week 1: Basic Python - Calculator",
  "Week 2: Basic Logic",
  "Week 3: Productivity Math",
  "Week 4: review4 (Fundamentals Review)",
  "Week 5: exam1 (Fundamentals Assessment)",
  "Week 6: Loops",
  "Week 7: Functions",
  "Week 8: Data Structures",
  "Week 9: review9 (Loops/Functions/Data Review)",
  "Week 10: exam2 (Loops/Functions/Data Assessment)",
  "Week 11: File I/O",
  "Week 12: OOP Basics",
  "Week 13: OOP Modeling",
  "Week 14: Advanced Features",
  "Week 15: review15 (File I/O, OOP, Advanced Review)",
  "Week 16: exam3 (Comprehensive Final Assessment)",
];

const PYTHON_BIN = process.env.PYTHON_BIN ?? "python3";
const CACHE_TTL_MS = 60_000;
let cache: { createdAt: number; assignments: ReturnType<typeof runAssignmentTest>[] } | null = null;

function runAssignmentTest(assignmentNumber: number) {
  const assignment = `assignment${assignmentNumber}`;
  const testPath = `${process.cwd()}/${assignment}/test_solution.py`;
  if (!existsSync(testPath)) {
    return { assignment, title: titles[assignmentNumber - 1], unlocked: false };
  }

  const result = spawnSync(PYTHON_BIN, [testPath], { encoding: "utf-8" });

  return {
    assignment,
    title: titles[assignmentNumber - 1],
    unlocked: result.status === 0,
  };
}

export async function GET() {
  if (cache && Date.now() - cache.createdAt < CACHE_TTL_MS) {
    return NextResponse.json({ assignments: cache.assignments });
  }

  const assignments = Array.from({ length: 16 }, (_, idx) => runAssignmentTest(idx + 1));
  cache = { assignments, createdAt: Date.now() };
  return NextResponse.json({ assignments });
}
