from src.agents.resume_analyzer import analyze_resume

resume = """
Pragya Pratap
Computer Science Engineering student.

Skills:
C++, Python, HTML, CSS, JavaScript, DSA.

Projects:
To-Do Web Application using HTML, CSS and JavaScript.
"""

result = analyze_resume(resume)

print("\n===== RESUME ANALYSIS =====\n")
print(result)