"""Shared fixtures for the resume-screening test-suite."""

from __future__ import annotations

import pytest


class FakeLLM:
    """Deterministic stand-in for an LLM.

    Records every prompt it receives so tests can assert on exactly what was
    sent to the model, and returns a stable ``.content`` equal to a
    ``RESULT:`` prefix plus the prompt.
    """

    def __init__(self) -> None:
        self.history: list[str] = []

    def invoke(self, text: str) -> FakeLLM._Response:
        self.history.append(text)
        return self._Response(f"RESULT: {text}")

    class _Response:
        def __init__(self, content: str) -> None:
            self.content = content


@pytest.fixture
def fake_llm() -> FakeLLM:
    return FakeLLM()