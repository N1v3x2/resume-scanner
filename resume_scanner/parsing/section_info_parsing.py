import json
from concurrent.futures import ThreadPoolExecutor, as_completed

from ..utils.with_structured_output import with_structured_output
from .schemas import Education, Experiences, Skills

with open("../config/prompts/education_extraction.txt", "r") as file:
    EDUCATION_EXTRACTION_TEMPLATE = file.read()
with open("../config/prompts/experience_extraction.txt", "r") as file:
    EXPERIENCE_EXTRACTION_TEMPLATE = file.read()
with open("../config/prompts/skill_extraction.txt", "r") as file:
    SKILL_EXTRACTION_TEMPLATE = file.read()

def parse_section_info(parsed_resume_sections: dict) -> dict:
    parsed_info = {}
    
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(
                with_structured_output,
                prompt=EDUCATION_EXTRACTION_TEMPLATE.format(resume_text=parsed_resume_sections["Education"]), 
                schema=Education
            ) : "Education",
            executor.submit(
                with_structured_output,
                prompt=EXPERIENCE_EXTRACTION_TEMPLATE.format(resume_text=parsed_resume_sections["Experience"]),
                schema=Experiences
            ) : "Work Experience",
            executor.submit(
                with_structured_output,
                prompt=SKILL_EXTRACTION_TEMPLATE.format(
                    resume_text=parsed_resume_sections["Experience"]
                        + parsed_resume_sections["Projects"]
                        + parsed_resume_sections["Skills"]
                        + parsed_resume_sections["Research"]
                        + parsed_resume_sections["Leadership"]),
                schema=Skills
            ) : "Skills"
        }
        for future in as_completed(futures):
            try:
                category = futures[future]
                parsed_info[category] = future.result(timeout=80)
            except Exception as e:
                print(f"Error when parsing resume section info: {e}")
    
    with open("../data/output/parsed_resume_info.json", "w") as file:
        json.dump(parsed_info, file, indent=4)
    
    return parsed_info
