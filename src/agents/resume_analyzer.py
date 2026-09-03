import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

prompt_template = ChatPromptTemplate.from_template("""
You are a Resume Analysis Agent.

Analyze the candidate's resume and provide a structured analysis.

Extract the following information:

1. Candidate Name
2. Technical Skills
3. Education
4. Work Experience
5. Projects
6. Certifications
7. Overall Strengths
8. Areas that need improvement

Keep the analysis concise and factual.
Do not invent information that is not present in the resume.

Resume:
{resume_text}
""")


def analyze_resume(resume_text: str) -> str:
    prompt = prompt_template.format(resume_text=resume_text)

    response = llm.invoke(prompt)

    return response.content