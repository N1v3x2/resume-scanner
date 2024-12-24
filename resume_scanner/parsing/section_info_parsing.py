import json
from concurrent.futures import ThreadPoolExecutor, as_completed

from ..utils.with_structured_output import with_structured_output
from .schemas import Education, Experiences, Projects, Research, Leadership, Skills

with open("../config/prompts/parsing/education_extraction.txt", "r") as file:
    EDUCATION_EXTRACTION_TEMPLATE = file.read()
with open("../config/prompts/parsing/experience_extraction.txt", "r") as file:
    EXPERIENCE_EXTRACTION_TEMPLATE = file.read()
with open("../config/prompts/parsing/projects_extraction.txt", "r") as file:
    PROJECTS_EXTRACTION_TEMPLATE = file.read()
with open("../config/prompts/parsing/leadership_extraction.txt", "r") as file:
    LEADERSHIP_EXTRACTION_TEMPLATE = file.read()
with open("../config/prompts/parsing/research_extraction.txt", "r") as file:
    RESEARCH_EXTRACTION_TEMPLATE = file.read()
with open("../config/prompts/parsing/skills_extraction.txt", "r") as file:
    SKILLS_EXTRACTION_TEMPLATE = file.read()

def parse_section_info(resume_sections: dict) -> dict:
    parsed_info = {}
    
    with ThreadPoolExecutor() as executor:
        futures = {}
        
        if resume_sections["Education"]:
            futures[executor.submit(
                with_structured_output,
                prompt=EDUCATION_EXTRACTION_TEMPLATE.format(resume_text=resume_sections["Education"]), 
                schema=Education
            )] = "Education"
        
        if resume_sections["Experience"]:
            futures[executor.submit(
                with_structured_output,
                prompt=EXPERIENCE_EXTRACTION_TEMPLATE.format(resume_text=resume_sections["Experience"]),
                schema=Experiences
            )] = "Work Experience"
        
        if resume_sections["Projects"]:
            futures[executor.submit(
                with_structured_output,
                prompt=PROJECTS_EXTRACTION_TEMPLATE.format(resume_text=resume_sections["Projects"]),
                schema=Projects
            )] = "Projects"
        
        if resume_sections["Leadership"]:
            futures[executor.submit(
                with_structured_output,
                prompt=LEADERSHIP_EXTRACTION_TEMPLATE.format(resume_text=resume_sections["Leadership"]),
                schema=Leadership
            )] = "Leadership"
        
        if resume_sections["Research"]:
            futures[executor.submit(
                with_structured_output,
                prompt=RESEARCH_EXTRACTION_TEMPLATE.format(resume_text=resume_sections["Research"]),
                schema=Research
            )] = "Research"
            
        if resume_sections["Skills"]:
            futures[executor.submit(
                with_structured_output,
                prompt=SKILLS_EXTRACTION_TEMPLATE.format(resume_text=resume_sections["Skills"]),
                schema=Skills
            )] = "Skills"
        
        for future in as_completed(futures):
            try:
                category = futures[future]
                parsed_info[category] = future.result(timeout=80)
            except Exception as e:
                print(f"Error when parsing resume section info: {e}")
    
    with open("../data/output/parsed_resume_info.json", "w") as file:
        json.dump(parsed_info, file, indent=4)
    
    return parsed_info
