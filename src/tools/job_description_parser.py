import re


def extract_job_requirements(job_description):

    if not job_description or not job_description.strip():
        raise ValueError("Job description is required")

    text = job_description.lower()

    skill_keywords = [
        "python",
        "java",
        "c++",
        "javascript",
        "html",
        "css",
        "sql",
        "git",
        "react",
        "node.js",
        "mongodb",
        "django",
        "flask",
        "machine learning",
        "data structures",
        "algorithms"
    ]

    required_skills = []

    for skill in skill_keywords:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            required_skills.append(skill)

    if not required_skills:
        raise ValueError(
            "No supported skills found in job description"
        )

    return {
        "required_skills": required_skills
    }