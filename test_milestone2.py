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

Knowledge of data structures and algorithms is preferred.
"""


print("\n===== TEST 1: COMPLETE WORKFLOW =====")

try:
    result = run_resume_workflow(
        resume,
        "web developer",
        job_description
    )

    print("PASS: Workflow completed successfully")

    print("\nSkill Matching:")
    print(result["skill_matching"])

except Exception as e:
    print("FAIL:", e)


print("\n===== TEST 2: UNKNOWN JOB ROLE =====")

try:
    result = run_resume_workflow(
        resume,
        "data scientist",
        job_description
    )

    print("PASS: Error handled")
    print(result["job_info"])

except Exception as e:
    print("FAIL:", e)


print("\n===== TEST 3: EMPTY JOB DESCRIPTION =====")

try:
    result = run_resume_workflow(
        resume,
        "web developer",
        ""
    )

    print("PASS: Workflow handled empty job description")

    print("\nSkill Matching:")
    print(result["skill_matching"])

except Exception as e:
    print("FAIL:", e)


print("\n===== TEST 4: EMPTY JOB ROLE =====")

try:
    result = run_resume_workflow(
        resume,
        "",
        job_description
    )

    print("Result:")
    print(result["job_info"])

except Exception as e:
    print("PASS: Error handled")
    print("Error:", e)