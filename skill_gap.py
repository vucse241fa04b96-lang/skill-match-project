import streamlit as st
import pandas as pd

@st.cache_data
def load_job_db():
    # df = pd.read_csv("job_dataset.csv")
    df=pd.read_csv("job_dataset.csv", encoding="utf-8")
    JOB_DB = {}

    for _, row in df.iterrows():
        try:
            # role = str(row[1]).strip()
            role = str(row.iloc[1]).strip()
        except:
            continue

        skills_text = ""
        for i in range(2, len(row)):
            # skills_text += " " + str(row[i])
            skills_text += " " + str(row.iloc[i])

        skills = skills_text.replace(";", ",").split(",")

        cleaned_skills = []
        for s in skills:
            s = s.strip().lower()

            if len(s.split()) > 4:
                continue
            if not s or len(s) < 2:
                continue

            cleaned_skills.append(s)

        if role:
            JOB_DB[role] = list(set(cleaned_skills))

    return JOB_DB


def normalize_skills(skills):
    return [skill.lower().strip() for skill in skills]


def clean_missing_skills(skills):
    cleaned = []

    for s in skills:
        if len(s.split()) > 4:
            continue
        if any(word in s for word in ["assist", "collaborate", "learn", "perform"]):
            continue

        cleaned.append(s)

    return list(set([s.title() for s in cleaned]))


def find_skill_gap(user_skills, job_role, JOB_DB):
    required_skills = JOB_DB.get(job_role, [])
    return clean_missing_skills(
        [skill for skill in required_skills if skill not in user_skills]
    )


# ✅ FINAL CLEAN FUNCTION
def skill_gap_detection(skills_data, selected_role):
    JOB_DB = load_job_db()
    user_skills = set(normalize_skills(skills_data["skills"]))

    missing = []

    if selected_role:
        missing = find_skill_gap(user_skills, selected_role, JOB_DB)

    return {
        "selected_role": selected_role,
        "missing_skills": missing
    }