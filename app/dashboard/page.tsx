/**
 * app/dashboard/page.tsx
 *
 * Server Component — fetches assignment status on every request so students
 * always see their latest results without a manual refresh.
 *
 * Each assignment is checked by calling the internal API route, which runs
 * the Python test suite via lib/assignment_loader.py.
 */

import { headers } from "next/headers";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

interface Assignment {
  id: string;
  week: number | string;
  title: string;
  description: string;
  type: "assignment" | "review" | "exam";
}

interface AssignmentStatus extends Assignment {
  isUnlocked: boolean;
  output: string;
}

// ---------------------------------------------------------------------------
// Course metadata
// ---------------------------------------------------------------------------

const ASSIGNMENTS: Assignment[] = [
  { id: "assignment0",  week: 0,  title: "Onboarding & Setup",              description: "Configure your Codespace and submit your first commit.",          type: "assignment" },
  { id: "assignment1",  week: 1,  title: "Hello World",                     description: "Display a personalised greeting in the dashboard.",              type: "assignment" },
  { id: "assignment2",  week: 2,  title: "Calculator",                      description: "Build arithmetic utilities for the productivity tracker.",        type: "assignment" },
  { id: "assignment3",  week: 3,  title: "Decision Logic",                  description: "Add conditional rendering based on user stats.",                 type: "assignment" },
  { id: "review4",      week: 4,  title: "Review: Fundamentals",            description: "Consolidate variables, types, operators & control flow.",         type: "review"     },
  { id: "exam5",        week: 5,  title: "Test 1 Practice",                 description: "Practice exam covering weeks 1–4.",                              type: "exam"       },
  { id: "assignment6",  week: 6,  title: "Loops",                           description: "Iterate over task lists to compute completion stats.",            type: "assignment" },
  { id: "assignment7",  week: 7,  title: "Functions",                       description: "Refactor dashboard helpers into reusable functions.",             type: "assignment" },
  { id: "assignment8",  week: 8,  title: "Data Structures",                 description: "Store and query task data using lists and dicts.",                type: "assignment" },
  { id: "review9",      week: 9,  title: "Review: Loops, Functions & Data", description: "Consolidate loops, functions, lists, dicts and tuples.",          type: "review"     },
  { id: "exam10",       week: 10, title: "Test 2 Practice",                 description: "Practice exam covering weeks 6–9.",                              type: "exam"       },
  { id: "assignment11", week: 11, title: "File I/O",                        description: "Persist task data to a local CSV/JSON file.",                    type: "assignment" },
  { id: "assignment12", week: 12, title: "OOP Classes",                     description: "Model a Task Manager using a Python class.",                     type: "assignment" },
  { id: "assignment13", week: 13, title: "Inheritance & Polymorphism",      description: "Extend Task Manager with specialised task types.",               type: "assignment" },
  { id: "assignment14", week: 14, title: "Advanced Features",               description: "Add decorators and generators to the task pipeline.",             type: "assignment" },
  { id: "review15",     week: 15, title: "Review: File I/O, OOP & Advanced", description: "Consolidate file handling, OOP and advanced Python.",          type: "review"     },
  { id: "exam16",       week: 16, title: "Final Exam Practice",             description: "Comprehensive practice exam covering the full course.",           type: "exam"       },
];

// ---------------------------------------------------------------------------
// Helper: check a single assignment via the internal API
// ---------------------------------------------------------------------------

async function checkAssignment(id: string, baseUrl: string): Promise<{ passed: boolean; output: string }> {
  try {
    const res = await fetch(`${baseUrl}/api/check-assignment?id=${id}`, {
      cache: "no-store",
    });
    if (!res.ok) return { passed: false, output: "Error contacting check API." };
    return res.json();
  } catch {
    return { passed: false, output: "Could not reach check API." };
  }
}

// ---------------------------------------------------------------------------
// Page
// ---------------------------------------------------------------------------

export default async function DashboardPage() {
  // Determine base URL from the incoming request headers so this works both
  // locally (http://localhost:3000) and on Vercel (https://<your-app>.vercel.app).
  const headersList = await headers();
  const host = headersList.get("host") ?? "localhost:3000";
  const proto = host.startsWith("localhost") ? "http" : "https";
  const baseUrl = `${proto}://${host}`;

  // Check all assignments in parallel for fast page load.
  const results = await Promise.all(
    ASSIGNMENTS.map(async (a): Promise<AssignmentStatus> => {
      const { passed, output } = await checkAssignment(a.id, baseUrl);
      return { ...a, isUnlocked: passed, output };
    })
  );

  const completedCount = results.filter((r) => r.isUnlocked).length;
  const totalCount = results.length;

  return (
    <div>
      <h1 style={{ marginBottom: "0.25rem" }}>📊 My Progress Dashboard</h1>
      <p style={{ color: "#555", marginBottom: "2rem" }}>
        {completedCount} / {totalCount} assignments completed
      </p>

      {/* Progress bar */}
      <div style={{ background: "#ddd", borderRadius: "8px", height: "12px", marginBottom: "2.5rem" }}>
        <div
          style={{
            background: "#4caf50",
            width: `${(completedCount / totalCount) * 100}%`,
            height: "100%",
            borderRadius: "8px",
            transition: "width 0.4s ease",
          }}
        />
      </div>

      {/* Assignment cards */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))",
          gap: "1.25rem",
        }}
      >
        {results.map((a) => (
          <AssignmentCard key={a.id} assignment={a} />
        ))}
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Card sub-component (still a server component — no interactivity needed)
// ---------------------------------------------------------------------------

function AssignmentCard({ assignment }: { assignment: AssignmentStatus }) {
  const { id, week, title, description, type, isUnlocked, output } = assignment;

  const borderColor = isUnlocked
    ? "#4caf50"
    : type === "exam"
    ? "#e91e63"
    : type === "review"
    ? "#ff9800"
    : "#ccc";

  const badge =
    type === "exam"
      ? { label: "Exam", bg: "#fce4ec", color: "#c62828" }
      : type === "review"
      ? { label: "Review", bg: "#fff3e0", color: "#e65100" }
      : { label: "Assignment", bg: "#e8f5e9", color: "#2e7d32" };

  return (
    <div
      style={{
        background: "#fff",
        border: `2px solid ${borderColor}`,
        borderRadius: "10px",
        padding: "1.25rem",
        opacity: isUnlocked ? 1 : 0.65,
        position: "relative",
      }}
    >
      {/* Week + badge */}
      <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "0.5rem" }}>
        <span style={{ fontSize: "0.8rem", color: "#888" }}>Week {week}</span>
        <span
          style={{
            fontSize: "0.75rem",
            fontWeight: 600,
            background: badge.bg,
            color: badge.color,
            padding: "2px 8px",
            borderRadius: "12px",
          }}
        >
          {badge.label}
        </span>
      </div>

      {/* Title */}
      <h3 style={{ margin: "0 0 0.4rem", fontSize: "1rem" }}>
        {isUnlocked ? "✅" : "🔒"} {title}
      </h3>

      {/* Description */}
      <p style={{ margin: "0 0 0.75rem", fontSize: "0.9rem", color: "#555" }}>
        {description}
      </p>

      {/* Folder label */}
      <code
        style={{
          fontSize: "0.75rem",
          background: "#f0f0f0",
          padding: "2px 6px",
          borderRadius: "4px",
        }}
      >
        assignments/{id}/
      </code>

      {/* Test output (collapsed by default via details/summary) */}
      {output && (
        <details style={{ marginTop: "0.75rem" }}>
          <summary style={{ fontSize: "0.8rem", cursor: "pointer", color: "#888" }}>
            Test output
          </summary>
          <pre
            style={{
              fontSize: "0.75rem",
              background: "#1e1e1e",
              color: "#d4d4d4",
              padding: "0.5rem",
              borderRadius: "4px",
              overflow: "auto",
              maxHeight: "150px",
              marginTop: "0.4rem",
              whiteSpace: "pre-wrap",
            }}
          >
            {output}
          </pre>
        </details>
      )}
    </div>
  );
}
