import json

from .schemas import JobDescription
from ..utils.with_structured_output import with_structured_output

with open("../config/prompts/job_description_extraction.txt", "r") as file:
    JOB_DESC_EXTRACTION_TEMPLATE = file.read()
    
def parse_job_desc(job_path: str) -> dict:
    with open(job_path, "r") as file:
        job_desc = file.read()
    
    job_info = with_structured_output(
        prompt=JOB_DESC_EXTRACTION_TEMPLATE.format(job_desc=job_desc),
        schema=JobDescription)
    
    with open("../data/output/parsed_job_desc.json", "w") as file:
        json.dump(job_desc, file, indent=4)
        
    return job_info