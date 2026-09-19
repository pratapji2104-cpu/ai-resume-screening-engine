# AI Resume Screening Engine

An AI-powered resume screening system that analyzes resumes, compares them with job requirements, and provides structured feedback.

## Project Objective

The project demonstrates the development of AI agents, prompt-based workflows, enterprise tool integration, validation, and intelligent skill matching.

The implementation currently covers:

- Milestone 1: Agent Environment Setup & Foundation Development
- Milestone 2: Tool Integration & Intelligent Action Execution

---

# Technology Stack

- Python
- LangChain
- Google Gemini
- Flask
- Flask-CORS
- PyPDF
- HTML
- CSS
- JavaScript
- Git & GitHub

---

# Milestone 1: Agent Foundation

## Resume Analyzer Agent

The Resume Analyzer Agent analyzes resume content and identifies:

- Candidate information
- Education
- Skills
- Experience
- Projects
- Missing or weak areas

## Resume Feedback Agent

The Resume Feedback Agent uses the resume analysis to generate:

- Strengths
- Weaknesses
- Suggestions for improvement

## Agent Workflow

The basic workflow is:

```text
Resume
   ↓
Resume Analyzer Agent
   ↓
Resume Feedback Agent
   ↓
Structured Resume Feedback
