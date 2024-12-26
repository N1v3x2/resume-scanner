from pdf2image import convert_from_path
from pytesseract import pytesseract

from ..utils.decode import decode_with_ollama
from ..utils.extract_pdf_text import extract_pdf_text
from ..schemas.parsing_schemas import Resume

with open("../config/prompts/parsing/initial_extraction.txt", "r") as file:
    INITIAL_EXTRACTION_TEMPLATE = file.read()

def parse_resume_sections(resume_path: str) -> Resume:
    resume = extract_pdf_text(resume_path)
    
    # If unable to directly extract text from image-based PDF
    if not resume:
        pdf_images = convert_from_path(resume_path, dpi=300)
        resume = pytesseract.image_to_string(pdf_images[0])
    
    parsed_sections: Resume = decode_with_ollama(
        prompt=INITIAL_EXTRACTION_TEMPLATE.format(resume_text=resume),
        schema=Resume
    )
    
    return parsed_sections