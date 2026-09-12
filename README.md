# AI Resume Screening Engine

A foundational AI resume screening system built with LangChain and Google
Gemini. It analyzes a candidate's resume, looks up the target job's
requirements, and generates concise, actionable feedback.

## Features

- **Resume analysis agent** — extracts name, skills, education, experience,
  projects, certifications, strengths and areas for improvement.
- **Feedback agent** — turns an analysis into 2 strengths, 2 weaknesses and
  3 improvement suggestions.
- **Job lookup** — maps common roles (python/web/software engineer) to their
  required skills and experience.
- **Tool selector** — routes a free-form user request to the right
  enterprise tool.
- **Offline-first design** — agents accept an injectable LLM, so the whole
  pipeline runs without a network connection or API key (`--mock` mode).

## Project Structure

```text
ai-resume-screening-engine/
├── src/
│   ├── agents/
│   │   ├── job_agent.py          # job-info lookup agent
│   │   ├── resume_analyzer.py    # resume analysis agent
│   │   ├── resume_feedback.py    # feedback agent
│   │   └── tool_selector.py      # request → tool router
│   ├── cli.py                    # command-line interface (resume-screen)
│   ├── enterprise_tools.py       # job-role requirement lookup
│   ├── llm.py                    # Gemini backend factory (injectable)
│   └── workflow.py               # end-to-end screening workflow
├── tests/                        # offline pytest suite (no API key needed)
├── .env.example
├── pyproject.toml
├── requirements.txt
└── LICENSE
```

## Quick Start

### 1. Install

```bash
uv venv .venv
uv pip install -e ".[gemini,dev]"
# or with pip:
# pip install -e ".[gemini,dev]"
cp .env.example .env   # then add your GOOGLE_API_KEY
```

### 2. Run without an API key (mock mode)

```bash
resume-screen resume.txt --job-role "web developer" --mock
```

Or list supported roles:

```bash
resume-screen --list-jobs
```

### 3. Run with the real Gemini backend

```bash
resume-screen resume.txt --job-role "software engineer"
```

### 4. From Python

```python
from src.workflow import run_resume_workflow

result = run_resume_workflow(resume_text, "python developer")
print(result["analysis"])
print(result["job_info"])
print(result["feedback"])
```

## Running Tests

```bash
uv run pytest tests/ -v
```

The test-suite is fully offline — it injects a deterministic `FakeLLM`, so
no network access or API key is required.

## Technology Stack

- Python
- LangChain + LangChain Google GenAI (optional, only for real calls)
- Google Gemini API
- python-dotenv

## License

MIT