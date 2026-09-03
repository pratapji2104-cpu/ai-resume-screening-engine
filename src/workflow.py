from src.agents.resume_analyzer import analyze_resume
from src.agents.resume_feedback import generate_feedback


def run_resume_workflow(resume_text: str) -> dict:
    # Step 1: Analyze the resume
    analysis = analyze_resume(resume_text)

    # Step 2: Generate feedback using the analysis
    feedback = generate_feedback(analysis)

    return {
        "analysis": analysis,
        "feedback": feedback
    }