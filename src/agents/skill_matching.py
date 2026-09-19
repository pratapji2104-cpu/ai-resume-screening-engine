def match_skills(resume_text, required_skills):

    resume_text = resume_text.lower()

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in resume_text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }