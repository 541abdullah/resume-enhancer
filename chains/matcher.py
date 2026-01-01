from schemas.match_schema import MatchResult
from schemas.resume_schema import ResumeData
from schemas.jd_schema import JDData


def normalize(skill: str) -> str:
    return (
        skill.lower()
        .replace(".", "")
        .replace("-", "")
        .replace(" ", "")
        .strip()
    )


def match_resume_to_jd(resume: ResumeData, jd: JDData) -> MatchResult:
    resume_skills = {normalize(skill) for skill in resume.skills}
    required_skills = {normalize(skill) for skill in jd.required_skills}

    matched = resume_skills.intersection(required_skills)
    missing = required_skills.difference(resume_skills)

    skill_match_percentage = (
        len(matched) / len(required_skills) * 100
        if required_skills else 0
    )

    experience_match = resume.years_experience >= jd.min_experience

    return MatchResult(
        matched_skills=sorted(matched),
        missing_skills=sorted(missing),
        skill_match_percentage=round(skill_match_percentage, 2),
        experience_match=experience_match
    )
