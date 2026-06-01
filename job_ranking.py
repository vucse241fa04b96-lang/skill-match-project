import pandas as pd
import streamlit as st

# ✅ Load dataset ONLY ONCE (important for Streamlit)
@st.cache_data
def load_job_db():
    df=pd.read_csv("job_dataset.csv", encoding="utf-8")

    JOB_DB = {}

    for _, row in df.iterrows():

        try:
            # role = str(row[1]).strip()
            role = str(row.iloc[1]).strip()   # Column B (Job Role)
        except:
            continue

        skills_text = ""

        for i in range(2, len(row)):
            # skills_text += " " + str(row[i])
            skills_text += " " + str(row.iloc[i])

        skills = skills_text.replace(";", ",").split(",")

        skills = [s.strip().lower() for s in skills if s.strip()]

        if role:
            JOB_DB[role] = skills

    return JOB_DB


# ✅ Normalize skills
def normalize_skills(skills):
    return [skill.lower().strip() for skill in skills]


# ✅ Calculate match %
def calculate_match(user_skills, job_skills):

    if len(job_skills) == 0:
        return 0

    match_count = 0

    for skill in job_skills:
        if skill in user_skills:
            match_count += 1

    match_percentage = (match_count / len(job_skills)) * 100

    return round(match_percentage)


# ✅ MAIN FUNCTION
def rank_jobs(skills_data):

    JOB_DB = load_job_db()   # ✅ load from CSV

    user_skills = normalize_skills(skills_data["skills"])

    results = []

    for role, job_skills in JOB_DB.items():

        match = calculate_match(user_skills, job_skills)

        results.append({
            "role": role,
            "match": match
        })

    # ✅ Sort by highest match
    results.sort(key=lambda x: x["match"], reverse=True)

    # ✅ Top 5 only
    top_jobs = results[:15]

    # ✅ Add rank
    for i, job in enumerate(top_jobs, 1):
        job["rank"] = i

    return {
        "ranked_jobs": top_jobs
    }