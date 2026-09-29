class DecisionAgent:

    def make_decision(self, analysis_result):
        skill_matching = analysis_result.get("skill_matching", {})

        matched_skills = skill_matching.get("matched_skills", [])
        missing_skills = skill_matching.get("missing_skills", [])

        if matched_skills and len(matched_skills) >= len(missing_skills):
            decision = "Suitable"
        else:
            decision = "Needs Improvement"

        return {
            "agent": "DecisionAgent",
            "decision": decision,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        }