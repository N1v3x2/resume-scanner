import json

from ..utils.decode import decode_with_openai
from ..schemas.parsing_schemas import ResumeInfo
from ..schemas.scoring_schemas import ResumeEvaluation, ResumeWeights, FinalOutput

with open("../config/prompts/scoring/weight_assignment.txt", "r") as file:
    WEIGHT_ASSIGNMENT_TEMPLATE = file.read()
with open("../config/prompts/scoring/final_scoring.txt", "r") as file:
    FINAL_SCORING_TEMPLATE = file.read()
    
    
def calculate_score(eval_data, weight):
    """
    Helper function to calculate a weighted score for a category.
    """
    depth = getattr(eval_data, "depth", 0)
    impact = getattr(eval_data, "impact", 0)
    relevance = getattr(eval_data, "relevance", 1)
    alignment = getattr(eval_data, "alignment", 0)

    # Determine the score formula based on available attributes
    if hasattr(eval_data, "alignment"):
        return (alignment / 5) * weight
    else:
        return (depth + impact) / 10 * (relevance / 5)  * weight
    
    
def score_resume(resume_info: ResumeInfo, job_desc: str) -> FinalOutput:
    eval: ResumeEvaluation = decode_with_openai(
        prompt=FINAL_SCORING_TEMPLATE.format(resume_info=resume_info, job_info=job_desc),
        schema=ResumeEvaluation
    )
    
    weights: ResumeWeights = decode_with_openai(
        prompt=WEIGHT_ASSIGNMENT_TEMPLATE.format(job_desc=job_desc),
        schema=ResumeWeights
    )
    
    categories = {
        "education": (eval.education, weights.education),
        "experience": (eval.experience, weights.experience),
        "projects": (eval.projects, weights.projects),
        "research": (eval.research, weights.research),
        "leadership": (eval.leadership, weights.leadership),
        "skills": (eval.skills, weights.skills),
    }

    final_score = sum(calculate_score(eval_data, weight) for eval_data, weight in categories.values())
    
    final_output = FinalOutput(resume_eval=eval, resume_weights=weights, final_score=final_score)
    
    with open("../data/output/resume_evaluation.json", "w") as file:
        json.dump(final_output.model_dump(), file, indent=4)
        
    return final_output