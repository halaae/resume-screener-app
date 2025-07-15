# resume_parser.py

from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_file_path):
    try:
        text = extract_text(pdf_file_path)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""
