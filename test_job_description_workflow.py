from src.workflow import run_resume_workflow


resume = """
Pragya Pratap

Computer Science Engineering student.

Skills:
C++, Python, JavaScript, HTML, CSS, DSA, Git.

Projects:
To-Do Web Application developed using HTML, CSS, and JavaScript.

Experience:
No prior professional work experience.
"""


job_description = """
We are looking for a Web Developer.

Required skills:
HTML, CSS, JavaScript, React, Git and SQL.

The candidate should have good knowledge
of data structures and algorithms.
"""


result = run_resume_workflow(
    resume,
    "web developer",
    job_description
)


print("\n===== JOB DESCRIPTION REQUIREMENTS =====")
print(result["job_description_requirements"])

print("\n===== SKILL MATCHING =====")
print(result["skill_matching"])