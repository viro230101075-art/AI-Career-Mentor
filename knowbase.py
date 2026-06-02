import json


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


# Load all knowledge base files
careers = load_json("data/career.json")
certifications = load_json("data/certificates.json")
courses = load_json("data/courses.json")
higher_education = load_json("data/highedu.json")


def get_career_info(career_name):
    return careers.get(career_name, {})


def get_certifications(career_name):
    return certifications.get(career_name, [])


def get_courses(career_name):
    return courses.get(career_name, [])


def get_higher_education(career_name):
    return higher_education.get(career_name, {})


def detect_career(user_query):

    query = user_query.lower().strip()

    if (
        "artificial intelligence" in query
        or "ai engineer" in query
        or "machine learning" in query
    ):
        return "Artificial Intelligence"

    elif (
        "data science" in query
        or "data scientist" in query
        or "data analyst" in query
    ):
        return "Data Science"

    elif (
        "software" in query
        or "developer" in query
        or "full stack" in query
        or "frontend" in query
        or "backend" in query
    ):
        return "Software Development"

    elif (
        "cyber" in query
        or "security analyst" in query
        or "ethical hacker" in query
    ):
        return "Cybersecurity"

    elif (
        "agriculture" in query
        or "agri" in query
    ):
        return "Agriculture Technology"

    elif (
        "food" in query
        or "fssai" in query
        or "food safety" in query
    ):
        return "Food Technology"

    elif (
        "business" in query
        or "management" in query
    ):
        return "Business & Management"

    elif (
        "design" in query
        or "ui" in query
        or "ux" in query
        or "graphic" in query
    ):
        return "Design & Creative Fields"

    return None

if __name__ == "__main__":

    print(get_career_info("Artificial Intelligence"))

    print(get_certifications("Artificial Intelligence"))

    print(get_courses("Artificial Intelligence"))

    print(get_higher_education("Artificial Intelligence"))