import json

from ..utils.decode import decode_with_ollama
from .schemas import ResumeEvaluation

with open("../config/prompts/scoring/weight_assignment.txt", "r") as file:
    WEIGHT_ASSIGNMENT_TEMPLATE = file.read()
with open("../config/prompts/scoring/final_scoring.txt", "r") as file:
    FINAL_SCORING_TEMPLATE = file.read()
    
def score_resume(resume_info: dict, job_desc: str) -> dict:
    evaluation = decode_with_ollama(
        prompt=FINAL_SCORING_TEMPLATE.format(resume_info=resume_info, job_info=job_desc),
        schema=ResumeEvaluation
    )
    
    
    
    with open("../data/output/resume_evaluation.json", "w") as file:
        json.dump(evaluation.model_dump(), file, indent=4)
        
    return evaluation