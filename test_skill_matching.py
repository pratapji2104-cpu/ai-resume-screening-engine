from src.agents.skill_matching import match_skills


resume = """
I am a Web Developer with knowledge of HTML, CSS,
JavaScript and Git. I have also worked with Python.
"""

required_skills = [
    "html",
    "css",
    "javascript",
    "react",
    "git"
]


result = match_skills(resume, required_skills)

print("\n===== SKILL MATCHING RESULT =====")
print(result)