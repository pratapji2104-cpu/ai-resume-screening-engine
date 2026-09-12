"""Tool-selector agent: route a free-form user request to an enterprise tool."""

from __future__ import annotations

from src.enterprise_tools import get_job_requirements

__all__ = ["select_tool", "execute_request"]

_KEYWORDS = ("job", "requirements", "skills")


def select_tool(user_request: str) -> str:
    """Return the tool name for a request, or ``"no_tool"`` if not matched."""
    request = user_request.lower()
    if any(kw in request for kw in _KEYWORDS):
        return "get_job_requirements"
    return "no_tool"


def execute_request(user_request: str, job_role: str) -> dict:
    """Execute the tool selected for ``user_request`` against ``job_role``."""
    selected_tool = select_tool(user_request)

    if selected_tool == "get_job_requirements":
        try:
            return get_job_requirements(job_role)
        except ValueError as e:
            return {"error": str(e)}

    return {"message": "No enterprise tool required"}