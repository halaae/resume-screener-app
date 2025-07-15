# skill_matcher.py

import re

def extract_keywords(text):
    # Convert to lowercase and remove non-alphabetic characters
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())

    # Define some common job skills (you can expand this list)
    common_skills = [
        'python', 'java', 'c++', 'sql', 'machine learning', 'deep learning',
        'nlp', 'data analysis', 'excel', 'pandas', 'numpy', 'keras', 'tensorflow',
        'scikit-learn', 'power bi', 'matplotlib', 'communication', 'teamwork',
        'problem solving', 'leadership', 'aws', 'azure', 'docker', 'git', 'linux'
    ]

    # Match skills from the text
    found_skills = [skill for skill in common_skills if skill in text]
    return set(found_skills)

def find_missing_skills(resume_text, jd_text):
    resume_skills = extract_keywords(resume_text)
    jd_skills = extract_keywords(jd_text)

    missing = jd_skills - resume_skills
    return sorted(missing)
