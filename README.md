# RAG Resume Matching Agent

## Overview
A RAG (Retrieval-Augmented Generation) application that screens resumes against
a job description. It extracts structured candidate information from a resume,
embeds resume and job description text, and computes a similarity score using
Google's Gemini API — demonstrating the core RAG pipeline end to end.

## How it works
1. **Ingestion** — Resume PDFs are parsed into raw text (PyPDF2)
2. **Extraction** — Gemini (gemini-flash-latest) extracts structured fields
   (name, skills, experience, education) from the raw text
3. **Embedding** — Resume text and job description are converted into vector
   embeddings using Gemini's embedding model (gemini-embedding-001)
4. **Retrieval/Scoring** — Cosine similarity measures how closely the resume
   matches the job description
5. **UI** — A Streamlit interface lets users upload a resume and paste a job
   description to see results interactively

## Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.12 |
| LLM / embeddings | Google Gemini API (`google-generativeai`) |
| PDF parsing | PyPDF2 |
| Similarity math | NumPy (cosine similarity) |
| UI | Streamlit |
| Hosting (code) | GitHub |
| Hosting (live app) | Streamlit Community Cloud (free tier) |
| Secrets management | `.env` locally, Streamlit Cloud "Secrets" in production |

## Running it
\`\`\`bash
pip install -r requirements.txt
streamlit run app.py
\`\`\`
Add your Gemini API key to a `.env` file:
\`\`\`
GEMINI_API_KEY=your_key_here
\`\`\`

## Example
Upload a resume PDF, paste a job description, click "Analyze" — the app
returns extracted candidate info and a similarity score (0-100%).

## Limitations
- Works best with well-formatted, text-based PDF resumes (not scanned images)
- Similarity scoring is a supporting signal, not a sole hiring decision
- Currently handles one resume at a time in the UI

## What I learned
Built this to understand the RAG pipeline hands-on — how embeddings capture
semantic meaning, why cosine similarity works for ranking relevance, and how
retrieval and generation combine to ground LLM outputs in real data. Also
worked through real-world API integration issues (deprecated model names,
rate limits) while building this.