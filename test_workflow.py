from src.workflow import run_resume_workflow


resume = """
Pragya Pratap

Computer Science Engineering student.

Skills:
C++, Python, JavaScript, HTML, CSS, DSA, Git.

Projects:
To-Do Web Application developed using HTML, CSS, and JavaScript.

Experience:
No prior professional work experience; currently seeking internship opportunities.
"""


result = run_resume_workflow(resume, "web developer")


print("\n===== RESUME ANALYSIS =====")
print(result["analysis"])


print("\n===== RESUME FEEDBACK =====")
print(result["feedback"])


print("\n===== JOB REQUIREMENTS =====")
print(result["job_info"])


print("\n===== SKILL MATCHING =====")
print(result["skill_matching"])