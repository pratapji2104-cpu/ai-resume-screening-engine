def get_job_requirements(job_role):

    if not job_role or not job_role.strip():
        raise ValueError("Job role is required")

    jobs = {
        "python developer": {
            "required_skills": ["Python", "SQL", "Git"],
            "experience": "0-2 years"
        },
        "web developer": {
            "required_skills": ["HTML", "CSS", "JavaScript"],
            "experience": "0-2 years"
        },
        "software engineer": {
            "required_skills": ["C++", "DSA", "Git"],
            "experience": "0-2 years"
        }
    }

    job_role = job_role.strip().lower()

    if job_role not in jobs:
        raise ValueError("Job role not found")

    result = jobs[job_role]

    if "required_skills" not in result:
        raise ValueError("Job requirements are incomplete")

    return result