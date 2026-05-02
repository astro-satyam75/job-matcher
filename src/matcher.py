import re

# Define important skills
SKILLS = [
    "python", "sql", "machine learning", "excel", "ml", "analytics",
    "power bi", "tableau", "statistics", "nlp", "tableau", "pyspark", "genai"
]


def extract_skills(text):
    text = text.lower()

    skills_found = set()

    for skill in SKILLS:
        # split multi-word skills
        if " " in skill:
            if all(word in text for word in skill.split()):
                skills_found.add(skill)
        else:
            if skill in text:
                skills_found.add(skill)

    return skills_found


def keyword_score(resume, jd):
    resume_skills = extract_skills(resume)
    jd_skills = extract_skills(jd)

    if not jd_skills:
        return 0

    match_count = len(resume_skills & jd_skills)
    return match_count / len(jd_skills)

def skill_gap(resume, jd):
    resume_skills = extract_skills(resume)
    jd_skills = extract_skills(jd)

    print("RESUME:", resume_skills)
    print("JD:", jd_skills)

    missing = jd_skills - resume_skills
    return list(missing)