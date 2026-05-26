# 🌍 AI Remote Job Matcher

An AI-powered web application that helps users discover relevant remote jobs by matching their resumes against live job postings using NLP-based similarity scoring.

The project fetches real-time remote jobs from the internet, analyzes uploaded resumes, identifies skill gaps, and ranks opportunities based on relevance.

Built using Python, Streamlit, and Machine Learning concepts like TF-IDF and cosine similarity.

---

# 🚀 Features

- Upload resumes in PDF or DOCX format
- Fetch live remote jobs from online APIs
- AI-based resume-to-job matching
- Match score ranking in descending order
- Missing skill detection
- Direct apply links
- Interactive Streamlit dashboard
- Market skill insights visualization

---

# 🧠 How It Works

The application follows this workflow:

1. User uploads a resume
2. Resume text is extracted and processed
3. Live remote jobs are fetched online
4. Resume and job descriptions are converted into TF-IDF vectors
5. Cosine similarity is calculated
6. Jobs are ranked based on similarity score
7. Missing skills are identified from job descriptions

---

# 🏗️ Tech Stack

## Frontend
- Streamlit

## Backend / ML
- Python
- scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

## Resume Parsing
- pdfplumber
- python-docx

## Data Handling
- pandas
- BeautifulSoup4

## Job Source
- RemoteOK API

---

# 📂 Project Structure

```text
Job_Matcher/
│
├── app.py
├── requirements.txt
│
├── src/
│   ├── fetch_jobs.py
│   ├── matcher.py
│   ├── parser.py
│   └── skills.py
```

---

# ⚡ Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

## Move into the Project Folder

```bash
cd Job_Matcher
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

---

# 📄 Resume Upload Support

Supported file formats:
- PDF
- DOCX

---

# 📊 Matching Engine

The matching system uses Natural Language Processing techniques to compare resumes with job descriptions.

### TF-IDF Vectorization
Converts textual information into numerical vectors.

### Cosine Similarity
Measures similarity between:
- Resume content
- Job descriptions

Jobs are then ranked based on relevance score.

---

# 🎯 Skill Gap Detection

The application extracts skills from:
- Uploaded resumes
- Job descriptions

Then identifies missing skills required for each role.

Example:

```python
missing_skills = job_skills - resume_skills
```

This helps users understand:
- missing technologies
- learning gaps
- job readiness

---

# 🌐 Live Remote Jobs

The project fetches real-time remote jobs using the RemoteOK API.

Each job includes:
- Title
- Company
- Location
- Description
- Apply link

---

# 📸 Current Capabilities

- Live remote job search
- Resume parsing
- AI-based job ranking
- Skill analysis
- Interactive dashboard
- Real-time recommendations

---

# 🚀 Future Improvements

Planned upgrades:
- Sentence-transformer embeddings
- Semantic search
- Better skill extraction
- Resume optimization suggestions
- Cover letter generation
- Multi-platform job scraping
- LLM integration

---

# 💼 Resume Project Description

> Developed an AI-powered remote job matching platform that fetches live remote jobs and ranks opportunities against uploaded resumes using NLP-based similarity scoring. Implemented PDF/DOCX parsing, skill-gap analysis, and an interactive Streamlit dashboard.

---

# 🧠 Concepts Used

- Natural Language Processing (NLP)
- Information Retrieval
- Recommendation Systems
- Semantic Similarity
- Feature Engineering
- Streamlit Deployment

---

# 📦 Requirements

```text
streamlit
pandas
scikit-learn
pdfplumber
python-docx
requests
beautifulsoup4
```

---

# 👨‍💻 Author

Satyam Anand

Data Analyst | ML Enthusiast | AI/NLP Projects

---

# ⭐ Acknowledgements

Inspired by the growing need for AI-assisted career tools and intelligent job discovery systems.