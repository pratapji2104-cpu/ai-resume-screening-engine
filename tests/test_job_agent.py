"""Tests for src.agents.job_agent."""

from __future__ import annotations

from src.agents.job_agent import get_job_info


def test_get_job_info_success() -> None:
    info = get_job_info("web developer")
    assert info["job_role"] == "web developer"
    assert info["requirements"]["experience"] == "0-2 years"


def test_get_job_info_unknown_role_returns_error_dict() -> None:
    info = get_job_info("data scientist")
    assert "error" in info
    assert "not found" in info["error"]