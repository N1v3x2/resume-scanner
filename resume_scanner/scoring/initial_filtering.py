from .schemas import MinReq
from ..utils.with_structured_output import with_structured_output

with open("../config/prompts/education_filtering.txt", "r") as file:
    EDUCATION_FILTERING_TEMPLATE = file.read()
with open("../config/prompts/experience_filtering.txt", "r") as file:
    EXPERIENCE_FILTERING_TEMPLATE = file.read()

def meets_min_skills(job_info: dict, resume_info: dict) -> bool:
    job_skills = job_info["Required Skills"]
    if len(job_skills) == 0:
        return True
    
    resume_skills = resume_info["Skills"]["Technical Skills"]
    for skill in job_skills:
        if skill in resume_skills:
            return True
    return False

def filter_min_reqs(job_info: dict, resume_info: dict) -> dict:
    meets_skills = True
    skill_reasoning = "Resume meets minimum skill requirements."
    if not meets_min_skills(job_info, resume_info):
        meets_skills = False
        skill_reasoning = "Resume does not contain any of the required skills."
        
    edu_output = with_structured_output(
        prompt=EDUCATION_FILTERING_TEMPLATE.format(
            resume_edu=resume_info["Education"],
            min_education_req=job_info["Required Education"]),
        schema=MinReq
    )
    meets_education = edu_output["Meets Requirements"]
    education_reasoning = edu_output["Reasoning"]
    
    experience_output = with_structured_output(
        prompt=EXPERIENCE_FILTERING_TEMPLATE.format(
            resume_yoe=resume_info["Work Experience"]["Total Years of Experience"],
            resume_info=resume_info["Skills"]["Technical Skills"] +     
                resume_info["Skills"]["Domain-Specific Skills"],
            min_experience_req=job_info["Required Experience"]),
        schema=MinReq)
    meets_experience = experience_output["Meets Experience"]
    experience_reasoning = experience_output["Reasoning"]
    
    return {
        "Meets Requirements": meets_skills and meets_education and meets_experience,
        "Feedback": [
            skill_reasoning, education_reasoning, experience_reasoning
        ]
    }