from app.core.utils.decode import decode_with_openai
from app.models.parsing import ResumeInfo
from app.models.scoring import ResumeEvaluation, ResumeWeights, ScoredResume
from app.core.config import WEIGHT_ASSIGNMENT_TXT, FINAL_SCORING_TXT

with open(WEIGHT_ASSIGNMENT_TXT, "r") as file:
    WEIGHT_ASSIGNMENT_TEMPLATE = file.read()
with open(FINAL_SCORING_TXT, "r") as file:
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
    
    
def score_resume(resume_info: ResumeInfo, job_desc: str) -> ScoredResume:
    DEFAULT = "Unavailable."
    eval: ResumeEvaluation = decode_with_openai(
        prompt=FINAL_SCORING_TEMPLATE.format(
            job_desc=job_desc,
            experience=getattr(resume_info, "experience", DEFAULT),
            education=getattr(resume_info, "education", DEFAULT),
            projects=getattr(resume_info, "projects", DEFAULT),
            leadership=getattr(resume_info, "leadership", DEFAULT),
            research=getattr(resume_info, "research", DEFAULT),
            skills=getattr(resume_info, "skills", DEFAULT)
        ),
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
    final_score = round(final_score, 2)
    final_output = ScoredResume(resume_eval=eval, resume_weights=weights, final_score=final_score)
    
    # TODO: cache query results
    # with open("../data/output/resume_evaluation.json", "w") as file:
    #     json.dump(final_output.model_dump(), file, indent=4)
        
    return final_output