import streamlit as st
from jd_matcher import get_match_score, extract_missing_skills
from pdfminer.high_level import extract_text
import pytesseract
import fitz  # PyMuPDF
from PIL import Image
import io
import tempfile

st.set_page_config(page_title="AI Resume Screener", layout="centered")

st.title("📄 AI Resume Screener + Matcher")
st.write("Upload your resume and paste a job description to get your match score and missing skills!")

uploaded_resume = st.file_uploader("📎 Upload Resume (PDF)", type=["pdf"])
jd_input = st.text_area("💼 Paste Job Description", height=200)

def extract_resume_text(uploaded_resume):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_resume.read())
        tmp_path = tmp_file.name

    # Step 1: Try extracting normal PDF text
    text = extract_text(tmp_path)
    if text and len(text.strip()) > 100:
        return text

    # Step 2: Fallback to OCR
    try:
        doc = fitz.open(tmp_path)
        ocr_text = ""
        for page in doc:
            pix = page.get_pixmap(dpi=300)
            img_bytes = pix.tobytes("png")
            image = Image.open(io.BytesIO(img_bytes))  # ✅ Convert bytes to PIL image
            ocr_text += pytesseract.image_to_string(image)
        return ocr_text
    except Exception as e:
        return f"OCR_ERROR::{e}"

if st.button("🚀 Analyze Resume"):
    if uploaded_resume and jd_input.strip():
        resume_text = extract_resume_text(uploaded_resume)

        if resume_text.startswith("OCR_ERROR::"):
            st.error(f"❌ OCR failed: {resume_text.split('::')[1]}")
        elif not resume_text.strip():
            st.error("❌ No text found in the resume. Please upload a valid PDF.")
        else:
            score = get_match_score(resume_text, jd_input)
            missing_skills = extract_missing_skills(resume_text, jd_input)

            st.success(f"✅ Match Score: {score}%")
            if score < 70:
                st.warning("🔍 Try improving your resume to better match this role.")

            if missing_skills:
                st.subheader("🚫 Missing Keywords")
                st.write(", ".join(missing_skills))
            else:
                st.success("🎯 You're hitting all the right keywords!")
    else:
        st.warning("Please upload a resume and provide a job description.")



