import spacy
import docx2txt
import PyPDF2
import re
import os
import nltk
from pyresparser import ResumeParser
nltk_data_path = "/opt/render/nltk_data"
os.makedirs(nltk_data_path, exist_ok=True)  # Create directory if it doesn't exist
nltk.data.path.append(nltk_data_path)  # Append to NLTK's search path
nltk.download('stopwords', download_dir=nltk_data_path)  


spacy.cli.download("en_core_web_sm")

nlp = spacy.load("en_core_web_sm")






def extract_skills(resume_path):
    try:
        data = ResumeParser(resume_path).get_extracted_data()
        return data.get("skills", [])  # Returns the extracted skills or an empty list if not found
    except Exception as e:
        print(f"Error extracting skills: {e}")
        return []


def parse_resume(file_path):
    return extract_skills(file_path)
