import redis
import hashlib
from pydantic import ValidationError

from app.core.utils.decode import decode_with_openai
from app.models.parsing import ResumeInfo
from app.models.scoring import ResumeEvaluation, ResumeWeights, ScoredResume
from app.core.config import WEIGHT_ASSIGNMENT_TXT, FINAL_SCORING_TXT
from app.core.utils.cache_utils import add_to_cache

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
    
def score_resume(resume_info: ResumeInfo, job_desc: str, redis_client: redis.Redis) -> ScoredResume:
    eval_hash: str = hashlib.sha256(
        (resume_info.model_dump_json() + job_desc).encode("utf-8")
    ).hexdigest()
    eval_key = f"eval:{eval_hash}"
    
    try:
        # Check the cache
        final_output = ScoredResume.model_validate_json(
            redis_client.get(eval_key)
        )
    except ValidationError:
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
        
        # Check cache for job description weights
        weights_hash = hashlib.sha256(job_desc.encode("utf-8")).hexdigest()
        weights_key = f"eval:weights:{weights_hash}"
        try:
            weights = ResumeWeights.model_validate_json(
                redis_client.get(weights_key)
            )
        except ValidationError:
            weights: ResumeWeights = decode_with_openai(
                prompt=WEIGHT_ASSIGNMENT_TEMPLATE.format(job_desc=job_desc),
                schema=ResumeWeights
            )
            # Cache the output
            add_to_cache(redis_client, weights_key, weights.model_dump_json())
        
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
        
        # Cache the output
        add_to_cache(redis_client, eval_key, final_output.model_dump_json())
        
    return final_output