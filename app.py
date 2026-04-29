import streamlit as st
import pdfplumber
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import plotly.graph_objects as go

# =========================
# MODEL
# =========================
model = SentenceTransformer('all-MiniLM-L6-v2')

# =========================
# FUNCTIONS
# =========================

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def compute_similarity(resume_text, job_desc):
    emb1 = model.encode(resume_text)
    emb2 = model.encode(job_desc)
    return round(cosine_similarity([emb1], [emb2])[0][0] * 100, 2)


def extract_skills(text):
    skills_db = [
        "python","java","c++","machine learning","deep learning",
        "nlp","data science","sql","tensorflow","pytorch",
        "docker","kubernetes","aws","git","linux","html","css","javascript"
    ]
    return [s for s in skills_db if s in text.lower()]


def missing_skills(resume_skills, job_desc):
    job_skills = extract_skills(job_desc)
    return list(set(job_skills) - set(resume_skills))


# =========================
# FREE AI (NO API)
# =========================

def llm_feedback(resume_text, job_desc):
    feedback = []

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)
    missing = list(set(job_skills) - set(resume_skills))

    feedback.append("🔍 Resume Analysis:\n")

    if len(resume_skills) > 5:
        feedback.append("✅ Good number of technical skills")
    else:
        feedback.append("⚠️ Add more relevant skills")

    if missing:
        feedback.append(f"❌ Missing skills: {', '.join(missing)}")
    else:
        feedback.append("✅ Skills match is strong")

    if "project" not in resume_text.lower():
        feedback.append("⚠️ Add projects section")

    if "%" not in resume_text:
        feedback.append("⚠️ Add measurable achievements (numbers, % etc.)")

    return "\n".join(feedback)


def improve_bullets(text):
    lines = text.split("\n")
    improved = []

    for line in lines:
        if line.strip():
            improved.append(f"• {line} → Improved with impact and measurable results")

    return "\n".join(improved)


# =========================
# UI
# =========================

st.set_page_config(page_title="AI Resume Screener (FREE)", layout="wide")

st.title("🚀 AI Resume Screener (FREE VERSION)")
st.markdown("### Resume Analysis using NLP + Semantic Matching (No API Required)")

menu = st.sidebar.selectbox("Menu", ["Analyzer", "Multi Job", "Resume Feedback", "Bullet Improver"])


# =========================
# ANALYZER
# =========================

if menu == "Analyzer":
    col1, col2 = st.columns(2)

    with col1:
        resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    with col2:
        job_desc = st.text_area("Paste Job Description")

    if st.button("Analyze Resume"):
        if resume_file and job_desc:
            resume_text = extract_text_from_pdf(resume_file)

            score = compute_similarity(resume_text, job_desc)
            skills = extract_skills(resume_text)
            missing = missing_skills(skills, job_desc)

            st.success("Analysis Complete!")

            c1, c2, c3 = st.columns(3)
            c1.metric("Match %", score)
            c2.metric("Skills Found", len(skills))
            c3.metric("Missing Skills", len(missing))

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                title={'text': "Match Score"},
                gauge={'axis': {'range': [0, 100]}}
            ))
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("✅ Skills Found")
            st.write(skills)

            st.subheader("❌ Missing Skills")
            st.write(missing)

        else:
            st.error("Please upload resume and enter job description")


# =========================
# MULTI JOB MATCH
# =========================

elif menu == "Multi Job":
    resume_file = st.file_uploader("Upload Resume", type=["pdf"])

    job1 = st.text_area("Job 1")
    job2 = st.text_area("Job 2")
    job3 = st.text_area("Job 3")

    if st.button("Compare Jobs"):
        if resume_file:
            resume_text = extract_text_from_pdf(resume_file)

            scores = []
            for job in [job1, job2, job3]:
                if job:
                    scores.append(compute_similarity(resume_text, job))
                else:
                    scores.append(0)

            st.write("Match Scores:", scores)


# =========================
# RESUME FEEDBACK
# =========================

elif menu == "Resume Feedback":
    resume_file = st.file_uploader("Upload Resume", type=["pdf"])
    job_desc = st.text_area("Job Description")

    if st.button("Get Feedback"):
        if resume_file and job_desc:
            resume_text = extract_text_from_pdf(resume_file)

            feedback = llm_feedback(resume_text, job_desc)

            st.subheader("💡 Resume Feedback")
            st.write(feedback)


# =========================
# BULLET IMPROVER
# =========================

elif menu == "Bullet Improver":
    text = st.text_area("Paste your resume bullet points")

    if st.button("Improve"):
        if text:
            improved = improve_bullets(text)

            st.subheader("✨ Improved Version")
            st.write(improved)
