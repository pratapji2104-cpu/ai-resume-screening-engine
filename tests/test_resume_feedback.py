"""Tests for src.agents.resume_feedback."""

from __future__ import annotations

from src.agents.resume_feedback import (
    FEEDBACK_PROMPT,
    build_feedback_prompt,
    generate_feedback,
)

ANALYSIS = "Candidate: Jane Doe. Strong Python and SQL skills."


def test_feedback_prompt_mentions_required_items() -> None:
    for item in ("2 strengths", "2 weaknesses", "3 improvement suggestions"):
        assert item in FEEDBACK_PROMPT


def test_build_feedback_prompt_embeds_analysis() -> None:
    prompt = build_feedback_prompt(ANALYSIS)
    assert ANALYSIS in prompt


def test_generate_feedback_uses_llm_and_returns_content(fake_llm) -> None:
    result = generate_feedback(ANALYSIS, llm=fake_llm)
    assert result == f"RESULT: {build_feedback_prompt(ANALYSIS)}"
    assert fake_llm.history == [build_feedback_prompt(ANALYSIS)]