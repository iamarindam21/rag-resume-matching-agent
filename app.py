import streamlit as st
from read_resume import read_pdf
from extract_info import extract_candidate_info
from similarity import get_embedding, cosine_similarity

st.title("Resume Screening Agent")
st.write("Upload a resume and paste a job description to see how well they match.")

job_description = st.text_area("Paste job description")
uploaded_file = st.file_uploader("Upload resume (PDF)", type="pdf")

if st.button("Analyze") and uploaded_file and job_description:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_text = read_pdf("temp_resume.pdf")

    st.subheader("Extracted Candidate Info")
    info = extract_candidate_info(resume_text)
    st.write(info)

    st.subheader("Match Score")
    job_emb = get_embedding(job_description)
    resume_emb = get_embedding(resume_text)
    score = cosine_similarity(job_emb, resume_emb)
    st.write(f"Similarity Score: {score:.4f} ({score*100:.1f}%)")