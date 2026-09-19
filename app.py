from flask import Flask, request, jsonify
from flask_cors import CORS

from src.workflow import run_resume_workflow
from src.tools.pdf_parser import extract_text_from_pdf

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "AI Resume Screening Engine API is running"
    })


@app.route("/analyze", methods=["POST"])
def analyze_resume():

    try:
        job_role = request.form.get("job_role", "").strip()

        if not job_role:
            return jsonify({
                "error": "Job role is required"
            }), 400

        # PDF resume upload
        if "resume_file" in request.files:

            resume_file = request.files["resume_file"]

            if resume_file.filename == "":
                return jsonify({
                    "error": "Please select a resume PDF"
                }), 400

            if not resume_file.filename.lower().endswith(".pdf"):
                return jsonify({
                    "error": "Only PDF resumes are supported"
                }), 400

            resume = extract_text_from_pdf(resume_file)

        # Resume text input
        else:

            resume = request.form.get("resume", "").strip()

            if not resume:
                return jsonify({
                    "error": "Resume text or PDF is required"
                }), 400

        # Run existing AI workflow
        result = run_resume_workflow(resume, job_role)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)