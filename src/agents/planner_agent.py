class PlannerAgent:

    def create_plan(self, resume_text, job_role):
        return {
            "agent": "PlannerAgent",
            "task": "Resume screening",
            "steps": [
                "Analyze resume",
                "Identify job requirements",
                "Match candidate skills",
                "Generate final decision"
            ],
            "resume": resume_text,
            "job_role": job_role
        }