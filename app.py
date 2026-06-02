import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv

from prompt import SYSTEM_PROMPT

from knowbase import (
    detect_career,
    get_career_info,
    get_certifications,
    get_courses,
    get_higher_education
)
language = st.selectbox(
    "Language",
    [
        "English",
        "Hindi",
        "Telugu"
    ]
)
from roadmap import generate_roadmap

# ==========================
# GEMINI CONFIG
# ==========================

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# ==========================
# STREAMLIT CONFIG
# ==========================

st.set_page_config(
    page_title="AI Career Mentor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Career Mentor")

st.markdown("""
Welcome to AI Career Mentor.

Get:
- Career Guidance
- Certifications
- Courses
- Higher Education Advice
- Personalized Roadmaps
""")

# ==========================
# SESSION STATE
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "career" not in st.session_state:
    st.session_state.career = None

if "education" not in st.session_state:
    st.session_state.education = ""

if "skills" not in st.session_state:
    st.session_state.skills = ""

if "study_time" not in st.session_state:
    st.session_state.study_time = ""

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("Career Domains")

st.sidebar.markdown("""
### Available Domains

- Artificial Intelligence
- Data Science
- Software Development
- Cybersecurity
- Agriculture Technology
- Food Technology
- Business & Management
- Design & Creative Fields
""")

if st.session_state.career:
    st.sidebar.success(
        f"Current Career: {st.session_state.career}"
    )
else:
    st.sidebar.info(
        "No career selected yet"
    )

# ==========================
# CHAT SECTION
# ==========================

st.header("Career Guidance Chat")

user_input = st.text_input(
    "Ask a career-related question"
)

if st.button("Send"):

    if user_input:

        career = detect_career(user_input)

        if career:
            st.session_state.career = career

        if st.session_state.career is None:
            st.session_state.career = "Artificial Intelligence"

        current_career = st.session_state.career

        # Retrieval Layer
        career_info = get_career_info(current_career)

        certs = get_certifications(current_career)

        courses = get_courses(current_career)

        higher_ed = get_higher_education(current_career)

        # Gemini Prompt
        full_prompt = f"""
{SYSTEM_PROMPT}

Respond in:
{language}

Current Career Domain:
{current_career}

Knowledge Base Information

Career Details:
{career_info}

Certifications:
{certs}

Courses:
{courses}

Higher Education:
{higher_ed}

Conversation Context:
Current Career = {current_career}

User Query:
{user_input}

Instructions:

1. Use the supplied knowledge base information.
2. Personalize the response.
3. Explain why recommendations are useful.
4. Use headings and bullet points.
5. Answer follow-up questions using remembered context.
6. Do not simply repeat raw data.
"""

        try:

          response = model.generate_content(
            full_prompt
          )

          bot_response = "GEMINI\n\n" + response.text

        except Exception as e:

          bot_response = f"""
❌ GEMINI FAILED

ERROR:
{str(e)}
## Career Domain
{current_career}

## Career Information
{career_info.get('description', 'N/A')}

## Required Skills
{', '.join(career_info.get('skills', []))}

## Recommended Certifications
{', '.join(certs)}

## Recommended Courses
{', '.join(courses)}

## Higher Education

### Countries
{', '.join(higher_ed.get('countries', []))}

### Exams
{', '.join(higher_ed.get('exams', []))}

### Scholarships
{', '.join(higher_ed.get('scholarships', []))}
"""

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": bot_response
            }
        )

# ==========================
# CHAT HISTORY
# ==========================

st.subheader("Conversation")

for msg in st.session_state.messages:

   if msg["role"] == "user":
    with st.chat_message("user"):
        st.write(msg["content"])

   else:
    with st.chat_message("assistant"):
        st.write(msg["content"])

# ==========================
# ROADMAP GENERATOR
# ==========================

st.header("Personalized Career Roadmap")

education = st.text_input(
    "Education Level",
    value=st.session_state.education
)

career_goal = st.text_input(
    "Career Goal",
    value=st.session_state.career or ""
)

skills = st.text_input(
    "Current Skills",
    value=st.session_state.skills
)

study_time = st.text_input(
    "Study Time Per Week",
    value=st.session_state.study_time
)

if st.button("Generate Roadmap"):

    st.session_state.education = education
    st.session_state.skills = skills
    st.session_state.study_time = study_time

    roadmap = generate_roadmap(
        education,
        career_goal,
        skills,
        study_time
    )

    st.text_area(
        "Roadmap",
        roadmap,
        height=350
    )
st.header("Resume Analysis")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "txt"]
)
from resana import extract_resume_text
if uploaded_file:

    resume_text = extract_resume_text(
        uploaded_file
    )

    prompt = f"""
Analyze this resume.

Resume:

{resume_text}

Provide:

1. Key Skills
2. Strengths
3. Weaknesses
4. Missing Skills
5. Career Recommendations
6. Certifications
"""

    response = model.generate_content(
        prompt
    )

    st.markdown(response.text)