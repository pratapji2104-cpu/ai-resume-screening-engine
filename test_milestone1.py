from src.agents.resume_analyzer import analyze_resume
from src.agents.resume_feedback import generate_feedback


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


print("\n===== RESUME ANALYZER AGENT =====")

analysis = analyze_resume(resume)

print("PASS: Resume Analyzer working")
print(analysis)


print("\n===== RESUME FEEDBACK AGENT =====")

feedback = generate_feedback(analysis)

print("PASS: Resume Feedback working")
print(feedback)