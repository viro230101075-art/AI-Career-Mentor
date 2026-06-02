def generate_roadmap(
    education,
    career_goal,
    skills,
    study_time
):

    goal = career_goal.lower().strip()

    # ==========================
    # AI / ML
    # ==========================

    if (
        "artificial intelligence" in goal
        or "ai engineer" in goal
        or "machine learning" in goal
        or "ml engineer" in goal
    ):

        roadmap = """
Month 1:
- Advanced Python

Month 2:
- Statistics and Linear Algebra

Month 3:
- Machine Learning

Month 4:
- Deep Learning

Month 5:
- NLP and Computer Vision

Month 6:
- AI Projects

Month 7:
- Resume and GitHub

Month 8:
- Internship Preparation
"""

    # ==========================
    # SOFTWARE DEVELOPMENT
    # ==========================

    elif (
        "software" in goal
        or "developer" in goal
        or "full stack" in goal
        or "backend" in goal
        or "frontend" in goal
    ):

        roadmap = """
Month 1:
- Python or Java

Month 2:
- Data Structures

Month 3:
- Algorithms

Month 4:
- OOP and Databases

Month 5:
- Web Development

Month 6:
- Full Stack Project

Month 7:
- Resume and GitHub

Month 8:
- Placement Preparation
"""

    # ==========================
    # CYBERSECURITY
    # ==========================

    elif (
        "cyber" in goal
        or "security analyst" in goal
        or "ethical hacker" in goal
    ):

        roadmap = """
Month 1:
- Networking Basics

Month 2:
- Linux

Month 3:
- Security Fundamentals

Month 4:
- Ethical Hacking

Month 5:
- Web Security

Month 6:
- Security Projects

Month 7:
- Security Certifications

Month 8:
- Internship Preparation
"""

    # ==========================
    # DATA SCIENCE
    # ==========================

    elif (
        "data scientist" in goal
        or "data science" in goal
        or "data analyst" in goal
    ):

        roadmap = """
Month 1:
- Python

Month 2:
- Statistics

Month 3:
- SQL

Month 4:
- Data Analysis

Month 5:
- Machine Learning

Month 6:
- Data Science Projects

Month 7:
- Dashboard Building

Month 8:
- Interview Preparation
"""

    # ==========================
    # FOOD TECHNOLOGY
    # ==========================

    elif (
        "food" in goal
        or "fssai" in goal
        or "food safety" in goal
    ):

        roadmap = """
Month 1:
- Food Science Fundamentals

Month 2:
- Food Processing Techniques

Month 3:
- Food Safety Standards

Month 4:
- HACCP and Quality Control

Month 5:
- Food Packaging

Month 6:
- Industry Training

Month 7:
- Regulatory Compliance

Month 8:
- Placement Preparation
"""

    # ==========================
    # AGRICULTURE
    # ==========================

    elif (
        "agriculture" in goal
        or "agri" in goal
    ):

        roadmap = """
Month 1:
- Agricultural Fundamentals

Month 2:
- Soil Science

Month 3:
- Crop Production

Month 4:
- Farm Management

Month 5:
- Agri Technology

Month 6:
- Field Projects

Month 7:
- Internship Preparation

Month 8:
- Placement Preparation
"""

    # ==========================
    # BUSINESS
    # ==========================

    elif (
        "business" in goal
        or "management" in goal
        or "manager" in goal
    ):

        roadmap = """
Month 1:
- Business Fundamentals

Month 2:
- Marketing

Month 3:
- Finance Basics

Month 4:
- Operations Management

Month 5:
- Leadership Skills

Month 6:
- Business Projects

Month 7:
- Resume Preparation

Month 8:
- Placement Preparation
"""

    # ==========================
    # DESIGN
    # ==========================

    elif (
        "design" in goal
        or "ui" in goal
        or "ux" in goal
        or "graphic" in goal
    ):

        roadmap = """
Month 1:
- Design Principles

Month 2:
- UI Design

Month 3:
- UX Research

Month 4:
- Figma

Month 5:
- Portfolio Building

Month 6:
- Design Projects

Month 7:
- Resume and Portfolio

Month 8:
- Internship Preparation
"""

    else:

        roadmap = """
Month 1:
- Learn Fundamentals

Month 2:
- Build Core Skills

Month 3:
- Projects

Month 4:
- Advanced Learning
"""

    return f"""
=================================
PERSONALIZED ROADMAP
=================================

Education:
{education}

Career Goal:
{career_goal}

Current Skills:
{skills}

Study Time:
{study_time}

---------------------------------

{roadmap}
"""