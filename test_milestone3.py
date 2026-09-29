from src.coordination.agent_coordinator import AgentCoordinator
from src.memory.short_term_memory import ShortTermMemory
from src.memory.long_term_memory import LongTermMemory


print("\n===== TEST 1: AGENT COORDINATION =====")

try:
    coordinator = AgentCoordinator()

    result = coordinator.coordinate(
        "C++ Python HTML CSS Git DSA",
        "web developer",
        {
            "candidate": "Pragya Pratap"
        },
        {
            "job_role": "web developer",
            "requirements": {
                "required_skills": [
                    "HTML",
                    "CSS",
                    "JavaScript"
                ]
            }
        },
        {
            "required_skills": [
                "html",
                "css",
                "javascript"
            ]
        },
        {
            "matched_skills": [
                "HTML",
                "CSS"
            ],
            "missing_skills": [
                "JavaScript"
            ]
        }
    )

    print("PASS: Agent coordination working")
    print("Decision:", result["decision"])


except Exception as e:
    print("FAIL:", e)


print("\n===== TEST 2: SHORT-TERM MEMORY =====")

try:
    memory = ShortTermMemory()

    memory.store(
        "candidate",
        "Pragya Pratap"
    )

    value = memory.retrieve("candidate")

    if value == "Pragya Pratap":
        print("PASS: Short-term memory working")
    else:
        print("FAIL: Short-term memory returned incorrect value")

except Exception as e:
    print("FAIL:", e)


print("\n===== TEST 3: LONG-TERM MEMORY =====")

try:
    memory = LongTermMemory()

    memory.store(
        "job_role",
        "web developer"
    )

    value = memory.retrieve("job_role")

    if value == "web developer":
        print("PASS: Long-term memory working")
    else:
        print("FAIL: Long-term memory returned incorrect value")

except Exception as e:
    print("FAIL:", e)


print("\n===== TEST 4: COLLABORATIVE WORKFLOW =====")

try:
    result = coordinator.coordinate(
        "Python HTML CSS Git",
        "web developer",
        {
            "candidate": "Test Candidate"
        },
        {
            "job_role": "web developer",
            "requirements": {
                "required_skills": [
                    "HTML",
                    "CSS"
                ]
            }
        },
        {
            "required_skills": [
                "html",
                "css"
            ]
        },
        {
            "matched_skills": [
                "HTML",
                "CSS"
            ],
            "missing_skills": []
        }
    )

    if (
        "plan" in result
        and "research" in result
        and "analysis" in result
        and "decision" in result
        and "short_term_memory" in result
        and "long_term_memory" in result
    ):
        print("PASS: Collaborative workflow working")
    else:
        print("FAIL: Collaborative workflow incomplete")

except Exception as e:
    print("FAIL:", e)


print("\n===== MILESTONE 3 VALIDATION COMPLETE =====")