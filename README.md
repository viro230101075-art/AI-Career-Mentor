# 🎓 AI Career Mentor

An AI-powered career guidance platform that helps students and professionals explore career opportunities, receive personalized recommendations, generate learning roadmaps, analyze resumes, and discover growth opportunities using Google Gemini and a structured knowledge retrieval system.

---

## 🚀 Overview

AI Career Mentor combines the power of **Google Gemini**, **knowledge retrieval**, and **session memory** to provide intelligent career guidance tailored to individual users.

The system supports:

* Career exploration across multiple domains
* Personalized career recommendations
* Skill and certification suggestions
* Higher education guidance
* Resume analysis
* Career roadmap generation
* Multi-language support
* Context-aware follow-up conversations

---

## ✨ Key Features

### 🤖 AI-Powered Career Guidance

Uses Google Gemini to provide intelligent and personalized career advice.

### 🧠 Career Memory

Remembers the user's selected career domain and previous interactions for contextual follow-up responses.

### 📚 Knowledge Retrieval System

Retrieves structured information from JSON knowledge bases including:

* Career descriptions
* Required skills
* Certifications
* Courses
* Higher education opportunities

### 🗺️ Personalized Career Roadmaps

Generates customized learning plans based on:

* Education level
* Career goal
* Existing skills
* Available study time

### 📄 Resume Analysis

Analyzes resumes and provides:

* Skill identification
* Strengths assessment
* Improvement suggestions
* Career recommendations

### 🌍 Multi-Language Support

Allows users to interact with the system in multiple languages.

### 🔄 Fallback Knowledge Base

If the Gemini API is unavailable, the application automatically falls back to the local knowledge base to ensure uninterrupted functionality.

---

## 🏗️ System Architecture

```text
User Query
     │
     ▼
Career Detection
     │
     ▼
Knowledge Retrieval (JSON)
     │
     ▼
Google Gemini LLM
     │
     ▼
Personalized Response
     │
     ▼
Session Memory Update
```

---

## 🛠️ Technology Stack

| Component       | Technology              |
| --------------- | ----------------------- |
| Frontend        | Streamlit               |
| Backend         | Python                  |
| LLM             | Google Gemini           |
| Knowledge Base  | JSON                    |
| Memory System   | Streamlit Session State |
| Resume Analysis | Python Processing       |
| Version Control | Git & GitHub            |

---

## 📂 Project Structure

```text
AI-Career-Mentor/
│
├── app.py
├── chatbot.py
├── knowbase.py
├── memory.py
├── roadmap.py
├── resana.py
├── prompt.py
├── requirements.txt
│
├── data/
│   ├── career.json
│   ├── certificates.json
│   ├── courses.json
│   └── highedu.json
│
├── docs/
│   ├── archi.md
│   └── workflow.md
│
└── screenshots/
```

---

## 🔍 Workflow

1. User enters a career-related query.
2. Career domain is detected automatically.
3. Relevant information is retrieved from the knowledge base.
4. Gemini generates a personalized response using retrieved context.
5. User preferences and career selections are stored in memory.
6. Roadmaps, certifications, courses, and higher education suggestions are generated.
7. Resume analysis and multilingual support are provided when required.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/viro230101075-art/AI-Career-Mentor.git
cd AI-Career-Mentor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

### Run Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots of:

* Career Guidance Chat
* AI Response Generation
* Roadmap Generator
* Resume Analysis
* Multi-Language Support

inside the `screenshots` folder.

---

## 🎯 Future Enhancements

* Voice-based career assistant
* Job recommendation system
* RAG using vector databases
* Interview preparation module
* Career progress tracking
* Internship recommendation engine

---

## 👨‍💻 Author

**V. Koushik Sai Raj**

B.Tech Computer Science & Engineering

IIIT Manipur

---

## 📄 License

This project is developed for Educational purposes.
