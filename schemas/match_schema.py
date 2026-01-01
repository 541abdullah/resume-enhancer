from pydantic import BaseModel
from typing import List

class MatchResult(BaseModel):
    matched_skills: List[str]
    missing_skills: List[str]
    skill_match_percentage: float
    experience_match: bool