from flask import Flask
from flask_cors import CORS
from routes import resume_routes, job_routes
from config import Config
from models import db
import os
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

app.config.from_object(Config)
db.init_app(app)

# Register routes
app.register_blueprint(resume_routes)
app.register_blueprint(job_routes)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment or default to 5000
    app.run(host="0.0.0.0", port=port)
