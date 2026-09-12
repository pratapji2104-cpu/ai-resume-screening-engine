def get_job_requirements(job_role):
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

    job_role = job_role.lower()

    if job_role not in jobs:
        raise ValueError("Job role not found")

    return jobs[job_role]