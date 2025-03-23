import spacy
import docx2txt
import PyPDF2
import re
import os
from pyresparser import ResumeParser
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
