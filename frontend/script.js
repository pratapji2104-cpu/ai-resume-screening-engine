async function analyzeResume() {

    const jobRole = document.getElementById("jobRole").value.trim();
    const resumeFile = document.getElementById("resumeFile").files[0];

    const loading = document.getElementById("loading");
    const error = document.getElementById("error");

    loading.textContent = "Analyzing resume...";
    error.textContent = "";

    if (!jobRole) {
        error.textContent = "Please enter a job role.";
        loading.textContent = "";
        return;
    }

    if (!resumeFile) {
        error.textContent = "Please upload a PDF resume.";
        loading.textContent = "";
        return;
    }

    if (!resumeFile.name.toLowerCase().endsWith(".pdf")) {
        error.textContent = "Only PDF resumes are supported.";
        loading.textContent = "";
        return;
    }

    const formData = new FormData();

    formData.append("job_role", jobRole);
    formData.append("resume_file", resumeFile);

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/analyze",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong");
        }

        document.getElementById("analysis").textContent =
            typeof data.analysis === "string"
                ? data.analysis
                : JSON.stringify(data.analysis, null, 2);

        document.getElementById("jobRequirements").textContent =
            JSON.stringify(data.job_info, null, 2);

        document.getElementById("feedback").textContent =
            typeof data.feedback === "string"
                ? data.feedback
                : JSON.stringify(data.feedback, null, 2);

        document.getElementById("results").style.display = "block";

    } catch (err) {

        error.textContent = err.message;

    } finally {

        loading.textContent = "";
    }
}