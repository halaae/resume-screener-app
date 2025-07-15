import streamlit as st
from jd_matcher import get_match_score, extract_missing_skills
from pdfminer.high_level import extract_text
import tempfile

st.set_page_config(page_title="AI Resume Screener", layout="centered")

st.title("📄 AI Resume Screener + Matcher")
st.write("Upload your resume (PDF) and paste a job description to get your match score and missing skills!")

uploaded_resume = st.file_uploader("📎 Upload Resume (PDF)", type=["pdf"])
jd_input = st.text_area("💼 Paste Job Description", height=200)

def extract_resume_text(uploaded_resume):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_resume.read())
        tmp_path = tmp_file.name

    # Only extract text from PDF – no OCR
    text = extract_text(tmp_path)
    return text

if st.button("🚀 Analyze Resume"):
    if uploaded_resume and jd_input.strip():
        resume_text = extract_resume_text(uploaded_resume)

        if not resume_text.strip():
            st.error("❌ Could not extract text from the resume. Please upload a valid text-based PDF.")
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



