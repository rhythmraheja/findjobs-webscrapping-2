import spacy
import docx2txt
import PyPDF2
import re
import os
import requests
spacy.cli.download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")
API_URL = "https://api-inference.huggingface.co/models/Nucha/Nucha_ITSkillNER_BERT"
HEADERS = {"Authorization": "Bearer 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"}

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(docx_path):
    return docx2txt.process(docx_path)






  # Replace with your API key

def extract_skills(text):
    try:
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": text})
        
        # Handle API errors
        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")
            return []
        
        entities = response.json()
        
        # Extract skills from the API response
        skills = [entity["word"] for entity in entities if "skill" in entity["entity"].lower()]
        return list(set(skills))  # Remove duplicates

    except Exception as e:
        print(f"Exception occurred: {e}")
        return []





def parse_resume(file_path):
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        return []

    return extract_skills(text)