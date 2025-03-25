import os
import nltk
import spacy
from pyresparser import ResumeParser

# Ensure NLTK data is properly set up
nltk_data_path = "/opt/render/nltk_data"
os.makedirs(nltk_data_path, exist_ok=True)
nltk.data.path.append(nltk_data_path)

# Check and download stopwords only if missing
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords", download_dir=nltk_data_path)

# Load spaCy model (don't download it at runtime)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("spaCy model 'en_core_web_sm' not found. Install it before running.")

def extract_skills(resume_path):
    try:
        data = ResumeParser(resume_path).get_extracted_data()
        return data.get("skills", [])  # Returns the extracted skills or an empty list if not found
    except Exception as e:
        print(f"Error extracting skills: {e}")
        return []

def parse_resume(file_path):
    return extract_skills(file_path)
