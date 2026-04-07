# 🤖 AI Resume Screening System

An AI-powered web application that screens and ranks resumes based on job descriptions using Natural Language Processing (NLP).

---

## 🚀 Live Demo  
👉 [Click Here to Use the App](https://ai-resume-screener-khlpqxczr5nkwkk37pg4y9.streamlit.app)

---

## 📌 Features

- 📄 Upload multiple resumes (PDF)
- 🧠 Extract text using NLP
- 📊 Match resumes with job descriptions
- 🏆 Rank candidates based on similarity score
- 🔍 Extract key skills from resumes
- 🌐 Deployed as a live web app

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Scikit-learn  
- NLP (TF-IDF, Cosine Similarity)  
- pdfplumber  

---

## ⚙️ How It Works

1. Resume text is extracted from PDF files  
2. Text is cleaned and preprocessed  
3. TF-IDF converts text into numerical vectors  
4. Cosine similarity calculates match score  
5. Resumes are ranked based on relevance  

---

## 📂 Project Structure

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
