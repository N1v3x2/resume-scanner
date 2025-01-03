import redis
import hashlib
from pydantic import ValidationError

from app.core.parsing.initial_parsing import parse_resume_sections
from app.core.parsing.section_info_parsing import parse_section_info
from app.models.parsing import ResumeInfo
from app.core.utils.cache_utils import add_to_cache

def parse_resume(resume_bytes: bytes, redis_client: redis.Redis) -> ResumeInfo:
    resume_hash: str = hashlib.sha256(resume_bytes).hexdigest()
    resume_key = f"resume:{resume_hash}"
    
    try:
        # Check cache
        parsed_info = ResumeInfo.model_validate_json(
            redis_client.get(resume_key)
        )
    except ValidationError:
        parsed_sections = parse_resume_sections(resume_bytes)
        parsed_info = parse_section_info(parsed_sections)
        add_to_cache(redis_client, resume_key, parsed_info.model_dump_json())
    
    return parsed_info