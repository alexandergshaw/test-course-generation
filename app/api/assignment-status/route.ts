import { spawnSync } from "child_process";
import { NextResponse } from "next/server";

const titles = [
  "Week 1: Basic Python - Calculator",
  "Week 2: Basic Logic",
  "Week 3: Productivity Math",
  "Week 4: review4",
  "Week 5: exam1",
  "Week 6: Loops",
  "Week 7: Functions",
  "Week 8: Data Structures",
  "Week 9: review9",
  "Week 10: exam2",
  "Week 11: File I/O",
  "Week 12: OOP Basics",
  "Week 13: OOP Modeling",
  "Week 14: Advanced Features",
  "Week 15: review15",
  "Week 16: exam3",
];

function runAssignmentTest(assignmentNumber: number) {
  const assignment = `assignment${assignmentNumber}`;
  const testPath = `${process.cwd()}/${assignment}/test_solution.py`;
  const result = spawnSync("python", [testPath], { encoding: "utf-8" });

  return {
    assignment,
    title: titles[assignmentNumber - 1],
    unlocked: result.status === 0,
  };
}

export async function GET() {
  const assignments = Array.from({ length: 16 }, (_, idx) => runAssignmentTest(idx + 1));
  return NextResponse.json({ assignments });
}
