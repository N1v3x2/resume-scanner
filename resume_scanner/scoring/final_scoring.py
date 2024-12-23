import json

from ..utils.with_structured_output import with_structured_output
from .schemas import ResumeEvaluation

with open("../config/prompts/final_scoring.txt", "r") as file:
    FINAL_SCORING_TEMPLATE = file.read()
    
def score_resume(resume_info: dict, job_desc: str) -> dict:
    evaluation = with_structured_output(
        prompt=FINAL_SCORING_TEMPLATE.format(resume_info=resume_info, job_info=job_desc),
        schema=ResumeEvaluation
    )
    
    with open("../data/output/resume_evaluation.json", "w") as file:
        json.dump(evaluation, file, indent=4)
        
    return evaluation