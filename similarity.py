import google.generativeai as genai
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_embedding(text):
    result = genai.embed_content(
    model="models/gemini-embedding-001",
    content=text
    )
    return result['embedding']

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))