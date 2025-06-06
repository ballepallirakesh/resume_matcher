from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.text_cleaner import clean_text
import json

def load_job_descriptions(path="jobs/job_descriptions.json"):
    with open(path, "r") as file:
        return json.load(file)

def match_resume_to_jobs(cleaned_resume):
    jobs = load_job_descriptions()
    
    job_texts = [clean_text(job["description"]) for job in jobs]
    titles = [job["title"] for job in jobs]

    # Combine resume and job descriptions into one list
    all_texts = [cleaned_resume] + job_texts

    # Convert text into TF-IDF vectors
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(all_texts)

    # Compute cosine similarity between resume (index 0) and all job descriptions
    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    # Find the index of the best matching job
    best_match_index = similarities.argmax()
    best_match_score = similarities[best_match_index]

    return titles[best_match_index], best_match_score
