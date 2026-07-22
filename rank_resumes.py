from similarity import get_embedding, cosine_similarity
from read_resume import read_pdf

# Add multiple resume file paths here
resume_files = {
    "resume1": "sample_resume.pdf",
    # add more, e.g. "resume2": "another_resume.pdf"
}

job_description = """
Paste a sample job description here — e.g.:
Looking for a Data Analyst with experience in Excel, Power BI,
Python, and data visualization. 1-2 years experience preferred.
"""

def rank_resumes(resume_files, job_description):
    job_embedding = get_embedding(job_description)
    scores = {}

    for name, path in resume_files.items():
        text = read_pdf(path)
        emb = get_embedding(text)
        score = cosine_similarity(job_embedding, emb)
        scores[name] = score

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked

if __name__ == "__main__":
    results = rank_resumes(resume_files, job_description)
    for name, score in results:
        print(f"{name}: {score:.4f}")