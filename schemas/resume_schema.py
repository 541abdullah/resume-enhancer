from pydantic import BaseModel
from typing import List

class ResumeData(BaseModel):
    skills: List[str]
    years_experience: int
    roles: List[str]