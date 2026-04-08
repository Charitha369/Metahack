FROM python:3.10

WORKDIR /app

RUN pip install --upgrade pip && pip install uv

# Copy the dependency and lock files first
COPY pyproject.toml uv.lock ./

# Install based on the lock file
RUN uv venv .venv
RUN uv pip install -r pyproject.toml

# Copy everything else (including the /server folder)
COPY . .

EXPOSE 7860

ENV PATH="/app/.venv/bin:$PATH"

# Run the app
CMD ["python", "inference.py"]