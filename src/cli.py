"""Command-line interface for the AI Resume Screening Engine.

Runs the full workflow (analysis + job info + feedback) for a resume file.
Use ``--mock`` for a deterministic, key-free run — useful for demos, CI and
testing without a Google API key.
"""

from __future__ import annotations

import argparse
import json
import sys

from src.enterprise_tools import list_jobs
from src.workflow import run_resume_workflow

__all__ = ["main", "build_parser", "MockLLM"]


class MockLLM:
    """Deterministic stand-in for an LLM (no network, no API key).

    `invoke()` echoes the prompt inside a ``[mock]`` block wrapped in
    ``RESULT:`` so callers can verify the request made it through.
    """

    def __init__(self) -> None:
        self.history: list[str] = []

    def invoke(self, text: str) -> MockLLM._Response:
        self.history.append(text)
        return self._Response(f"RESULT: [mock] {text}")

    class _Response:
        def __init__(self, content: str) -> None:
            self.content = content


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="resume-screen",
        description="AI Resume Screening Engine",
    )
    parser.add_argument("resume", nargs="?", help="Path to a resume text file")
    parser.add_argument(
        "--job-role",
        default="software engineer",
        help="Target job role (default: %(default)s)",
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Use a deterministic mock LLM (no Google API key needed)",
    )
    parser.add_argument(
        "--list-jobs",
        action="store_true",
        help="List supported job roles and exit",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list_jobs:
        print("\n".join(f"- {role}" for role in list_jobs()))
        return 0

    if not args.resume:
        parser.print_help()
        return 1

    with open(args.resume, encoding="utf-8") as fh:
        resume_text = fh.read()

    llm = MockLLM() if args.mock else None
    result = run_resume_workflow(resume_text, args.job_role, llm=llm)

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())