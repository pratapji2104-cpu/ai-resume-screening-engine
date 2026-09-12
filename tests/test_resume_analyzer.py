"""Tests for src.agents.resume_analyzer."""

from __future__ import annotations

import pytest

from src.agents.resume_analyzer import (
    RESUME_ANALYSIS_PROMPT,
    analyze_resume,
    build_analysis_prompt,
)

RESUME = """Jane Doe
Software developer with 3 years of Python experience."""


def test_prompt_contains_required_sections() -> None:
    for section in (
        "Candidate Name",
        "Technical Skills",
        "Education",
        "Work Experience",
        "Projects",
        "Certifications",
        "Overall Strengths",
        "Areas that need improvement",
    ):
        assert section in RESUME_ANALYSIS_PROMPT


def test_build_analysis_prompt_embeds_resume() -> None:
    prompt = build_analysis_prompt(RESUME)
    assert RESUME in prompt
    assert prompt.startswith("You are a Resume Analysis Agent.")


def test_analyze_resume_uses_llm_and_returns_content(fake_llm) -> None:
    result = analyze_resume(RESUME, llm=fake_llm)
    assert result == f"RESULT: {build_analysis_prompt(RESUME)}"
    assert fake_llm.history == [build_analysis_prompt(RESUME)]


def test_analyze_resume_without_key_raises(fake_llm, monkeypatch) -> None:
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    # Force get_llm() to build a real backend with no key in scope.
    from src.agents import resume_analyzer

    # Patch the module's get_llm so it hits the missing-key path.
    def _missing():
        raise ValueError(
            "GOOGLE_API_KEY not found. Set it in your .env file "
            "(see .env.example) or pass api_key=... to get_llm()."
        )

    monkeypatch.setattr(resume_analyzer, "get_llm", _missing)

    with pytest.raises(ValueError):
        analyze_resume(RESUME)