import json
from concurrent.futures import ThreadPoolExecutor, as_completed

from ..utils.decode import decode_with_openai
from ...models.parsing import Resume, Education, Experiences, Projects, Research, Leadership, Skills, ResumeInfo

with open("config/prompts/parsing/education_extraction.txt", "r") as file:
    EDUCATION_EXTRACTION_TEMPLATE = file.read()
with open("config/prompts/parsing/experience_extraction.txt", "r") as file:
    EXPERIENCE_EXTRACTION_TEMPLATE = file.read()
with open("config/prompts/parsing/projects_extraction.txt", "r") as file:
    PROJECTS_EXTRACTION_TEMPLATE = file.read()
with open("config/prompts/parsing/leadership_extraction.txt", "r") as file:
    LEADERSHIP_EXTRACTION_TEMPLATE = file.read()
with open("config/prompts/parsing/research_extraction.txt", "r") as file:
    RESEARCH_EXTRACTION_TEMPLATE = file.read()
with open("config/prompts/parsing/skills_extraction.txt", "r") as file:
    SKILLS_EXTRACTION_TEMPLATE = file.read()

def parse_section_info(resume_sections: Resume) -> ResumeInfo:
    parsed_info = ResumeInfo()
    
    with ThreadPoolExecutor() as executor:
        futures = {}

        if resume_sections.education:
            futures[executor.submit(
                decode_with_openai,
                prompt=EDUCATION_EXTRACTION_TEMPLATE.format(resume_text=resume_sections.education), 
                schema=Education
            )] = "education"
        
        if resume_sections.experience:
            futures[executor.submit(
                decode_with_openai,
                prompt=EXPERIENCE_EXTRACTION_TEMPLATE.format(resume_text=resume_sections.experience),
                schema=Experiences
            )] = "experience"
        
        if resume_sections.projects:
            futures[executor.submit(
                decode_with_openai,
                prompt=PROJECTS_EXTRACTION_TEMPLATE.format(resume_text=resume_sections.projects),
                schema=Projects
            )] = "projects"
        
        if resume_sections.leadership:
            futures[executor.submit(
                decode_with_openai,
                prompt=LEADERSHIP_EXTRACTION_TEMPLATE.format(resume_text=resume_sections.leadership),
                schema=Leadership
            )] = "leadership"
        
        if resume_sections.research:
            futures[executor.submit(
                decode_with_openai,
                prompt=RESEARCH_EXTRACTION_TEMPLATE.format(resume_text=resume_sections.research),
                schema=Research
            )] = "research"
            
        if resume_sections.skills:
            futures[executor.submit(
                decode_with_openai,
                prompt=SKILLS_EXTRACTION_TEMPLATE.format(resume_text=resume_sections.skills),
                schema=Skills
            )] = "skills"
        
        for future in as_completed(futures):
            try:
                section = futures[future]
                parsed_data = future.result(timeout=60)
                
                # Handle "root" models with only a `data` attribute
                if hasattr(parsed_info, "data"):
                    parsed_data = parsed_data.data
                
                setattr(parsed_info, section, parsed_data)
            except Exception as e:
                print(f"Error when parsing resume section info: {e}")
    
    # TODO: cache query results
    # with open("../data/output/parsed_resume_info.json", "w") as file:
    #     json.dump(parsed_info.model_dump(), file, indent=4)
    
    return parsed_info
