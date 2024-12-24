from pdf2image import convert_from_path
from pytesseract import pytesseract

from ..utils.with_structured_output import with_structured_output
from ..utils.extract_pdf_text import extract_pdf_text
from .schemas import Resume

with open("../config/prompts/parsing/initial_extraction.txt", "r") as file:
    INITIAL_EXTRACTION_TEMPLATE = file.read()

def parse_resume_sections(resume_path: str) -> dict:
    resume = extract_pdf_text(resume_path)
    
    # Unable to directly extract text from image-based PDF
    if not resume:
        pdf_images = convert_from_path(resume_path, dpi=300)
        resume = pytesseract.image_to_string(pdf_images[0])
    
    parsed_sections = with_structured_output(
        prompt=INITIAL_EXTRACTION_TEMPLATE.format(resume_text=resume),
        schema=Resume
    )
    return parsed_sections