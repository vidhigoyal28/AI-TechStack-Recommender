import pandas as pd

df = pd.read_csv("raw_skills.csv", encoding="cp1252")

def get_all_skills():
    skills = set()
    for skill_list in df["Skills"].dropna():
        for skill in skill_list.split(","):
            skills.add(skill.strip())
    return sorted(skills)

def analyze_skill_gap(user_skills, job_skills):
    user_set = {s.strip().lower() for s in user_skills.split(",") if s.strip()}
    job_set = {s.strip().lower() for s in job_skills.split(",") if s.strip()}

    matched = sorted(user_set & job_set)
    missing = sorted(job_set - user_set)

    return matched, missing