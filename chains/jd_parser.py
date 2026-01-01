from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from schemas.jd_schema import JDData

load_dotenv()

llm = ChatOpenAI(
    model="mistralai/devstral-2512:free",
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
