# Build stage
FROM python:3.12-slim-bookworm AS builder

# Set shell to bash for better error handling
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install uv for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy dependency files first for caching
COPY pyproject.toml uv.lock ./

# Install dependencies (frozen to lockfile, no dev dependencies)
RUN uv sync --frozen --no-dev

# Final stage
FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /app

# Copy the installed environment from builder
COPY --from=builder /app /app

# Set PATH to use the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Copy the rest of the application
COPY . .

# Metadata
LABEL maintainer="Chimera CloudOps"
LABEL version="0.1.0"

# Default command: run tests
# Professional environment should use pytest and return proper exit codes
CMD ["pytest", "tests/"]
