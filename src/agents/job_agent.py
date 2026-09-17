from src.enterprise_tools import get_job_requirements


def get_job_info(job_role):

    try:

        requirements = get_job_requirements(job_role)

        return {
            "job_role": job_role,
            "requirements": requirements
        }

    except ValueError as e:

        return {
            "error": str(e)
        }