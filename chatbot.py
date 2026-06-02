import google.generativeai as genai
import os
from dotenv import load_dotenv

from prompt import SYSTEM_PROMPT

from knowbase import (
    get_career_info,
    get_certifications,
    get_courses,
    get_higher_education,
    detect_career
)

from roadmap import generate_roadmap

from memory import (
    save_career,
    save_education,
    save_skills,
    save_study_time,
    get_memory
)

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

user_query = input("You: ")

# ==========================
# MEMORY CHECK
# ==========================

if "memory" in user_query.lower():

    print("\nCurrent Memory:\n")
    print(get_memory())

    exit()

# ==========================
# ROADMAP MODE
# ==========================

if "roadmap" in user_query.lower():

    education = input("Education Level: ")

    skills = input("Current Skills: ")

    study_time = input("Study Time Per Week: ")

    career_goal = input("Career Goal: ")

    save_education(education)
    save_skills(skills)
    save_study_time(study_time)
    save_career(career_goal)

    roadmap = generate_roadmap(
        education,
        career_goal,
        skills,
        study_time
    )

    print(roadmap)

    exit()

# ==========================
# CAREER DETECTION
# ==========================

career = detect_career(user_query)

if career is None:
    career = "Artificial Intelligence"

save_career(career)

career_info = get_career_info(career)

certs = get_certifications(career)

course_list = get_courses(career)

higher_ed = get_higher_education(career)

full_prompt = f"""
{SYSTEM_PROMPT}

Career Domain:
{career}

Knowledge Base Career Information:
{career_info}

Knowledge Base Certifications:
{certs}

Knowledge Base Courses:
{course_list}

Knowledge Base Higher Education:
{higher_ed}

User Query:
{user_query}
"""

try:

    response = model.generate_content(
        full_prompt
    )

    print("\nCareer Mentor:\n")

    print(response.text)

except Exception as e:

    print("\nError:")

    print(e)