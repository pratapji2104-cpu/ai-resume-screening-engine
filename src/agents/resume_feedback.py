import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

feedback_prompt = ChatPromptTemplate.from_template("""
You are a Resume Feedback Agent.

Review the resume analysis below and provide concise, actionable
recommendations to improve the candidate's resume.

Focus on:
1. Missing information
2. Skills that could be improved
3. Project improvements
4. Experience improvements
5. Overall recommendations

Do not invent candidate information.

Resume Analysis:
{analysis}
""")


def generate_feedback(analysis: str) -> str:
    prompt = feedback_prompt.format(analysis=analysis)
    response = llm.invoke(prompt)
    return response.content