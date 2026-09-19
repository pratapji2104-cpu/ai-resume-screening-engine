from src.tools.job_description_parser import extract_job_requirements


job_description = """
We are looking for a Web Developer.

Required skills:
HTML, CSS, JavaScript, React, Git and SQL.

The candidate should have good knowledge of data structures
and algorithms.
"""


result = extract_job_requirements(job_description)

print("\n===== JOB REQUIREMENTS =====")
print(result)