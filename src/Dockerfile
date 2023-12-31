FROM python:3.9-slim  # Base image

WORKDIR /app  # Working directory

COPY requirements.txt requirements.txt  # Copy requirements file
RUN pip install -r requirements.txt  # Install dependencies

COPY api .  # Copy all project files

EXPOSE 8000  # Expose port 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]  # Start the server
