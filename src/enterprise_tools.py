"""Enterprise tools: job-role requirement lookup.

Pure data + validation module — no external dependencies.
"""

from __future__ import annotations

JOB_REQUIREMENTS = {
    "python developer": {
        "required_skills": ["Python", "SQL", "Git"],
        "experience": "0-2 years",
    },
    "web developer": {
        "required_skills": ["HTML", "CSS", "JavaScript"],
        "experience": "0-2 years",
    },
    "software engineer": {
        "required_skills": ["C++", "DSA", "Git"],
        "experience": "0-2 years",
    },
}

__all__ = ["JOB_REQUIREMENTS", "get_job_requirements", "list_jobs"]


def list_jobs() -> list[str]:
    """Return the supported job roles, sorted alphabetically."""
    return sorted(JOB_REQUIREMENTS)


def get_job_requirements(job_role: str) -> dict:
    """Return the requirements dict for a role (case-insensitive).

    Raises:
        ValueError: if the role is not a known job role.
    """
    key = job_role.lower()
    try:
        return JOB_REQUIREMENTS[key]
    except KeyError:
        raise ValueError(f"Job role not found: {job_role}") from None