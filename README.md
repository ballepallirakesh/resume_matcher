# 🧠 AI-Powered Resume Parser & Job Matcher

This Python-based project automatically extracts content from resumes and matches it with job descriptions using NLP and machine learning.

## 🚀 Features
- 📄 Extracts resume text from PDF using `pdfplumber`
- 🧼 Cleans and preprocesses text using `spaCy`
- 🤖 Matches resumes to job roles using TF-IDF + Cosine Similarity
- 📊 Outputs the best matching job title and relevance score

## 📁 Project Structure

resume_matcher/
├── main.py
├── parser/
│ └── resume_parser.py
├── matcher/
│ └── job_matcher.py
├── jobs/
│ └── job_descriptions.json
├── resumes/
│ └── sample_resume.pdf
├── utils/
│ └── text_cleaner.py
├── README.md
└── requirements.txt

## 📦 Setup Instructions

1. **Clone this repo**
   ```bash
   git clone https://github.com/your-username/resume_matcher.git
   cd resume_matcher
Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm
Run the app
python main.py
🧪 Sample Output
📄 Extracting resume text...
🧼 Cleaning resume text...
🔍 Matching resume to job descriptions...

🎯 Best Job Match:
📌 Title: Python Developer
✅ Similarity Score: 0.76
🛠️ Tech Stack
Python
pdfplumber
spaCy
scikit-learn
NLP, Cosine Similarity
📌 Use Cases
Job seekers can tailor resumes for better job matches
HR professionals can auto-screen candidates
📧 Contact
Developed by Rakesh Ballepalli
📧 rakeshballepalli@gmail.com