import streamlit as st
import pdfplumber
import nltk
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
from nltk.corpus import stopwords

# ==============================
# PAGE CONFIG (UI)
# ==============================
st.set_page_config(page_title="AI Resume Screener", page_icon="🤖", layout="centered")

st.markdown("""
# 🤖 AI Resume Screening System
### Smart Candidate Ranking using NLP
""")

st.markdown("---")

# ==============================
# FUNCTIONS
# ==============================
def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text

def clean_text(text):
    text = re.sub(r'\W', ' ', text)
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])
    return text

# Skill keywords
skills_list = [
    "python","java","c++","machine learning","deep learning",
    "tensorflow","keras","nlp","data science","sql",
    "html","css","javascript","react","opencv"
]

# ==============================
# INPUT SECTION
# ==============================
uploaded_files = st.file_uploader("📄 Upload Multiple Resumes", type=["pdf"], accept_multiple_files=True)

job_description = st.text_area("📌 Enter Job Description", height=150)

# ==============================
# MAIN LOGIC
# ==============================
if uploaded_files and job_description:

    results = []

    for file in uploaded_files:
        resume_text = extract_text_from_pdf(file)

        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(job_description)

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([clean_resume, clean_jd])

        similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

        skills = [skill for skill in skills_list if skill in clean_resume]

        results.append({
            "name": file.name,
            "score": round(similarity * 100, 2),
            "skills": skills
        })

    # Sort resumes by score
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    st.markdown("## 🏆 Resume Ranking")

    for i, res in enumerate(results):
        st.markdown(f"### {i+1}. {res['name']}")
        st.write(f"📊 Match Score: {res['score']}%")

        st.write("🧠 Skills Found:")
        if res['skills']:
            for skill in res['skills']:
                st.write(f"✔ {skill}")
        else:
            st.write("No relevant skills found")

        st.markdown("---")