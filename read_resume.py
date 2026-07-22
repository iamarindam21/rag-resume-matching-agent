import PyPDF2

def read_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

resume_text = read_pdf("sample_resume.pdf")
print(resume_text)