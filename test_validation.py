from src.enterprise_tools import get_job_requirements
from src.tools.job_description_parser import extract_job_requirements


print("\n===== TEST 1: VALID JOB ROLE =====")

try:
    print(get_job_requirements("web developer"))
except ValueError as e:
    print("Error:", e)


print("\n===== TEST 2: UNKNOWN JOB ROLE =====")

try:
    print(get_job_requirements("data scientist"))
except ValueError as e:
    print("Error:", e)


print("\n===== TEST 3: EMPTY JOB ROLE =====")

try:
    print(get_job_requirements(""))
except ValueError as e:
    print("Error:", e)


print("\n===== TEST 4: VALID JOB DESCRIPTION =====")

try:
    print(
        extract_job_requirements(
            "Looking for a developer with Python, SQL and Git."
        )
    )
except ValueError as e:
    print("Error:", e)


print("\n===== TEST 5: EMPTY JOB DESCRIPTION =====")

try:
    print(extract_job_requirements(""))
except ValueError as e:
    print("Error:", e)


print("\n===== TEST 6: NO SUPPORTED SKILLS =====")

try:
    print(
        extract_job_requirements(
            "Looking for a highly motivated candidate."
        )
    )
except ValueError as e:
    print("Error:", e)