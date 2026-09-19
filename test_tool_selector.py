from src.agents.tool_selector import select_tool, execute_request


print("\n===== TEST 1: JOB REQUIREMENTS =====")

request1 = "Show me the job requirements"

print("Selected Tool:")
print(select_tool(request1))

print("Result:")
print(
    execute_request(
        request1,
        job_role="web developer"
    )
)


print("\n===== TEST 2: JOB DESCRIPTION =====")

request2 = "Extract skills from the job description"

job_description = """
We are looking for a Web Developer.

Required skills:
HTML, CSS, JavaScript, React and Git.
"""

print("Selected Tool:")
print(select_tool(request2))

print("Result:")
print(
    execute_request(
        request2,
        job_description=job_description
    )
)


print("\n===== TEST 3: NO TOOL =====")

request3 = "Hello, how are you?"

print("Selected Tool:")
print(select_tool(request3))