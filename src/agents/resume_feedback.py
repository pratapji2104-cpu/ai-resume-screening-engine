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

Give very short and simple feedback based only on the resume analysis.

Return ONLY this format:

Strengths:
- Short point
- Short point

Weaknesses:
- Short point
- Short point

Suggestions:
- Short point
- Short point

Rules:
- Keep every point to one short sentence.
- Do not add explanations.
- Do not add extra sections.
- Do not invent information.

Resume Analysis:
{analysis}
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


def generate_feedback(analysis: str) -> str:
    prompt = feedback_prompt.format(
        analysis=analysis
    )

    response = llm.invoke(prompt)

    return extract_text(response)