from pydantic import BaseModel, RootModel

from .initial_parsing import parse_resume_sections
from .section_info_parsing import parse_section_info

def parse_resume(resume_path: str) -> (BaseModel | RootModel):
    parsed_sections = parse_resume_sections(resume_path)
    parsed_info = parse_section_info(parsed_sections)
    return parsed_info