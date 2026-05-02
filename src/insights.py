import sqlite3
import pandas as pd
from collections import Counter

# Same skill list
SKILLS = [
    "python", "sql", "machine learning", "excel",
    "power bi", "tableau", "statistics", "nlp",
    "tensorflow", "pytorch", "airflow", "spark",
    "etl", "data visualization", "aws", "docker"
]

def load_jobs():
    conn = sqlite3.connect("data/jobs.db")
    df = pd.read_sql("SELECT * FROM jobs", conn)
    conn.close()
    return df


def get_skill_counts():
    df = load_jobs()

    all_text = " ".join(df['description'].str.lower())

    skill_counts = {}

    for skill in SKILLS:
        if " " in skill:
            if all(word in all_text for word in skill.split()):
                skill_counts[skill] = all_text.count(skill)
        else:
            skill_counts[skill] = all_text.count(skill)

    return pd.DataFrame(
        sorted(skill_counts.items(), key=lambda x: x[1], reverse=True),
        columns=["skill", "count"]
    )