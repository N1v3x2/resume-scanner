import pdfplumber

def extract_pdf_text(pdf_path: str) -> str:
    """Extracts text from the provided PDF

    Args:
        `pdf_path` (str): The relative filepath to the PDF

    Returns:
        str: The extracted text. If PDF is an image-based PDF, this will be an empty string.
    """
    
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text