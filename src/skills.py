import re


SKILLS = {

    "python",
    "sql",
    "machine learning",
    "deep learning",
    "tableau",
    "power bi",
    "excel",
    "pandas",
    "numpy",
    "tensorflow",
    "nlp",
    "statistics",
    "pyspark",
    "bigquery",
    "data analysis"
}


def extract_skills(text):

    text = text.lower()

    found = set()

    for skill in SKILLS:

        if re.search(
            rf"\\b{re.escape(skill)}\\b",
            text
        ):

            found.add(skill)

    return found