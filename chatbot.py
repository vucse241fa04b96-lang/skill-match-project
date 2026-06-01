# import streamlit as st
# from groq import Groq

# # ================= GROQ CONFIG =================

# GROQ_API_KEY = "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"

# client = Groq(api_key=GROQ_API_KEY)

# MODEL_NAME = "llama-3.3-70b-versatile"


# # ================= CHATBOT FUNCTION =================

# def chatbot_ui():

#     st.markdown("## 🤖 AI Career Mentor")

#     # ================= SESSION MEMORY =================

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # ================= CAREER MEMORY =================

#     if "career_context" not in st.session_state:

#         st.session_state.career_context = {

#             "career_goal": "",

#             "roadmap_stage": "",

#             "completed_skills": [],

#             "recommended_projects": [],

#             "recommended_certifications": []
#         }

#     # ================= DISPLAY OLD CHATS =================

#     for message in st.session_state.messages:

#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # ================= USER INPUT =================

#     user_input = st.chat_input(
#         "Ask career questions..."
#     )

#     # ================= WHEN USER SENDS MESSAGE =================

#     if user_input:

#         # ================= TRACK USER GOALS =================

#         if "become" in user_input.lower():

#             st.session_state.career_context["career_goal"] = user_input

#         # -------- SHOW USER MESSAGE --------

#         with st.chat_message("user"):
#             st.markdown(user_input)

#         # -------- SAVE USER MESSAGE --------

#         st.session_state.messages.append({
#             "role": "user",
#             "content": user_input
#         })

#         # ================= CAREER CONTEXT =================

#         selected_role = st.session_state.get(
#             "last_role",
#             "Not Selected"
#         )

#         missing_skills = st.session_state.get(
#             "missing_skills",
#             []
#         )

#         user_skills = st.session_state.get(
#             "skills",
#             []
#         )

#         career_context = st.session_state.career_context

#         # ================= SYSTEM PROMPT =================

#         system_prompt = f"""
# You are an advanced AI Career Mentor.

# User Target Role:
# {selected_role}

# User Existing Skills:
# {user_skills}

# Missing Skills:
# {missing_skills}

# Career Context:
# {career_context}

# Your Responsibilities:
# - Guide the user step-by-step
# - Track user progress
# - Recommend roadmap
# - Recommend projects
# - Recommend certifications
# - Recommend interview preparation
# - Suggest latest industry skills
# - Avoid repeating previous suggestions
# - Personalize all responses
# - Keep responses practical and structured
# - Help user crack the target role

# If user asks roadmap:
# - divide into phases
# - beginner to advanced

# If user asks projects:
# - suggest portfolio-worthy projects

# If user asks interview questions:
# - give role-specific preparation

# Always behave like a professional career mentor.
# """

#         # ================= AI RESPONSE =================

#         response = client.chat.completions.create(

#             model=MODEL_NAME,

#             messages=[
#                 {
#                     "role": "system",
#                     "content": system_prompt
#                 }
#             ] + st.session_state.messages,

#             temperature=0.7
#         )

#         ai_reply = response.choices[0].message.content

#         # -------- SHOW AI RESPONSE --------

#         with st.chat_message("assistant"):
#             st.markdown(ai_reply)

#         # -------- SAVE AI RESPONSE --------

#         st.session_state.messages.append({
#             "role": "assistant",
#             "content": ai_reply
#         })


# import streamlit as st
# from groq import Groq

# # ================= GROQ CONFIG =================

# GROQ_API_KEY = "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"

# client = Groq(api_key=GROQ_API_KEY)

# MODEL_NAME = "llama-3.3-70b-versatile"


# # ================= CHATBOT FUNCTION =================

# def chatbot_ui():

#     st.markdown("## 🤖 AI Career Mentor")

#     # ================= SESSION MEMORY =================

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # ================= CAREER MEMORY =================

#     if "career_context" not in st.session_state:

#         st.session_state.career_context = {

#             "career_goal": "",

#             "roadmap_stage": "",

#             "completed_skills": [],

#             "recommended_projects": [],

#             "recommended_certifications": []
#         }

#     # ================= DISPLAY OLD CHATS =================

#     for message in st.session_state.messages:

#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # ================= USER INPUT =================

#     user_input = st.chat_input(
#         "Ask career questions..."
#     )

#     # ================= WHEN USER SENDS MESSAGE =================

#     if user_input:

#         # ================= DOMAIN RESTRICTION =================

#         allowed_keywords = [

#             "career",
#             "job",
#             "skills",
#             "roadmap",
#             "developer",
#             "engineer",
#             "data",
#             "scientist",
#             "ai",
#             "machine learning",
#             "resume",
#             "interview",
#             "certification",
#             "python",
#             "java",
#             "frontend",
#             "backend",
#             "full stack",
#             "learning",
#             "course",
#             "project",
#             "technology",
#             "salary",
#             "placement"
#         ]

#         is_career_query = any(
#             keyword in user_input.lower()
#             for keyword in allowed_keywords
#         )

#         # ================= BLOCK NON-CAREER QUESTIONS =================

#         if not is_career_query:

#             blocked_reply = """
# I am an AI Career Mentor chatbot.

# I can help only with:
# - Career guidance
# - Skill development
# - Resume analysis
# - Interview preparation
# - Learning roadmaps
# - Certifications
# - Job preparation

# Please ask career-related questions.
# """

#             with st.chat_message("assistant"):
#                 st.markdown(blocked_reply)

#             st.session_state.messages.append({
#                 "role": "assistant",
#                 "content": blocked_reply
#             })

#             return

#         # ================= TRACK USER GOALS =================

#         if "become" in user_input.lower():

#             st.session_state.career_context["career_goal"] = user_input

#         # -------- SHOW USER MESSAGE --------

#         with st.chat_message("user"):
#             st.markdown(user_input)

#         # -------- SAVE USER MESSAGE --------

#         st.session_state.messages.append({
#             "role": "user",
#             "content": user_input
#         })

#         # ================= ROADMAP REQUEST DETECTION =================

#         roadmap_keywords = [
#             "roadmap",
#             "learning path",
#             "study plan",
#             "guide",
#             "plan"
#         ]

#         is_roadmap_request = any(
#             keyword in user_input.lower()
#             for keyword in roadmap_keywords
#         )

#         # ================= CAREER CONTEXT =================

#         selected_role = st.session_state.get(
#             "last_role",
#             "Not Selected"
#         )

#         missing_skills = st.session_state.get(
#             "missing_skills",
#             []
#         )

#         user_skills = st.session_state.get(
#             "skills",
#             []
#         )

#         career_context = st.session_state.career_context

#         # ================= DYNAMIC SYSTEM PROMPT =================

#         if is_roadmap_request:

#             system_prompt = f"""
# You are an expert AI Career Mentor.

# Create a detailed career roadmap for the user.

# Target Role:
# {selected_role}

# User Existing Skills:
# {user_skills}

# Missing Skills:
# {missing_skills}

# Career Context:
# {career_context}

# Roadmap Rules:
# - Divide roadmap into phases
# - Include timeline
# - Include technologies
# - Include projects
# - Include certifications
# - Include interview preparation
# - Include practical guidance
# - Keep roadmap structured
# - Keep roadmap personalized
# - Mention free learning resources if possible

# Output Format:

# # Phase 1
# Timeline:
# Skills to Learn:
# Projects:
# Resources:

# # Phase 2
# Timeline:
# Skills to Learn:
# Projects:
# Resources:

# # Phase 3
# Timeline:
# Skills to Learn:
# Projects:
# Resources:

# # Final Interview Preparation
# """

#         else:

#             system_prompt = f"""
# You are an advanced AI Career Mentor.

# User Target Role:
# {selected_role}

# User Existing Skills:
# {user_skills}

# Missing Skills:
# {missing_skills}

# Career Context:
# {career_context}

# Your Responsibilities:
# - Guide the user step-by-step
# - Track user progress
# - Recommend roadmap
# - Recommend projects
# - Recommend certifications
# - Recommend interview preparation
# - Suggest latest industry skills
# - Avoid repeating previous suggestions
# - Personalize all responses
# - Keep responses practical and structured
# - Help user crack the target role

# You ONLY answer career-related questions.

# If question is unrelated to careers,
# politely refuse.
# """

#         # ================= AI RESPONSE =================

#         response = client.chat.completions.create(

#             model=MODEL_NAME,

#             messages=[
#                 {
#                     "role": "system",
#                     "content": system_prompt
#                 }
#             ] + st.session_state.messages,

#             temperature=0.7
#         )

#         ai_reply = response.choices[0].message.content

#         # -------- SHOW AI RESPONSE --------

#         with st.chat_message("assistant"):
#             st.markdown(ai_reply)

#         # -------- SAVE AI RESPONSE --------

#         st.session_state.messages.append({
#             "role": "assistant",
#             "content": ai_reply
#         })


# import streamlit as st
# from groq import Groq

# # ================= GROQ CONFIG =================

# GROQ_API_KEY = "YOUR_GROQ_API_KEY"

# client = Groq(api_key=GROQ_API_KEY)

# MODEL_NAME = "llama-3.3-70b-versatile"


# # ================= CHATBOT FUNCTION =================

# def chatbot_ui():

#     st.markdown("## 🤖 AI Career Mentor")

#     # ================= CHAT MEMORY =================

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # ================= CAREER MEMORY =================

#     if "career_context" not in st.session_state:

#         st.session_state.career_context = {

#             "career_goal": "",

#             "roadmap_stage": "",

#             "completed_skills": [],

#             "recommended_projects": [],

#             "recommended_certifications": []
#         }

#     # ================= DISPLAY OLD MESSAGES =================

#     for message in st.session_state.messages:

#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # ================= USER INPUT =================

#     user_input = st.chat_input(
#         "Ask about careers, skills, projects, roadmaps..."
#     )

#     # ================= HANDLE USER MESSAGE =================

#     if user_input:

#         user_input_lower = user_input.lower()

#         # ================= TRACK CAREER GOAL =================

#         if "become" in user_input_lower:

#             st.session_state.career_context[
#                 "career_goal"
#             ] = user_input

#         # ================= TRACK COMPLETED LEARNING =================

#         progress_keywords = [
#             "completed",
#             "finished",
#             "done",
#             "learned"
#         ]

#         if any(
#             word in user_input_lower
#             for word in progress_keywords
#         ):

#             st.session_state.career_context[
#                 "completed_skills"
#             ].append(user_input)

#         # ================= SHOW USER MESSAGE =================

#         with st.chat_message("user"):
#             st.markdown(user_input)

#         st.session_state.messages.append({
#             "role": "user",
#             "content": user_input
#         })

#         # ================= PROJECT CONTEXT =================

#         selected_role = st.session_state.get(
#             "last_role",
#             "Not Selected"
#         )

#         missing_skills = st.session_state.get(
#             "missing_skills",
#             []
#         )

#         user_skills = st.session_state.get(
#             "skills",
#             []
#         )

#         career_context = st.session_state.career_context

#         # ================= SYSTEM PROMPT =================

#         system_prompt = f"""
# You are CareerMentorAI.

# Target Role:
# {selected_role}

# Current Skills:
# {user_skills}

# Missing Skills:
# {missing_skills}

# Career Context:
# {career_context}

# Your Responsibilities:

# 1. Career Guidance
# 2. Skill Gap Analysis
# 3. Resume Improvement
# 4. Interview Preparation
# 5. Certification Recommendations
# 6. Project Recommendations
# 7. Learning Resource Recommendations
# 8. Career Roadmap Generation

# ROADMAP RULES:

# If user asks:
# - roadmap
# - study plan
# - learning path
# - what next
# - next step
# - progression plan
# - how to become

# Generate:

# Phase 1
# - Timeline
# - Skills
# - Resources
# - Projects

# Phase 2
# - Timeline
# - Skills
# - Resources
# - Projects

# Phase 3
# - Timeline
# - Skills
# - Resources
# - Projects

# Final Interview Preparation

# PERSONALIZATION RULES:

# Always use:
# - selected role
# - current skills
# - missing skills
# - completed skills
# - previous conversation history

# PROGRESS TRACKING:

# If user says:
# "I completed Python"

# Acknowledge progress and suggest next skill.

# DOMAIN FOCUS:

# You specialize in:
# - careers
# - jobs
# - learning
# - interviews
# - certifications
# - projects
# - skill development

# If user asks unrelated topics
# (movies, celebrities, sports, politics, etc.)

# Do NOT answer them directly.

# Politely redirect the conversation back toward:
# career growth,
# skill development,
# job readiness,
# or learning plans.

# Always be supportive,
# professional,
# and personalized.
# """

#         # ================= AI RESPONSE =================

#         response = client.chat.completions.create(

#             model=MODEL_NAME,

#             messages=[
#                 {
#                     "role": "system",
#                     "content": system_prompt
#                 }
#             ] + st.session_state.messages,

#             temperature=0.7
#         )

#         ai_reply = response.choices[0].message.content

#         # ================= SHOW AI RESPONSE =================

#         with st.chat_message("assistant"):
#             st.markdown(ai_reply)

#         # ================= SAVE AI RESPONSE =================

#         st.session_state.messages.append({
#             "role": "assistant",
#             "content": ai_reply
#         })




import streamlit as st
from groq import Groq

# ================= GROQ CONFIG =================

GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

MODEL_NAME = "llama-3.3-70b-versatile"


# ================= CHATBOT UI =================

def chatbot_ui():

    st.markdown("## 🤖 AI Career Mentor")

    # ================= CHAT MEMORY =================

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ================= CAREER MEMORY =================

    if "career_context" not in st.session_state:

        st.session_state.career_context = {

            "career_goal": "",

            "completed_skills": [],

            "roadmap_stage": "",

            "recommended_projects": [],

            "recommended_certifications": []
        }

    # ================= DISPLAY CHAT HISTORY =================

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # ================= USER INPUT =================

    user_input = st.chat_input(
        "Ask about careers, roadmaps, skills, projects..."
    )

    if not user_input:
        return

    user_input_lower = user_input.lower()

    # ================= STORE CAREER GOAL =================

    goal_keywords = [
        "become",
        "career goal",
        "want to become",
        "i want to become"
    ]

    if any(k in user_input_lower for k in goal_keywords):

        st.session_state.career_context[
            "career_goal"
        ] = user_input

    # ================= TRACK PROGRESS =================

    progress_keywords = [

        "completed",
        "finished",
        "done",
        "learned",
        "learnt",
        "studied"
    ]

    if any(
        k in user_input_lower
        for k in progress_keywords
    ):

        if user_input not in st.session_state.career_context["completed_skills"]:

            st.session_state.career_context[
                "completed_skills"
            ].append(user_input)

    # ================= SHOW USER =================

    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({

        "role": "user",
        "content": user_input
    })

    # ================= GET DATA FROM APP =================

    selected_role = st.session_state.get(
    "last_role",
    "Not Selected"
)
    user_skills = st.session_state.get(
        "skills",
        []
    )

    missing_skills = st.session_state.get(
        "missing_skills",
        []
    )

    outdated_skills = st.session_state.get(
        "outdated_skills",
        {}
    )

    suggested_skills = st.session_state.get(
        "suggested_skills",
        {}
    )

    ranked_jobs = st.session_state.get(
        "ranked_jobs",
        []
    )

    career_context = st.session_state.career_context

    # ================= SYSTEM PROMPT =================

    system_prompt = f"""
You are CareerMentorAI, a friendly AI assistant that specializes in career guidance but can also participate in normal conversation naturally.

You are part of a Skill-Based Career Analyzer system.

=================================================
USER PROFILE
=================================================

Selected Target Role:
{selected_role}

Current Skills:
{user_skills}

Missing Skills:
{missing_skills}

Outdated Skills:
{outdated_skills}

Trending Skill Recommendations:
{suggested_skills}

Recommended Job Roles:
{ranked_jobs}

Career Context:
{career_context}

=================================================
YOUR RESPONSIBILITIES
=================================================

1. Career Guidance
2. Skill Gap Analysis
3. Learning Roadmaps
4. Resume Improvement
5. Interview Preparation
6. Certification Recommendations
7. Project Recommendations
8. Job Readiness Guidance
9. Explain Job Recommendations
10. Explain Skill Gaps
11. Explain Trending Skills

=================================================
ROADMAP GENERATION
=================================================

If the user asks for:

- roadmap
- study plan
- learning path
- progression plan
- next step
- how to become
- what should I learn next

Generate:

PHASE 1
Timeline
Skills
Resources
Projects

PHASE 2
Timeline
Skills
Resources
Projects

PHASE 3
Timeline
Skills
Resources
Projects

INTERVIEW PREPARATION

RESUME PREPARATION

JOB APPLICATION STRATEGY

Use:

- Selected Role
- Current Skills
- Missing Skills
- Completed Skills

to personalize the roadmap.

=================================================
PROGRESS TRACKING
=================================================

Completed Skills:

{career_context.get("completed_skills", [])}

If user mentions completing a skill:

1. Congratulate them
2. Recognize progress
3. Recommend next skill
4. Recommend next project

=================================================
MEMORY AWARENESS
=================================================

Maintain conversation context.

Remember:

- Selected Role
- Current Skills
- Missing Skills
- Outdated Skills
- Trending Skills
- Recommended Roles
- Career Goal
- Completed Skills

Use previous conversation history automatically.

Do not ask the user to repeat information
already available in memory.

=================================================
JOB ROLE EXPLANATION
=================================================

If user asks:

- Why is this role recommended?
- Why is AI Engineer ranked first?
- Which role suits me best?

Explain using:

- Skill overlap
- Missing skills
- Match percentage
- User profile

=================================================
OUTDATED SKILLS ANALYSIS
=================================================

If user asks:

- Which skills are outdated?
- Which skills should I replace?
- Which trending skills should I learn?

Use:

Outdated Skills:
{outdated_skills}

Trending Skills:
{suggested_skills}

=================================================
PROJECT RECOMMENDATIONS
=================================================

Recommend portfolio-worthy projects based on:

- Selected Role
- Current Skills
- Missing Skills

=================================================
CERTIFICATION RECOMMENDATIONS
=================================================

Recommend recognized industry certifications.

=================================================
CONVERSATION STYLE
=================================================


You are a friendly AI Career Mentor.

You can engage in normal conversation such as:

- hello
- hi
- good morning
- thanks
- how are you
- okay
- bye

and other casual interactions naturally.

When the conversation relates to careers,
skills, jobs, learning, projects, interviews,
certifications, roadmaps or resume improvement,
use the user's profile data and provide
personalized guidance.

For non-career topics, you may answer briefly,
but whenever appropriate connect the discussion
back to learning, careers, technology,
professional growth, or skill development.

Do not refuse simple greetings.
Do not refuse casual conversation.
Maintain a helpful and friendly tone.

=================================================
BEHAVIOR
=================================================

Always:

- Professional
- Supportive
- Personalized
- Practical
- Actionable
- Structured
- Context Aware

Always use:

- Selected Role
- Current Skills
- Missing Skills
- Outdated Skills
- Trending Skills
- Recommended Roles
- Career Goal
- Completed Skills
- Previous Conversation History

When generating recommendations,
explain WHY they are relevant.

When generating roadmaps,
make them role-specific and personalized.

Avoid generic responses.
"""
    # ================= AI RESPONSE =================

    response = client.chat.completions.create(

        model=MODEL_NAME,

        messages=[
            {
                "role": "system",
                "content": system_prompt
            }
        ] + st.session_state.messages,

        temperature=0.7
    )

    ai_reply = response.choices[0].message.content

    # ================= SHOW AI =================

    with st.chat_message("assistant"):
        st.markdown(ai_reply)

    # ================= SAVE RESPONSE =================

    st.session_state.messages.append({

        "role": "assistant",
        "content": ai_reply
    })