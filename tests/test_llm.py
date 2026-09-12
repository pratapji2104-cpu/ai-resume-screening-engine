"""Tests for src.llm (the Gemini backend factory)."""

from __future__ import annotations

import pytest

from src.llm import DEFAULT_MODEL, get_api_key, get_llm


def test_default_model_is_set() -> None:
    assert DEFAULT_MODEL == "gemini-3.6-flash"


def test_get_api_key_uses_explicit_arg() -> None:
    assert get_api_key("abc123") == "abc123"


def test_get_api_key_reads_environment(monkeypatch) -> None:
    monkeypatch.setenv("GOOGLE_API_KEY", "env-key")
    assert get_api_key() == "env-key"


def test_get_llm_raising_without_key(monkeypatch) -> None:
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    with pytest.raises(ValueError, match="GOOGLE_API_KEY"):
        get_llm(api_key=None)


def test_get_llm_raising_with_blank_env(monkeypatch) -> None:
    monkeypatch.setenv("GOOGLE_API_KEY", "")
    with pytest.raises(ValueError, match="GOOGLE_API_KEY"):
        get_llm()