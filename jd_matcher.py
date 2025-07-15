# jd_matcher.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_match_score(resume_text, jd_text):
    docs = [resume_text, jd_text]
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.8)
    tfidf = vectorizer.fit_transform(docs)
    score = cosine_similarity(tfidf[0], tfidf[1])[0][0] * 100
    return round(score, 2)



