import PyPDF2
import re

def extract_resume_text(file):
    # reader = PyPDF2.PdfReader(file)
    reader = PyPDF2.PdfReader(file)
    if len(reader.pages) == 0:
        return ""
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "

    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()