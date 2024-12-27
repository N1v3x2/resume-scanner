from .initial_parsing import parse_resume_sections
from .section_info_parsing import parse_section_info
from ...models.parsing import ResumeInfo

def parse_resume(b64_encoded_resume: bytes) -> ResumeInfo:
    parsed_sections = parse_resume_sections(b64_encoded_resume)
    parsed_info = parse_section_info(parsed_sections)
    return parsed_info