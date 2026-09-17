async function analyzeResume() {

    const resume = document.getElementById("resume").value.trim();
    const jobRole = document.getElementById("jobRole").value.trim();

    const loading = document.getElementById("loading");
    const error = document.getElementById("error");
    const results = document.getElementById("results");

    if (!resume || !jobRole) {
        error.textContent = "Please enter both resume and job role.";
        results.style.display = "none";
        return;
    }

    loading.textContent = "Analyzing resume...";
    error.textContent = "";
    results.style.display = "none";

    try {

        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                resume: resume,
                job_role: jobRole
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong");
        }

        // Resume Analysis
        document.getElementById("analysis").textContent =
            data.analysis || "No analysis available.";

        // Job Requirements
        if (data.job_info && data.job_info.error) {

            document.getElementById("jobRequirements").textContent =
                "Error: " + data.job_info.error;

        } else {

            document.getElementById("jobRequirements").textContent =
                JSON.stringify(data.job_info, null, 2);
        }

        // AI Feedback
        document.getElementById("feedback").textContent =
            data.feedback || "No feedback available.";

        results.style.display = "block";

    } catch (err) {

        error.textContent = "Error: " + err.message;

    } finally {

        loading.textContent = "";
    }
}