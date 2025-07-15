# 🧠 AI Resume Screener & Matcher

A Streamlit app that helps users evaluate how well their resume matches a given job description.  
It provides a match score and lists missing skills/keywords to optimize your resume for better job opportunities.

---

## 🚀 Live Demo

🔗 [Click here to try the app](https://resume-screener-app-tswl5zfptube9tbxwd2vr4.streamlit.app)

---

## 🛠️ Features

- 📄 Upload PDF resumes
- 📝 Paste any job description
- ⚙️ Calculates **match score** using TF-IDF & cosine similarity
- 🔍 Lists top **missing keywords** from your resume
- 💡 Helps improve resume relevance for each job

---

## 📦 Tech Stack

- Python  
- Streamlit  
- scikit-learn  
- pdfminer.six (for PDF text extraction)

---

## 📁 Project Structure

```bash
resume-screener-app/
├── app.py
├── jd_matcher.py
├── requirements.txt
├── README.md
└── models/
```

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/halaae/resume-screener-app.git
cd resume-screener-app
pip install -r requirements.txt
streamlit run app.py
```

---

## 👩‍💻 Author

**Ayisha Hala**  
📫 [ayishatp78@gmail.com](mailto:ayishatp78@gmail.com)

---

## 💖 Contributions

Suggestions and improvements are welcome! Feel free to fork and create a pull request.

Add README for Resume Screener app

