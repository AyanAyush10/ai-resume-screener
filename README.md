# 🚀 AI Resume Screening System

An AI-powered web application that analyzes resumes and matches them with job descriptions using NLP and semantic similarity.

---

## 🌐 Live Demo

👉 https://ai-resume-screener-klhpqcxz5nwkk37pg4y9.streamlit.app

---

## 📌 Overview

This project helps job seekers evaluate their resumes against job descriptions.  
It uses Natural Language Processing (NLP) and transformer-based embeddings to calculate similarity and identify missing skills.

---

## 🔥 Features

- 📄 Upload Resume (PDF format)
- 🧠 Semantic matching using Sentence Transformers
- 📊 Resume vs Job Description match score
- 🛠 Skill extraction from resume
- ❌ Missing skill detection
- 💡 Resume feedback system
- ✍️ Bullet point improvement tool
- 🌐 Deployed as a live web application

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** (Frontend + Deployment)
- **Sentence Transformers** (Semantic similarity)
- **Scikit-learn** (Cosine similarity)
- **PDFPlumber** (PDF text extraction)

---

## ⚙️ How It Works

1. User uploads a resume (PDF)
2. Extracts text using PDF processing
3. Converts resume and job description into embeddings
4. Computes similarity score using cosine similarity
5. Extracts skills and compares with job requirements
6. Provides feedback and improvement suggestions

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

## 🙌 Author

**Ayan Ayush**  
- GitHub: https://github.com/AyanAyush10  
- LinkedIn: https://www.linkedin.com/in/ayan-ayush-7bb083265/
