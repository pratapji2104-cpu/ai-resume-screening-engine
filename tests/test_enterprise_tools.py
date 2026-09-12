"""Tests for src.enterprise_tools."""

from __future__ import annotations

import pytest

from src.enterprise_tools import JOB_REQUIREMENTS, get_job_requirements, list_jobs


def test_get_job_requirements_known_role() -> None:
    req = get_job_requirements("web developer")
    assert req == {
        "required_skills": ["HTML", "CSS", "JavaScript"],
        "experience": "0-2 years",
    }


def test_get_job_requirements_is_case_insensitive() -> None:
    assert get_job_requirements("Web Developer") == get_job_requirements("web developer")
    assert get_job_requirements("PYTHON DEVELOPER")["required_skills"] == [
        "Python",
        "SQL",
        "Git",
    ]


def test_get_job_requirements_unknown_role_raises_value_error() -> None:
    with pytest.raises(ValueError):
        get_job_requirements("data scientist")


def test_get_job_requirements_all_roles_have_skipped_whitespace() -> None:
    for role in JOB_REQUIREMENTS:
        assert "  " not in role


def test_list_jobs_is_sorted() -> None:
    jobs = list_jobs()
    assert jobs == sorted(jobs)
    assert jobs == ["python developer", "software engineer", "web developer"]