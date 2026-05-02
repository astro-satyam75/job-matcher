from sklearn.feature_extraction.text import TfidfVectorizer
from src.matcher import keyword_score
from src.matcher import skill_gap
from sklearn.metrics.pairwise import cosine_similarity
import sqlite3
import pandas as pd


def load_jobs():
    conn = sqlite3.connect("data/jobs.db")
    df = pd.read_sql("SELECT * FROM jobs", conn)
    conn.close()
    return df


def compute_similarity(resume_text):
    df = load_jobs()

    documents = df['description'].tolist()
    documents.append(resume_text)

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_matrix = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    df['semantic_score'] = similarity_matrix[0]

    df['keyword_score'] = df['description'].apply(
        lambda jd: keyword_score(resume_text, jd)
    )

    df['final_score'] = (
        0.7 * df['semantic_score'] +
        0.3 * df['keyword_score']
    )

    # 🔥 NEW: Skill gap
    df['missing_skills'] = df['description'].apply(
        lambda jd: skill_gap(resume_text, jd)
    )

    return df.sort_values(by="final_score", ascending=False)