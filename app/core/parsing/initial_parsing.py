from pdf2image import convert_from_bytes
from pytesseract import pytesseract
import io

from app.core.utils.decode import decode_with_openai
from app.core.utils.extract_pdf_text import extract_pdf_text
from app.models.parsing import Resume
from app.core.config import INITIAL_EXTRACTION_TXT

with open(INITIAL_EXTRACTION_TXT, "r") as file:
    INITIAL_EXTRACTION_TEMPLATE = file.read()

def parse_resume_sections(resume_bytes: bytes) -> Resume:
    pdf_file_like = io.BytesIO(resume_bytes)
    
    resume = extract_pdf_text(pdf_file_like)
    
    # If unable to directly extract text from image-based PDF
    if not resume:
        pdf_images = convert_from_bytes(resume_bytes, dpi=300)
        resume = pytesseract.image_to_string(pdf_images[0])
    
    parsed_sections: Resume = decode_with_openai(
        prompt=INITIAL_EXTRACTION_TEMPLATE.format(resume_text=resume),
        schema=Resume
    )
    
    return parsed_sections