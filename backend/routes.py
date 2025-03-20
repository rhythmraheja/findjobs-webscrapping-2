from flask import Blueprint, request, jsonify
from resume_parser import parse_resume
from job_scraper import scrape_jobs
from models import db, Job
import os

resume_routes = Blueprint("resume_routes", __name__)
job_routes = Blueprint("job_routes", __name__)
UPLOAD_FOLDER = "/tmp/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True) 

@resume_routes.route("/upload", methods=["POST"])
def upload_resume():
    file = request.files["resume"]
    file_path=os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    skills = parse_resume(file_path)
    return jsonify({"skills": skills})

@job_routes.route("/get_jobs", methods=["POST"])
def get_jobs():
    skills = request.json.get("skills", [])
    all_jobs = []

    for skill in skills:
        jobs = scrape_jobs(skill)
        all_jobs.extend(jobs)

    return jsonify({"jobs": all_jobs})
