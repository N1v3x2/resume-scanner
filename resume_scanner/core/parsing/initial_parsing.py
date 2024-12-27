from pdf2image import convert_from_bytes
from pytesseract import pytesseract
import base64
import io

from ..utils.decode import decode_with_openai
from ..utils.extract_pdf_text import extract_pdf_text
from ...models.parsing import Resume

with open("config/prompts/parsing/initial_extraction.txt", "r") as file:
    INITIAL_EXTRACTION_TEMPLATE = file.read()

def parse_resume_sections(b64_encoded_resume: bytes) -> Resume:
    pdf_file_like = io.BytesIO(b64_encoded_resume)
    
    resume = extract_pdf_text(pdf_file_like)
    
    # If unable to directly extract text from image-based PDF
    if not resume:
        pdf_images = convert_from_bytes(b64_encoded_resume, dpi=300)
        resume = pytesseract.image_to_string(pdf_images[0])
    
    parsed_sections: Resume = decode_with_openai(
        prompt=INITIAL_EXTRACTION_TEMPLATE.format(resume_text=resume),
        schema=Resume
    )
    
    return parsed_sections