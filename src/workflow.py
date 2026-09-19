from src.agents.resume_analyzer import analyze_resume
from src.agents.resume_feedback import generate_feedback
from src.agents.job_agent import get_job_info
from src.agents.skill_matching import match_skills
from src.tools.job_description_parser import extract_job_requirements


def run_resume_workflow(
    resume_text: str,
    job_role: str,
    job_description: str = ""
) -> dict:

    # Step 1: Analyze the resume
    analysis = analyze_resume(resume_text)

    # Step 2: Get job requirements from enterprise tool
    job_info = get_job_info(job_role)

    # Step 3: Extract skills from job description if provided
    job_description_requirements = {}

    if job_description.strip():
        try:
            job_description_requirements = extract_job_requirements(
                job_description
            )
        except ValueError as e:
            job_description_requirements = {
                "error": str(e)
            }

    # Step 4: Determine skills to match
    if job_description_requirements.get("required_skills"):
        required_skills = job_description_requirements["required_skills"]

    elif "requirements" in job_info:
        required_skills = job_info["requirements"].get(
            "required_skills",
            []
        )

    else:
        required_skills = []

    # Step 5: Match resume skills with required skills
    skill_matching = match_skills(
        resume_text,
        required_skills
    )

    # Step 6: Generate resume feedback
    feedback = generate_feedback(analysis)

    return {
        "analysis": analysis,
        "job_info": job_info,
        "job_description_requirements": job_description_requirements,
        "skill_matching": skill_matching,
        "feedback": feedback
    }