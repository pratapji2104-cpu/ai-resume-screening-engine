"""End-to-end resume screening workflow.

Orchestrates the analysis, job-lookup and feedback agents into a single
call, passing an injectable LLM through so the whole pipeline is testable
offline.
"""

from __future__ import annotations

from src.agents.job_agent import get_job_info
from src.agents.resume_analyzer import analyze_resume
from src.agents.resume_feedback import generate_feedback

__all__ = ["run_resume_workflow"]


def run_resume_workflow(resume_text: str, job_role: str, llm=None) -> dict:
    """Run the full screening pipeline for a resume against a target role.

    Args:
        resume_text: The candidate's resume as plain text.
        job_role: Target job role (e.g. ``"web developer"``).
        llm: Injectable LLM shared by the analysis and feedback agents.
            Defaults to the Gemini backend.

    Returns:
        dict: ``{"analysis": str, "job_info": dict, "feedback": str}``.
    """
    # Step 1: Analyze the resume
    analysis = analyze_resume(resume_text, llm=llm)

    # Step 2: Look up the job requirements
    job_info = get_job_info(job_role)

    # Step 3: Generate feedback from the analysis
    feedback = generate_feedback(analysis, llm=llm)

    return {
        "analysis": analysis,
        "job_info": job_info,
        "feedback": feedback,
    }