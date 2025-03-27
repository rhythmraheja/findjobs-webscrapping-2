import spacy
import docx2txt
import PyPDF2
import re
import os
spacy.cli.download("en_core_web_sm")

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(docx_path):
    return docx2txt.process(docx_path)

def extract_skills(resume_text):
    skills = set()
    keywords = ["Python", "Flask", "SQL", "Machine Learning", "Web Scraping", "Django"]
    for word in keywords:
        if re.search(rf"\b{word}\b", resume_text, re.IGNORECASE):
            skills.add(word)
    return list(skills)

def parse_resume(file_path):
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        return []

    return extract_skills(text)