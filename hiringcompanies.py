import requests
import streamlit as st

# ================= API CONFIG =================

RAPIDAPI_KEY = "816efbf668msh7110f3c6d1a6a47p151ccdjsncf0f293a4056"

URL = "https://jsearch.p.rapidapi.com/search"

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

# ================= FETCH JOBS =================

def get_hiring_companies(role, country="India"):

    querystring = {
        "query": f"{role} jobs in {country}",
        "page": "1",
        "num_pages": "1"
    }

    try:

        response = requests.get(
            URL,
            headers=HEADERS,
            params=querystring,
            timeout=20
        )

        data = response.json()

        # Debug
        print(data)

        if response.status_code != 200:
            st.error(f"API Error: {data}")
            return []

        jobs = []

        if not data.get("data"):
            return []

        for job in data["data"]:

            jobs.append({
                "company": job.get("employer_name", "N/A"),
                "title": job.get("job_title", "N/A"),
                "location": job.get("job_city", "N/A"),
                "state": job.get("job_state", "N/A"),
                "employment_type": job.get("job_employment_type", "N/A"),
                "salary_min": job.get("job_min_salary"),
                "salary_max": job.get("job_max_salary"),
                "apply_link": job.get("job_apply_link", ""),
                "description": job.get("job_description", "")[:250]
            })

        return jobs

    except Exception as e:
        st.error(f"API Error: {e}")
        return []