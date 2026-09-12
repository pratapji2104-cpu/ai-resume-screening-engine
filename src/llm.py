"""LLM factory for the resume screening agents.

The actual Gemini client is imported lazily (inside :func:`get_llm`) so the
rest of the package — and its offline test-suite — can be imported and run
without ``langchain-google-genai`` installed.  Agents also accept a *mock*
LLM (anything exposing ``invoke(text) -> obj.content``) for deterministic,
key-free testing.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

DEFAULT_MODEL = "gemini-3.6-flash"

__all__ = ["DEFAULT_MODEL", "get_llm", "get_api_key"]


def get_api_key(api_key: str | None = None) -> str | None:
    """Resolve the Gemini API key from an explicit arg or the environment."""
    load_dotenv()
    return api_key or os.getenv("GOOGLE_API_KEY")


def get_llm(model: str = DEFAULT_MODEL, api_key: str | None = None):
    """Return a configured Gemini chat model.

    Import of ``langchain_google_genai`` is deferred so that importing this
    package never requires the heavy SDK unless a real LLM is requested.

    Raises:
        ValueError: if no ``GOOGLE_API_KEY`` can be found.
    """
    key = get_api_key(api_key)
    if not key:
        raise ValueError(
            "GOOGLE_API_KEY not found. Set it in your .env file "
            "(see .env.example) or pass api_key=... to get_llm()."
        )
    from langchain_google_genai import ChatGoogleGenerativeAI

    return ChatGoogleGenerativeAI(model=model, api_key=key)