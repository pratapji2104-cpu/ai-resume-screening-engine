from src.enterprise_tools import get_job_requirements


def select_tool(user_request):

    request = user_request.lower()

    if "job" in request or "requirements" in request or "skills" in request:
        return "get_job_requirements"

    return "no_tool"


def execute_request(user_request, job_role):

    selected_tool = select_tool(user_request)

    if selected_tool == "get_job_requirements":

        try:
            return get_job_requirements(job_role)

        except ValueError as e:
            return {
                "error": str(e)
            }

    return {
        "message": "No enterprise tool required"
    }