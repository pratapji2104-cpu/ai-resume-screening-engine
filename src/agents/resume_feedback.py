"""Resume feedback agent.

Turns an existing resume analysis into short, actionable feedback.  LLM is
injectable for offline testing (same interface as the analyzer).
"""

from __future__ import annotations

from src.llm import get_llm

FEEDBACK_PROMPT = """You are a Resume Feedback Agent.

Give very simple and concise feedback on this resume analysis.

Provide only:
1. 2 strengths
2. 2 weaknesses
3. 3 improvement suggestions

Use short bullet points.
Do not explain in detail.
Do not invent information.

Resume Analysis:
{analysis}"""

__all__ = ["FEEDBACK_PROMPT", "build_feedback_prompt", "generate_feedback"]


def build_feedback_prompt(analysis: str) -> str:
    """Build the feedback prompt for a given resume analysis."""
    return FEEDBACK_PROMPT.format(analysis=analysis)


def generate_feedback(analysis: str, llm=None) -> str:
    """Generate concise strengths / weaknesses / suggestions feedback."""
    if llm is None:
        llm = get_llm()
    prompt = build_feedback_prompt(analysis)
    return llm.invoke(prompt).content