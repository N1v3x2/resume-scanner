from app.core.parsing.initial_parsing import parse_resume_sections
from app.core.parsing.section_info_parsing import parse_section_info
from app.models.parsing import ResumeInfo

def parse_resume(resume_bytes: bytes) -> ResumeInfo:
    parsed_sections = parse_resume_sections(resume_bytes)
    parsed_info = parse_section_info(parsed_sections)
    return parsed_info