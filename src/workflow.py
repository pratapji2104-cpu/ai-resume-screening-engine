from src.agents.resume_analyzer import analyze_resume
from src.agents.resume_feedback import generate_feedback
from src.agents.job_agent import get_job_info


def run_resume_workflow(resume_text: str, job_role: str) -> dict:

    # Step 1: Analyze resume
    analysis = analyze_resume(resume_text)

    # Step 2: Get job requirements
    job_info = get_job_info(job_role)

    # Step 3: Generate short feedback
    feedback = generate_feedback(analysis)

    return {
        "analysis": analysis,
        "job_info": job_info,
        "feedback": feedback
    }