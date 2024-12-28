import json

from .initial_parsing import parse_resume_sections
from .section_info_parsing import parse_section_info
from ...models.parsing import ResumeInfo

def parse_resume(resume_bytes: bytes) -> ResumeInfo:
    parsed_sections = parse_resume_sections(resume_bytes)
    parsed_info = parse_section_info(parsed_sections)
    
    with open("output.json", "w") as file:
        json.dump(parsed_info.model_dump(), file, indent=4)
    
    return parsed_info