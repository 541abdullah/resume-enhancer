from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from schemas.resume_schema import ResumeData

load_dotenv()

llm = ChatOpenAI(
    model="mistralai/devstral-2512:free",
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
