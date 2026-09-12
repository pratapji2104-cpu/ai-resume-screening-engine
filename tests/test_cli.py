"""Tests for src.cli."""

from __future__ import annotations

import json

from src.cli import MockLLM, build_parser, main


def test_mock_llm_records_history() -> None:
    llm = MockLLM()
    response = llm.invoke("hello")
    assert llm.history == ["hello"]
    assert "hello" in response.content


def test_parser_has_expected_flags() -> None:
    parser = build_parser()
    args = parser.parse_args(["resume.txt", "--job-role", "web developer", "--mock"])
    assert args.resume == "resume.txt"
    assert args.job_role == "web developer"
    assert args.mock is True


def test_main_list_jobs(capsys) -> None:
    assert main(["--list-jobs"]) == 0
    out = capsys.readouterr().out
    assert "- python developer" in out
    assert "- software engineer" in out


def test_main_missing_resume_returns_1(capsys) -> None:
    assert main([]) == 1


def test_main_mock_run_outputs_json(tmp_path, capsys) -> None:
    resume = tmp_path / "resume.txt"
    resume.write_text("Jane Doe\nPython developer.", encoding="utf-8")

    assert main([str(resume), "--job-role", "python developer", "--mock"]) == 0
    out = capsys.readouterr().out
    data = json.loads(out)
    assert set(data) == {"analysis", "job_info", "feedback"}
    assert data["job_info"]["job_role"] == "python developer"
    assert "Resume Analysis Agent" in data["analysis"]
    assert "Resume Feedback Agent" in data["feedback"]


def test_main_mock_needs_no_api_key(tmp_path, monkeypatch) -> None:
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    resume = tmp_path / "resume.txt"
    resume.write_text("Jane Doe", encoding="utf-8")
    # Runs offline and succeeds without any key present.
    assert main([str(resume), "--mock"]) == 0