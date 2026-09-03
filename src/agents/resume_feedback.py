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

Give very simple and concise feedback on this resume analysis.

Provide only:
1. 2 strengths
2. 2 weaknesses
3. 3 improvement suggestions

Use short bullet points.
Do not explain in detail.
Do not invent information.

Resume Analysis:
{analysis}
""")

def generate_feedback(analysis: str) -> str:
    prompt = feedback_prompt.format(analysis=analysis)
    response = llm.invoke(prompt)
    return response.content