"""Tests for src.agents.tool_selector."""

from __future__ import annotations

from src.agents.tool_selector import execute_request, select_tool


def test_select_tool_matches_job_keyword() -> None:
    assert select_tool("Show me the job requirements") == "get_job_requirements"


def test_select_tool_matches_skills_keyword() -> None:
    assert select_tool("what skills are required?") == "get_job_requirements"


def test_select_tool_is_case_insensitive() -> None:
    assert select_tool("JOB REQUIREMENTS") == "get_job_requirements"


def test_select_tool_no_match() -> None:
    assert select_tool("what is the weather today") == "no_tool"


def test_execute_request_success() -> None:
    result = execute_request("job requirements", "web developer")
    assert result["required_skills"] == ["HTML", "CSS", "JavaScript"]


def test_execute_request_unknown_role_returns_error_dict() -> None:
    result = execute_request("job requirements", "data scientist")
    assert "error" in result
    assert "not found" in result["error"]


def test_execute_request_no_tool_selected() -> None:
    result = execute_request("unrelated question", "web developer")
    assert result == {"message": "No enterprise tool required"}