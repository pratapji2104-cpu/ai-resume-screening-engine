"""Tests for src.workflow."""

from __future__ import annotations

from src.workflow import run_resume_workflow

RESUME = """Jane Doe
Software developer proficient in Python, SQL and Git."""


def test_workflow_returns_all_keys(fake_llm) -> None:
    result = run_resume_workflow(RESUME, "python developer", llm=fake_llm)
    assert set(result) == {"analysis", "job_info", "feedback"}
    assert result["job_info"]["job_role"] == "python developer"
    # The same LLM should have been used for analysis + feedback = 2 invokes.
    assert len(fake_llm.history) == 2


def test_workflow_shares_llm_across_agents(fake_llm) -> None:
    run_resume_workflow(RESUME, "software engineer", llm=fake_llm)
    # analysis prompt then feedback prompt, in that order.
    assert "Resume Analysis Agent" in fake_llm.history[0]
    assert "Resume Feedback Agent" in fake_llm.history[1]


def test_workflow_unknown_role_still_returns_error_dict(fake_llm) -> None:
    result = run_resume_workflow(RESUME, "data scientist", llm=fake_llm)
    assert "error" in result["job_info"]
    assert result["analysis"]
    assert result["feedback"]