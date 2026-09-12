from src.agents.tool_selector import execute_request

result = execute_request(
    "Show me the skills required for this job",
    "web developer"
)

print("===== TOOL SELECTION RESULT =====")
print(result)