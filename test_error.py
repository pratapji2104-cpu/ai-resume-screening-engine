from src.agents.tool_selector import execute_request

result = execute_request(
    "Show me the job requirements",
    "data scientist"
)

print("===== ERROR HANDLING RESULT =====")
print(result)