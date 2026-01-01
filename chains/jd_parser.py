from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from schemas.jd_schema import JDData
import os

import streamlit as st

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="mistralai/devstral-2512:free",
    api_key=OPENAI_API_KEY,
    temperature=0
)

parser = PydanticOutputParser(pydantic_object=JDData)

prompt = PromptTemplate(
    template="{format_instructions}\n{jd_text}",
    input_variables=["jd_text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

def parse_jd(jd_text: str) -> JDData:
    chain = prompt | llm | parser
    return chain.invoke({"jd_text": jd_text})
