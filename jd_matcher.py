# jd_matcher.py (BERT version)
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('./models/all-MiniLM-L6-v2')  # ✅ Use local model



def get_match_score(resume_text, job_description_text):
    try:
        # Encode both texts using BERT
        embeddings = model.encode([resume_text, job_description_text], convert_to_tensor=True)

        # Compute cosine similarity
        cosine_sim = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
        match_percent = round(cosine_sim * 100, 2)

        return match_percent
    except Exception as e:
        print(f"Error with BERT matching: {e}")
        return 0.0

