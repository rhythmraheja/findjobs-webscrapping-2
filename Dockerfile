# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Spacy model
RUN python -m spacy download en_core_web_sm

# Expose port 5000 (or any other port your Flask app runs on)
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=backend.app
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "backend.app:app"]
