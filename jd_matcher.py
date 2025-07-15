from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_match_score(resume_text, jd_text):
    docs = [resume_text, jd_text]
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.8)
    tfidf = vectorizer.fit_transform(docs)
    score = cosine_similarity(tfidf[0], tfidf[1])[0][0] * 100
    return round(score, 2)

def extract_missing_skills(resume_text, jd_text):
    jd_words = set(jd_text.lower().split())
    resume_words = set(resume_text.lower().split())
    missing = list(jd_words - resume_words)
    keywords = [w for w in missing if len(w) > 4 and not w.startswith(("http", "www"))]
    return keywords[:10]



