# import requests
# import streamlit as st

# # ================= API CONFIG =================

# RAPIDAPI_KEY = "816efbf668msh7110f3c6d1a6a47p151ccdjsncf0f293a4056"

# URL = "https://jsearch.p.rapidapi.com/search"

# HEADERS = {
#     "X-RapidAPI-Key": RAPIDAPI_KEY,
#     "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
# }

# # ================= FETCH JOBS =================

# def get_hiring_companies(role, country="India"):

#     querystring = {
#         "query": f"{role} jobs in {country}",
#         "page": "1",
#         "num_pages": "1"
#     }

#     try:

#         response = requests.get(
#             URL,
#             headers=HEADERS,
#             params=querystring,
#             timeout=20
#         )

#         data = response.json()

#         # Debug
#         print(data)

#         if response.status_code != 200:
#             st.error(f"API Error: {data}")
#             return []

#         jobs = []

#         if not data.get("data"):
#             return []

#         for job in data["data"]:

#             jobs.append({
#                 "company": job.get("employer_name", "N/A"),
#                 "title": job.get("job_title", "N/A"),
#                 "location": job.get("job_city", "N/A"),
#                 "state": job.get("job_state", "N/A"),
#                 "employment_type": job.get("job_employment_type", "N/A"),
#                 "salary_min": job.get("job_min_salary"),
#                 "salary_max": job.get("job_max_salary"),
#                 "apply_link": job.get("job_apply_link", ""),
#                 "description": job.get("job_description", "")[:250]
#             })

#         return jobs

#     except Exception as e:
#         st.error(f"API Error: {e}")
#         return []

import requests
import streamlit as st

# ================= API CONFIG =================

RAPIDAPI_KEY = "816efbf668msh7110f3c6d1a6a47p151ccdjsncf0f293a4056"

URL = "https://jsearch.p.rapidapi.com/search"

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}


@st.cache_data(ttl=3600)
def get_hiring_companies(role, country="India"):

    querystring = {
        "query": f"{role} jobs in {country}",
        "page": "1",
        "num_pages": "2"   # safer than 5, avoids timeout
    }

    try:
        response = requests.get(
            URL,
            headers=HEADERS,
            params=querystring,
            timeout=40
        )

        data = response.json()

        if response.status_code != 200:
            st.error(f"API Error: {data}")
            return []

        jobs = []

        for job in data.get("data", []):

            # Location
            city = job.get("job_city")
            state = job.get("job_state")
            country_name = job.get("job_country")

            location_parts = [
                x for x in [city, state, country_name]
                if x and str(x).lower() != "none"
            ]

            location = (
                ", ".join(location_parts)
                if location_parts
                else "Location not specified"
            )

            # Salary
            salary_min = job.get("job_min_salary")
            salary_max = job.get("job_max_salary")

            if salary_min or salary_max:
                salary = f"₹ {salary_min or '-'} - {salary_max or '-'}"
            else:
                salary = "Not disclosed"

            # Description
            desc = job.get(
                "job_description",
                "No description available."
            ).replace("\n", " ").strip()

            if len(desc) > 500:
                desc = desc[:500]
                last_dot = desc.rfind(".")
                if last_dot > 0:
                    desc = desc[:last_dot + 1]
                else:
                    desc += "..."

            jobs.append({
                "company": job.get("employer_name") or "Unknown Company",
                "title": job.get("job_title") or role,
                "location": location,
                "employment_type": job.get(
                    "job_employment_type"
                ) or "Not specified",
                "salary": salary,
                "apply_link": job.get("job_apply_link", ""),
                "posted_date": job.get(
                    "job_posted_at_datetime_utc", ""
                ),
                "description": desc
            })

        # Remove duplicates
        unique_jobs = []
        seen = set()

        for job in jobs:
            key = (job["company"], job["title"])

            if key not in seen:
                seen.add(key)
                unique_jobs.append(job)

        return unique_jobs

    except Exception as e:
        st.error(f"API Error: {e}")
        return []