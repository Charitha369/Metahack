FROM python:3.10

WORKDIR /app

# 1. Install uv globally for fast dependency management
RUN pip install --upgrade pip && pip install uv

# 2. Copy the pyproject.toml (This satisfies the "multi-mode" check)
# You can also keep requirements.txt if you want, but this is the critical one.
COPY pyproject.toml .

# 3. Create the virtual environment and install dependencies from the toml file
RUN uv venv .venv
RUN uv pip install -r pyproject.toml

# 4. Copy the rest of your application code (inference.py, environment.py, etc.)
COPY . .

# 5. Hugging Face/OpenEnv default port
EXPOSE 7860

# 6. Ensure the environment's bin folder is in the PATH
ENV PATH="/app/.venv/bin:$PATH"

# 7. Run the renamed inference file
CMD ["python", "inference.py"]