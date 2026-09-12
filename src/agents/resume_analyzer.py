"""Resume analysis agent.

Builds a structured-analysis prompt for a resume and sends it to an LLM.
The LLM is injectable so the module is unit-testable without a network
connection or API key.
"""

from __future__ import annotations

from src.llm import get_llm

RESUME_ANALYSIS_PROMPT = """You are a Resume Analysis Agent.

Analyze the candidate's resume and provide a structured analysis.

Extract the following information:

1. Candidate Name
2. Technical Skills
3. Education
4. Work Experience
5. Projects
6. Certifications
7. Overall Strengths
8. Areas that need improvement

Keep the analysis concise and factual.
Do not invent information that is not present in the resume.

Resume:
{resume_text}"""

__all__ = ["RESUME_ANALYSIS_PROMPT", "build_analysis_prompt", "analyze_resume"]


def build_analysis_prompt(resume_text: str) -> str:
    """Build the analysis prompt for a given resume."""
    return RESUME_ANALYSIS_PROMPT.format(resume_text=resume_text)


def analyze_resume(resume_text: str, llm=None) -> str:
    """Analyze a resume and return the LLM's structured analysis.

    Args:
        resume_text: The candidate's resume as plain text.
        llm: Any object with ``invoke(text)`` returning a result with a
            ``.content`` attribute. Defaults to the Gemini backend.

    Returns:
        str: The model's analysis text.
    """
    if llm is None:
        llm = get_llm()
    prompt = build_analysis_prompt(resume_text)
    return llm.invoke(prompt).content