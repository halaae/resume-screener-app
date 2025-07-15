from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")  # ✅ Model hosted on Hugging Face

def get_match_score(resume_text, jd_text):
    if not resume_text or not jd_text:
        return 0

    resume_emb = model.encode([resume_text])[0]
    jd_emb = model.encode([jd_text])[0]

    score = cosine_similarity([resume_emb], [jd_emb])[0][0] * 100
    return round(score, 2)

from sklearn.metrics.pairwise import cosine_similarity


