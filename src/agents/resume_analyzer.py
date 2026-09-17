import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

resume_prompt = ChatPromptTemplate.from_template("""
You are a Resume Analyzer Agent.

Analyze the following resume.

Return a simple and concise analysis using ONLY these sections:

Candidate:
- Name

Education:
- Short summary

Skills:
- Important skills

Experience:
- Short summary

Projects:
- Short summary

Missing or Weak Areas:
- Short points

Rules:
- Keep the answer concise.
- Use bullet points.
- Do not add unnecessary explanations.
- Do not invent information.

Resume:
{resume}
""")


def extract_text(response):
    content = response.content

    # If response is already a string
    if isinstance(content, str):
        return content

    # If Gemini returns a list of content blocks
    if isinstance(content, list):
        texts = []

        for item in content:
            if isinstance(item, dict) and "text" in item:
                texts.append(item["text"])

            elif hasattr(item, "text"):
                texts.append(item.text)

        if texts:
            return "\n".join(texts)

    return str(content)


def analyze_resume(resume_text: str) -> str:
    prompt = resume_prompt.format(
        resume=resume_text
    )

    response = llm.invoke(prompt)

    return extract_text(response)