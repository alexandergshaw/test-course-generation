import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Python Foundations Dashboard",
  description: "Personal Productivity Tracker — Python Foundations Course",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body style={{ margin: 0, fontFamily: "system-ui, sans-serif", background: "#f5f5f5" }}>
        <nav style={{ background: "#1a1a2e", color: "#fff", padding: "1rem 2rem", display: "flex", gap: "2rem", alignItems: "center" }}>
          <strong style={{ fontSize: "1.1rem" }}>🐍 Python Foundations</strong>
          <a href="/" style={{ color: "#ccc", textDecoration: "none" }}>Home</a>
          <a href="/dashboard" style={{ color: "#ccc", textDecoration: "none" }}>Dashboard</a>
        </nav>
        <main style={{ maxWidth: "1100px", margin: "0 auto", padding: "2rem" }}>
          {children}
        </main>
      </body>
    </html>
  );
}
