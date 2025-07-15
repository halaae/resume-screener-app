# app.py

import streamlit as st
import os
from resume_parser import extract_text_from_pdf
from jd_matcher import get_match_score
from skill_matcher import find_missing_skills

st.set_page_config(page_title="AI Resume Screener", layout="centered")

st.title("📄 AI Resume Screener + Job Match")
st.write("Upload your **Resume (PDF)** and paste a **Job Description** to see how well it matches.")

# Upload Resume
resume_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

# Paste or type Job Description
job_description = st.text_area("Paste the Job Description here", height=200)

if resume_file and job_description:
    with st.spinner("Processing..."):
        # Save resume temporarily
        with open("temp_resume.pdf", "wb") as f:
            f.write(resume_file.read())

        # Extract text from resume
        resume_text = extract_text_from_pdf("temp_resume.pdf")

        if resume_text:
            # Get match score using BERT
            match_score = get_match_score(resume_text, job_description)
            st.success(f"✅ Match Score: **{match_score}%**")

            # Match feedback
            if match_score >= 75:
                st.info("🎯 Great match! Your resume fits this job well.")
            elif match_score >= 50:
                st.warning("🧐 Decent match. Consider adding missing keywords.")
            else:
                st.error("❌ Low match. Try tailoring your resume to the job description.")

            # Show missing skills
            missing = find_missing_skills(resume_text, job_description)
            if missing:
                st.warning("🔍 Missing Keywords from Resume:")
                for skill in missing:
                    st.markdown(f"- ❌ `{skill}`")
            else:
                st.success("✅ All important keywords seem to be present!")

            # View raw resume text (optional)
            with st.expander("📄 View Extracted Resume Text"):
                st.write(resume_text)
        else:
            st.error("Failed to extract text from the resume.")

