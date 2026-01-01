from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="mistralai/devstral-2512:free",
    api_key=OPENAI_API_KEY,
    temperature=0.4
)


def generate_resume_advice(resume_text: str, jd_text: str) -> str:
    """
    Generates actionable improvement suggestions for the resume,
    WITHOUT rewriting it. Uses the new resume_suggestions_prompt.txt.
    """
    prompt = PromptTemplate(
        template=open("prompts/resume_suggestions_prompt.txt").read(),
        input_variables=["resume_text", "jd_text"]
    )

    chain = prompt | llm

    return chain.invoke({
        "resume_text": resume_text,
        "jd_text": jd_text
    }).content


def generate_cover_letter(resume_text: str, jd_text: str) -> str:
    prompt = PromptTemplate(
        template=open("prompts/cover_letter_prompt.txt").read(),
        input_variables=["resume_text", "jd_text"]
    )
    chain = prompt | llm
    return chain.invoke({
        "resume_text": resume_text,
        "jd_text": jd_text
    }).content


def generate_enhanced_resume(resume_text: str, jd_text: str) -> str:
    """
    Rewrites the resume to better match the job description.
    Constraints:
    - Only rephrase existing information
    - Do NOT add new jobs, companies, or years
    - Emphasize skills relevant to the JD
    - Output plain text
    """
    prompt_template = """
You are a resume optimization assistant.

Rewrite the resume to improve alignment with the job description. Rules:
- Do not invent new jobs, companies, or years
- Do not add fake experience
- Only rephrase existing bullets
- Emphasize skills relevant to the job description
- Output plain text

Resume:
{resume_text}

Job Description:
{jd_text}
"""
    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["resume_text", "jd_text"]
    )

    chain = prompt | llm
    return chain.invoke({
        "resume_text": resume_text,
        "jd_text": jd_text
    }).content
