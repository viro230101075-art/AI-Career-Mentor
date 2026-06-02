memory = {
    "career": None,
    "education": None,
    "skills": None,
    "study_time": None
}


def save_career(career):
    memory["career"] = career


def save_education(education):
    memory["education"] = education


def save_skills(skills):
    memory["skills"] = skills


def save_study_time(time):
    memory["study_time"] = time


def get_memory():
    return memory