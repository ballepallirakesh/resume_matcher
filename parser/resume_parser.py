from pdfminer.high_level import extract_text
import os

def extract_resume_text(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"No file found at {pdf_path}")

    try:
        text = extract_text(pdf_path)
        return text.strip()
    except Exception as e:
        print("Error parsing PDF:", e)
        return ""