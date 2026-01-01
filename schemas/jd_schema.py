from pydantic import BaseModel
from typing import List

class JDData(BaseModel):
    required_skills: List[str]
    preferred_skills: List[str]
    min_experience: int
    role_title: str