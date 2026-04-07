<<<<<<< HEAD
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Hugging Face Spaces always use port 7860
EXPOSE 7860

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
=======
# FROM python:3.10

# WORKDIR /app

# COPY . .

# RUN pip install --no-cache-dir -r requirements.txt

# # Hugging Face Spaces always use port 7860
# EXPOSE 7860

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
# -------------
FROM python:3.10

WORKDIR /app

# Install uv globally
RUN pip install --upgrade pip && pip install uv

# Copy requirements (or pyproject.toml/uv.lock if using modern dependency management)
COPY requirements.txt .

# Always create the venv first (this line wipes the old .venv, so must be before installs)
RUN uv venv .venv

# Install dependencies INTO the current .venv
RUN uv pip install -r requirements.txt

COPY . .

EXPOSE 7860 7860

ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "app.py"]
>>>>>>> b266043 (Updated Dockerfile)
