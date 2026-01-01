from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from schemas.resume_schema import ResumeData

import streamlit as st

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")


llm = ChatOpenAI(
    model="mistralai/devstral-2512:free",
    api_key=OPENAI_API_KEY,
    temperature=0
)

parser = PydanticOutputParser(pydantic_object=ResumeData)

prompt = PromptTemplate(
    template="{format_instructions}\n{resume_text}",
    input_variables=["resume_text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

def parse_resume(resume_text: str) -> ResumeData:
    chain = prompt | llm | parser
    return chain.invoke({"resume_text": resume_text})
