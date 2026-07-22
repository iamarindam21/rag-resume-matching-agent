import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")

def extract_candidate_info(resume_text):
    prompt = f"""
    Extract the following from this resume as JSON:
    - name
    - skills (list)
    - years_of_experience
    - education

    Resume:
    {resume_text}

    Return ONLY valid JSON, nothing else.
    """
    response = model.generate_content(prompt)
    return response.text

from read_resume import resume_text
if __name__ == "__main__":
    print("--- Available embedding models ---")
    for m in genai.list_models():
        if 'embedContent' in m.supported_generation_methods:
            print(m.name)