import streamlit as st
from jd_matcher import get_match_score, extract_missing_skills
from pdfminer.high_level import extract_text
from pdf2image import convert_from_path
import pytesseract
import tempfile
import os

st.set_page_config(page_title="AI Resume Screener", layout="centered")

st.title("📄 AI Resume Screener + Matcher")
st.write("Upload your resume and paste a job description to see your match score and missing skills.")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_input = st.text_area("Paste Job Description Here")

# ---- Resume Text Extractor (OCR + Normal) ----
def extract_resume_text(uploaded_resume):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_resume.read())
        tmp_path = tmp_file.name

    # Try regular text extraction
    text = extract_text(tmp_path)
    if text and len(text.strip()) > 100:
        return text

    # If not enough text, try OCR
    try:
        images = convert_from_path(tmp_path)
        ocr_text = ""
        for img in images:
            ocr_text += pytesseract.image_to_string(img)
        return ocr_text
    except Exception as e:
        return f"OCR_ERROR::{e}"

# ---- Process ----
if st.button("🔍 Analyze"):
    if uploaded_resume and jd_input.strip():
        resume_text = extract_resume_text(uploaded_resume)

        if resume_text.startswith("OCR_ERROR::"):
            st.error(f"❌ OCR failed: {resume_text.split('::')[1]}")
            st.stop()
        elif not resume_text.strip():
            st.error("❌ Couldn't extract text. Resume might be empty or corrupted.")
            st.stop()

        score = get_match_score(resume_text, jd_input)
        missing_skills = extract_missing_skills(resume_text, jd_input)

        st.success(f"✅ Match Score: {score}%")
        if score < 70:
            st.warning("⚠️ You may want to improve your resume for a better fit.")

        if missing_skills:
            st.subheader("🚫 Missing Keywords")
            st.write(", ".join(missing_skills))
        else:
            st.write("✅ Great! No major keywords missing.")
    else:
        st.warning("Please upload a resume and paste a job description.")

