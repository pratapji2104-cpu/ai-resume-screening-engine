from src.workflow import run_resume_workflow


resume = """
Pragya Pratap

Education:
B.Tech Computer Science Engineering

Skills:
C++, Python, JavaScript, HTML, CSS, DSA

Projects:
To-Do Web Application using HTML, CSS and JavaScript.

Experience:
Currently looking for internship opportunities.
"""

result = run_resume_workflow(resume, "web developer")

print("\n===== RESUME ANALYSIS =====")
print(result["analysis"])

print("\n===== RESUME FEEDBACK =====")
print(result["feedback"])

print("\n===== JOB REQUIREMENTS =====")
print(result["job_info"])