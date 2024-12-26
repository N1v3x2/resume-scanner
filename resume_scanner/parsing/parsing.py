from .initial_parsing import parse_resume_sections
from .section_info_parsing import parse_section_info
from ..schemas.parsing_schemas import ResumeInfo

def parse_resume(resume_path: str) -> ResumeInfo:
    parsed_sections = parse_resume_sections(resume_path)
    parsed_info = parse_section_info(parsed_sections)
    return parsed_info