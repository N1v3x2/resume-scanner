import pdfplumber
from io import BytesIO

def extract_pdf_text(resume_pdf: BytesIO) -> str:
    """Extracts text from the provided PDF

    Args:
        `resume_pdf` (BytesIO): A PDF-like bytes representation of the resume.

    Returns:
        str: The extracted text. If PDF is an image-based PDF, this will be an empty string.
    """
    
    with pdfplumber.open(resume_pdf) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text