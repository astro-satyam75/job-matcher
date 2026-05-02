from src.model import compute_similarity

resume = """
Python
"""

results = compute_similarity(resume)

print(results[['title', 'company', 'final_score', 'missing_skills']].head(5))