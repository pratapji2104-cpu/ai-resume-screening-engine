from flask import Flask, request, jsonify
from flask_cors import CORS

from src.workflow import run_resume_workflow


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

        data = request.get_json()

        resume = data.get("resume", "")
        job_role = data.get("job_role", "")

        if not resume:

            return jsonify({
                "error": "Resume text is required"
            }), 400

        if not job_role:

            return jsonify({
                "error": "Job role is required"
            }), 400

        result = run_resume_workflow(
            resume,
            job_role
        )

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":

    app.run(
        debug=True
    )