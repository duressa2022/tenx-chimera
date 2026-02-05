FROM python:3.12-slim

# Install uv and pytest
RUN pip install uv && uv pip install pytest

# Set workdir
WORKDIR /app

# Copy project files
COPY .. /app

# Default command: run tests (intentionally failing)
CMD ["uv", "pip", "run", "pytest", "tests/"]
