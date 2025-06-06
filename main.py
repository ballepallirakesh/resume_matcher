from parser.resume_parser import extract_resume_text
from utils.text_cleaner import clean_text
from matcher.job_matcher import match_resume_to_jobs

def main():
    resume_path = "resumes/sample_resume.pdf"

    print("📄 Extracting resume text...")
    resume_text = extract_resume_text(resume_path)

    if not resume_text:
        print("❌ Resume text could not be extracted.")
        return

    print("\n🧼 Cleaning resume text...")
    cleaned_resume = clean_text(resume_text)

    print("\n🔍 Matching resume to job descriptions...")
    best_match, score = match_resume_to_jobs(cleaned_resume)

    print("\n🎯 Best Job Match:")
    print(f"📌 Title: {best_match}")
    print(f"✅ Similarity Score: {score:.2f}")

if __name__ == "__main__":
    main()
