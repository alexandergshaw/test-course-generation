"use client";

import { useEffect, useState } from "react";

type AssignmentStatus = {
  assignment: string;
  title: string;
  unlocked: boolean;
};

const unlockedFeatures: Record<string, string> = {
  assignment1: "Calculator UI",
  assignment2: "Logic Evaluator",
  assignment3: "Focus Timer",
  assignment4: "Review Workspace",
  assignment5: "Fundamentals Exam Panel",
  assignment6: "Loop Insights",
  assignment7: "Function Library",
  assignment8: "Data Structure Viewer",
  assignment9: "Review Drill Set",
  assignment10: "Exam Analytics",
  assignment11: "File Parser UI",
  assignment12: "OOP Class Visualizer",
  assignment13: "Model Relationship Map",
  assignment14: "Advanced Automation Panel",
  assignment15: "Comprehensive Review Board",
  assignment16: "Final Productivity Command Center",
};

export default function DashboardGrid() {
  const [assignments, setAssignments] = useState<AssignmentStatus[]>([]);

  useEffect(() => {
    fetch("/api/assignment-status")
      .then((response) => response.json())
      .then((data) => setAssignments(data.assignments ?? []));
  }, []);

  return (
    <div className="mx-auto max-w-6xl p-8">
      <h1 className="mb-6 text-3xl font-bold">Python Productivity Hub</h1>
      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
        {assignments.map((item) => (
          <article
            key={item.assignment}
            className={`rounded-xl border p-5 ${
              item.unlocked ? "border-emerald-400 bg-emerald-950/40" : "border-slate-700 bg-slate-900"
            }`}
          >
            <p className="text-sm text-slate-400">{item.assignment}</p>
            <h2 className="text-lg font-semibold">{item.title}</h2>
            {item.unlocked ? (
              <p className="mt-3 text-emerald-300">Unlocked: {unlockedFeatures[item.assignment]}</p>
            ) : (
              <p className="mt-3 text-amber-300">Locked: Complete {item.assignment}/solution.py</p>
            )}
          </article>
        ))}
      </div>
    </div>
  );
}
