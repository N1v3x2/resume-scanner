from .schemas import MinReq
from ..utils.with_structured_output import with_structured_output

with open("../config/prompts/education_filtering.txt", "r") as file:
    EDUCATION_FILTERING_TEMPLATE = file.read()
with open("../config/prompts/experience_filtering.txt", "r") as file:
    EXPERIENCE_FILTERING_TEMPLATE = file.read()

# TODO: merge minimum education/experience filtering prompts into a single minimum requirements prompt
def filter_min_reqs(resume_info: dict, job_info: str) -> dict:
    edu_output = with_structured_output(
        prompt=EDUCATION_FILTERING_TEMPLATE.format(
            resume_edu=resume_info["Education"],
            min_education_req=job_info),
        schema=MinReq
    )
    meets_education = edu_output["Meets Requirements"]
    education_reasoning = edu_output["Reasoning"]
    
    experience_output = with_structured_output(
        prompt=EXPERIENCE_FILTERING_TEMPLATE.format(
            resume_yoe=resume_info["Work Experience"]["Total Years of Experience"],
            resume_info=resume_info["Skills"]["Technical Skills"] +     
                resume_info["Skills"]["Domain-Specific Skills"],
            min_experience_req=job_info),
        schema=MinReq)
    meets_experience = experience_output["Meets Requirements"]
    experience_reasoning = experience_output["Reasoning"]
    
    return {
        "Meets Requirements": meets_education and meets_experience,
        "Feedback": [
            education_reasoning, experience_reasoning
        ]
    }