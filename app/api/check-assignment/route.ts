import { NextRequest, NextResponse } from "next/server";
import { execFile } from "child_process";
import path from "path";

/**
 * GET /api/check-assignment?id=<assignment_folder_name>
 *
 * Runs `python3 lib/assignment_loader.py <assignment_folder_name>` in a
 * child process and returns { passed: boolean, output: string }.
 *
 * The Python script exits with code 0 when all tests pass, non-zero otherwise.
 */
export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const id = searchParams.get("id");

  if (!id || !/^[\w-]+$/.test(id)) {
    return NextResponse.json({ error: "Invalid assignment id" }, { status: 400 });
  }

  const repoRoot = path.join(process.cwd());
  const loaderPath = path.join(repoRoot, "lib", "assignment_loader.py");

  return new Promise<NextResponse>((resolve) => {
    execFile(
      "python3",
      [loaderPath, id],
      { cwd: repoRoot, timeout: 15_000 },
      (error, stdout, stderr) => {
        const output = stdout + stderr;
        if (error) {
          resolve(
            NextResponse.json({ passed: false, output }, { status: 200 })
          );
        } else {
          resolve(
            NextResponse.json({ passed: true, output }, { status: 200 })
          );
        }
      }
    );
  });
}
