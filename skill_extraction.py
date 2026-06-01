import spacy
import re
import pandas as pd
import streamlit as st

nlp = spacy.load("en_core_web_sm")

# Load skills
@st.cache_data
def load_skills_db():
    df=pd.read_csv("job_dataset.csv", encoding="utf-8")

    skills_set = set()

    for _, row in df.iterrows():

        skills_text = ""

        for i in range(2, len(row)):
            # skills_text += " " + str(row[i])
            skills_text += " " + str(row.iloc[i])

        skills = skills_text.replace(";", ",").split(",")

        skills = [s.strip().lower() for s in skills if s.strip()]

        skills_set.update(skills)

    return list(skills_set)


# Alias
SKILL_ALIASES = {
    "ml": "machine learning",
    "dl": "deep learning",
    "ai": "machine learning",
    "js": "javascript",
    "py": "python"
}

STOPWORDS = {
    "and","or","with","using","based","system",
    "development","team","project"
}


# OUTDATED SKILLS
OUTDATED_SKILLS = {
    "jquery": ["react","vue","angular"],
    "angularjs": ["react","angular","vue"],
    "svn": ["git","github","gitlab"],
    "manual testing": ["selenium","automation testing","cypress"],
    "excel": ["power bi","tableau","data visualization"],
    "php": ["nodejs","django","spring boot"],
    "mongodb": ["postgresql","mysql","firebase"],
    "bootstrap": ["tailwind css","material ui"],
    "hadoop": ["spark","databricks"]
}


def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    return text


def extract_skills(text, skills_db):

    text_norm = normalize_text(text)

    found_skills = set()

    for skill in skills_db:
        if skill in text_norm:
            found_skills.add(skill)

    for alias, actual in SKILL_ALIASES.items():
        if alias in text_norm:
            found_skills.add(actual)

    found_skills = {s for s in found_skills if s not in STOPWORDS}

    return sorted(found_skills)


# Detect outdated
def detect_outdated(skills):

    outdated = {}
    suggested = {}

    for skill in skills:
        skill_lower = skill.lower()

        if skill_lower in OUTDATED_SKILLS:
            outdated[skill] = True
            suggested[skill] = OUTDATED_SKILLS[skill_lower]

    return outdated, suggested


def clean_skills(skills):
    return list(set([s.title() for s in skills]))


# MAIN PIPELINE
def skill_extraction_pipeline(resume_data):

    text = resume_data["text"]

    skills_db = load_skills_db()

    skills = extract_skills(text, skills_db)

    cleaned_skills = clean_skills(skills)

    outdated, suggested = detect_outdated(cleaned_skills)

    return {
        "skills": cleaned_skills,
        "outdated_skills": outdated,
        "suggested_skills": suggested
    }