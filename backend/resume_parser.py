import os
import spacy
import nltk
from pyresparser import ResumeParser

# Download necessary resources
nltk.download('stopwords')
spacy.cli.download("en_core_web_sm")

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_skills(resume_path):
    try:
        if not os.path.exists(resume_path):
            print("Error: File not found!")
            return []
            
        data = ResumeParser(resume_path).get_extracted_data()
        return data.get("skills", [])  # Returns extracted skills or empty list if not found

    except Exception as e:
        print(f"Error extracting skills: {e}")
        return []

def parse_resume(file_path):
    return extract_skills(file_path)

