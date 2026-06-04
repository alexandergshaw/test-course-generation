import Link from "next/link";

export default function HomePage() {
  return (
    <div style={{ textAlign: "center", paddingTop: "4rem" }}>
      <h1 style={{ fontSize: "2.5rem", marginBottom: "1rem" }}>
        🐍 Python Foundations
      </h1>
      <p style={{ fontSize: "1.2rem", color: "#555", marginBottom: "2rem" }}>
        Building a Personal Productivity Tracker — one assignment at a time.
      </p>
      <Link
        href="/dashboard"
        style={{
          display: "inline-block",
          background: "#1a1a2e",
          color: "#fff",
          padding: "0.75rem 2rem",
          borderRadius: "8px",
          textDecoration: "none",
          fontSize: "1.1rem",
        }}
      >
        View My Dashboard →
      </Link>
    </div>
  );
}
