from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)


def compute_similarity(
    resume_text,
    jobs_df
):

    job_descriptions = jobs_df[
        "description"
    ].fillna("").tolist()

    documents = [
        resume_text
    ] + job_descriptions

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(
        documents
    )

    resume_vector = tfidf_matrix[0]

    job_vectors = tfidf_matrix[1:]

    scores = cosine_similarity(
        resume_vector,
        job_vectors
    )[0]

    jobs_df["match_score"] = scores

    jobs_df = jobs_df.sort_values(
        by="match_score",
        ascending=False
    )

    return jobs_df