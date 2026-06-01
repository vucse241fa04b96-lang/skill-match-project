import streamlit as st
import pandas as pd
from upload import extract_resume_text, clean_text
from skill_extraction import skill_extraction_pipeline
from job_ranking import rank_jobs
from skill_gap import skill_gap_detection
from chatbot import chatbot_ui
from hiringcompanies import get_hiring_companies
import os
from chat_storage import get_user_chats
from chat_storage import load_chat
from auth import (
    save_user,
    verify_user,
    user_exists
)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""
if not st.session_state.logged_in:

    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )
if st.button("Login"):

    if verify_user(username, password):

        st.session_state.logged_in = True
        st.session_state.username = username

        st.rerun()

    else:
        st.error("Invalid credentials")
if st.button("Sign Up"):

    if user_exists(username):

        st.error("User already exists")

    else:

        save_user(username, password)

        st.success(
            "Account created successfully"
        )
if not st.session_state.logged_in:
    st.stop()
username = st.session_state.username

os.makedirs(
    f"chats/{username}",
    exist_ok=True
)
import time

if "chat_file" not in st.session_state:

    st.session_state.chat_file = (
        f"chats/{username}/chat_{int(time.time())}.json"
    )


st.write(st.session_state.chat_file)
# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Career Analyzer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ================= GLOBAL CSS =================
st.markdown("""
<style>
/* ---------- App background ---------- */
.stApp {
    background: linear-gradient(135deg, #eef2ff 0%, #f8fafc 50%, #ecfeff 100%);
}

/* ---------- Hero ---------- */
.hero {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%);
    padding: 40px 30px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 20px 50px -20px rgba(99,102,241,0.55);
}
.hero h1 {
    font-size: 44px;
    margin: 0;
    font-weight: 800;
    letter-spacing: -0.5px;
}
.hero p {
    font-size: 17px;
    opacity: 0.92;
    margin-top: 8px;
}

/* ---------- Cards ---------- */
.card {
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(10px);
    padding: 24px 26px;
    border-radius: 16px;
    border: 1px solid rgba(226,232,240,0.8);
    box-shadow: 0 8px 24px -12px rgba(15,23,42,0.12);
    margin-bottom: 22px;
}
.section-title {
    font-size: 20px;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* ---------- Stat tiles ---------- */
.stat-tile {
    background: white;
    border-radius: 14px;
    padding: 18px;
    border: 1px solid #e2e8f0;
    text-align: center;
}
.stat-num { font-size: 28px; font-weight: 800; color: #6366f1; }
.stat-lbl { font-size: 13px; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; }

/* ---------- Skill chips ---------- */
.skill-chip {
    display: inline-block;
    padding: 6px 14px;
    margin: 4px;
    background: linear-gradient(135deg, #eef2ff, #e0e7ff);
    color: #4338ca;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 500;
    border: 1px solid #c7d2fe;
}
.gap-item {
    display: inline-block;
    padding: 6px 14px;
    margin: 4px;
    background: linear-gradient(135deg, #fee2e2, #fecaca);
    color: #b91c1c;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 500;
    border: 1px solid #fca5a5;
}
.trend-item {
    display: inline-block;
    padding: 6px 14px;
    margin: 4px;
    background: linear-gradient(135deg, #d1fae5, #a7f3d0);
    color: #047857;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 500;
    border: 1px solid #6ee7b7;
}

/* ---------- Job card ---------- */
.job-card {
    background: white;
    padding: 16px 18px;
    border-radius: 12px;
    margin-bottom: 10px;
    border: 1px solid #e2e8f0;
    border-left: 5px solid #6366f1;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: transform .15s ease, box-shadow .15s ease;
}
.job-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 24px -12px rgba(99,102,241,0.35);
}
.job-title { font-weight: 700; color: #1e293b; font-size: 15px; }
.match-pill {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
}

/* ---------- Replace row ---------- */
.replace-row {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 12px 14px;
    margin-bottom: 10px;
}

/* ---------- File uploader tweak ---------- */
section[data-testid="stFileUploaderDropzone"] {
    background: linear-gradient(135deg, #f5f3ff, #ede9fe);
    border: 2px dashed #a78bfa !important;
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

# ================= HERO =================
st.markdown("""
<div class="hero">
    <h1>🚀 Skill-Based Career Analyzer</h1>
    <p>Upload your resume — get skills, job matches, gap analysis, and trending recommendations.</p>
</div>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
# Get logged-in username
username = st.session_state.username

# ================= SIDEBAR =================
with st.sidebar:

    st.markdown("### ⚙️ How it works")
    st.markdown("""
    1. **Upload** your resume (PDF)
    2. We **extract** skills
    3. Get **matched** roles
    4. See your **skill gaps**
    5. Chat with the **AI advisor**
    """)

    st.divider()

    st.caption("💡 Tip: Use a recent, text-based PDF for best results.")

    # ================= NEW CHAT =================
    if st.button("➕ New Chat"):

        import time

        st.session_state.messages = []

        st.session_state.chat_file = (
            f"chats/{username}/chat_{int(time.time())}.json"
        )

        st.rerun()

    # ================= RECENT CHATS =================
    st.subheader("Recent Chats")

    chat_files = get_user_chats(username)

    if chat_files:

        for file in chat_files:

            if st.button(
                file,
                key=f"chat_{file}"
            ):

                st.session_state.chat_file = (
                    f"chats/{username}/{file}"
                )

                st.session_state.messages = load_chat(
                    st.session_state.chat_file
                )

                st.rerun()

    else:
        st.info("No previous chats")

    st.divider()

    # ================= CURRENT USER =================
    st.write(f"👤 Logged in as: {username}")

    # ================= LOGOUT =================
    if st.button("🚪 Logout"):

        st.session_state.logged_in = False
        st.session_state.username = ""

        # Clear current chat
        st.session_state.messages = []

        # Remove active chat file
        if "chat_file" in st.session_state:
            del st.session_state.chat_file

        st.rerun()
# ================= SESSION =================
st.session_state.setdefault("skills", [])
st.session_state.setdefault("last_role", "")

# ================= UPLOAD =================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📄 Upload Your Resume</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Drop your PDF here", type=["pdf"], label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# ================= PIPELINE =================
if uploaded_file is not None:
    st.toast("Resume uploaded successfully!", icon="✅")

    with st.spinner("🔍 Analyzing your resume..."):
        try:
            # ----- text -----
            raw_text = extract_resume_text(uploaded_file)
            cleaned_text = clean_text(raw_text)
            resume_data = {"text": cleaned_text}

            # ----- skills -----
            skills_data = skill_extraction_pipeline(resume_data)
            extracted_skills = skills_data.get("skills", [])[:50]
            outdated_skills = skills_data.get("outdated_skills", {}) or {}
            suggested_skills = skills_data.get("suggested_skills", {}) or {}

            st.session_state.skills = [s.lower() for s in extracted_skills]
            st.session_state.outdated_skills = outdated_skills
            st.session_state.suggested_skills = suggested_skills

            # ----- jobs -----
            ranked_jobs = rank_jobs(skills_data)
            job_roles = ranked_jobs.get("ranked_jobs", [])
            st.session_state.ranked_jobs = job_roles

            # ================= STAT TILES =================
            c1, c2, c3, c4 = st.columns(4)
            for col, num, lbl in [
                (c1, len(extracted_skills), "Skills found"),
                (c2, len(job_roles), "Roles matched"),
                (c3, len(outdated_skills), "Outdated"),
                (c4, sum(len(v) for v in suggested_skills.values()), "Trending"),
            ]:
                with col:
                    st.markdown(
                        f'<div class="stat-tile"><div class="stat-num">{num}</div>'
                        f'<div class="stat-lbl">{lbl}</div></div>',
                        unsafe_allow_html=True,
                    )

            st.write("")

            # ================= TABS =================
            tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🧠 Skills",
            "💼 Jobs",
            "📈 Trending",
            "🎯 Gap Analysis",
            "🏢 Hiring Companies"
            ])

            # ---------- SKILLS TAB ----------
            with tab1:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">🧠 Extracted Skills (Top 50)</div>', unsafe_allow_html=True)
                if extracted_skills:
                    chips = "".join(f'<span class="skill-chip">{s}</span>' for s in extracted_skills)
                    st.markdown(chips, unsafe_allow_html=True)
                else:
                    st.info("No skills found.")
                st.markdown('</div>', unsafe_allow_html=True)

            # ---------- JOBS TAB ----------
            with tab2:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">💼 Job Recommendations</div>', unsafe_allow_html=True)
                if job_roles:
                    for i, job in enumerate(job_roles):
                        st.markdown(
                            f'<div class="job-card">'
                            f'<div class="job-title">{i+1}. {job["role"]}</div>'
                            f'<div class="match-pill">{job["match"]}% match</div>'
                            f'</div>',
                            unsafe_allow_html=True,
                        )
                        st.progress(int(job["match"]) / 100)
                else:
                    st.info("No job recommendations found.")
                st.markdown('</div>', unsafe_allow_html=True)

            # ---------- TRENDING TAB ----------
            with tab3:
                if outdated_skills:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown('<div class="section-title">📉 Outdated Skills</div>', unsafe_allow_html=True)
                    st.markdown(
                        "".join(f'<span class="gap-item">{s}</span>' for s in outdated_skills.keys()),
                        unsafe_allow_html=True,
                    )
                    st.markdown('</div>', unsafe_allow_html=True)

                if suggested_skills:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown('<div class="section-title">🚀 Trending Replacements</div>', unsafe_allow_html=True)
                    for old, news in suggested_skills.items():
                        chips = "".join(f'<span class="trend-item">{n}</span>' for n in news)
                        st.markdown(
                            f'<div class="replace-row">Replace <b>{old}</b> with:<br>{chips}</div>',
                            unsafe_allow_html=True,
                        )
                    st.markdown('</div>', unsafe_allow_html=True)

                if not outdated_skills and not suggested_skills:
                    st.success("✨ Your skills are up to date!")

            # ---------- GAP TAB ----------
            with tab4:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">🎯 Choose a Target Role</div>', unsafe_allow_html=True)

                if job_roles:
                    options = [f"{i+1}. {job['role']}" for i, job in enumerate(job_roles)]
                    selected_option = st.selectbox("Pick a role to analyze", options)
                    selected_role = job_roles[options.index(selected_option)]["role"]
                else:
                    selected_role = "Not found"

                st.markdown('</div>', unsafe_allow_html=True)

                skill_gap = skill_gap_detection(skills_data, selected_role)
                missing_skills = skill_gap.get("missing_skills", [])
                st.session_state.missing_skills = missing_skills
                st.session_state.selected_role = selected_role
                st.session_state.last_role = selected_role.lower()

                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">📉 Skill Gap Analysis</div>', unsafe_allow_html=True)
                st.markdown(f"**🎯 Target Role:** `{selected_role}`")

                if missing_skills:
                    st.markdown(
                        "".join(f'<span class="gap-item">{s}</span>' for s in missing_skills),
                        unsafe_allow_html=True,
                    )
                    coverage = max(0, 100 - len(missing_skills) * 5)
                    st.progress(coverage / 100, text=f"Approx. readiness: {coverage}%")
                else:
                    st.success("🎉 You already have most required skills!")
                st.markdown('</div>', unsafe_allow_html=True)

        #     with tab5:

        #         st.markdown("### 🏢 Hiring Companies")

        #         if job_roles:

        #             options = [
        #             f"{i+1}. {job['role']}"
        #             for i, job in enumerate(job_roles)
        #             ]

        #             selected_option = st.selectbox(
        #             "Select a Job Role",
        #             options,
        #             key="hiring_role"
        #             )

        #             selected_role = job_roles[
        #             options.index(selected_option)
        #             ]["role"]

        #             jobs = get_hiring_companies(selected_role)

        #             if jobs:

        #                 for job in jobs:

        #                     st.markdown(f"### 🏢 {job['company']}")

        #                     st.write(f"**Role:** {job['title']}")
        #                     st.write(f"**Location:** {job['location']}, {job['state']}")
        #                     st.write(f"**Type:** {job['employment_type']}")

        #                     if job["salary_min"] or job["salary_max"]:
        #                         st.success(
        #                         f"💰 ₹{job['salary_min']} - ₹{job['salary_max']}"
        #                         )

        #                     st.write(job["description"])

        #                     if job["apply_link"]:
        #                         st.link_button(
        #                          "Apply Now",
        #                             job["apply_link"]
        #                         )

        #                     st.divider()

        #             else:
        #                 st.warning(
        #                 f"No hiring companies found for {selected_role}"
        #                 )

        # except Exception as e:
        #     st.error(f"⚠️ Error: {e}")
    
        # ---------- HIRING COMPANIES TAB ----------
            with tab5:

                st.markdown("### 🏢 Hiring Companies")

                if job_roles:

                    options = [
                f"{i+1}. {job['role']}"
                for i, job in enumerate(job_roles)
                ]

                selected_option = st.selectbox(
                 "   Select a Job Role",
                options,
                key="hiring_role"
                )

                selected_role = job_roles[
                options.index(selected_option)
                ]["role"]

                jobs = get_hiring_companies(selected_role)

                if jobs:

                    st.success(
                    f"Found {len(jobs)} hiring opportunities for {selected_role}"
                    )

                    for job in jobs:

                        st.markdown(f"## 🏢 {job['company']}")

                        col1, col2 = st.columns(2)

                        with col1:
                                st.write(f"**Role:** {job['title']}")
                                st.write(f"**📍 Location:** {job['location']}")

                        with col2:
                                st.write(f"**💼 Employment Type:** {job['employment_type']}")
                                

                                st.write(f"**💰 Salary:** {job['salary']}")

                        st.write("**Job Description:**")

                        st.markdown(
        f"""
        <div style="
            font-size:15px;
            line-height:1.6;
            color:#334155;
            margin-bottom:15px;
        ">
            {job['description']}
        </div>
        """,
        unsafe_allow_html=True
    )

                        if job.get("apply_link"):
                             st.link_button(
            "🔗 Apply Now",
            job["apply_link"]
        )

                        st.divider()
                    # else:
                    #  st.warning(
                    # f"No hiring companies found for {selected_role}"
                    # )

                # else:
                #     st.warning("No job roles available.")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
# ================= CHATBOT =================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🤖 AI Career Chatbot</div>', unsafe_allow_html=True)
chatbot_ui()
st.markdown('</div>', unsafe_allow_html=True)
