# Chimera Automation Makefile

DOCKER_IMAGE = tenx-chimera
DOCKER_TAG = latest

.PHONY: help setup build test spec-check clean

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  setup       Install dependencies and initialize the environment"
	@echo "  build       Build the Docker image"
	@echo "  test        Run tests inside a Docker container"
	@echo "  spec-check  Run specification compliance check script"
	@echo "  clean       Remove build artifacts and temporary files"

setup:
	@echo "Setting up local development environment..."
	uv venv
	uv sync

build:
	@echo "Building Docker image $(DOCKER_IMAGE):$(DOCKER_TAG)..."
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

test:
	@echo "Running tests in Docker..."
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .
	docker run --rm $(DOCKER_IMAGE):$(DOCKER_TAG)

spec-check:
	@echo "Verifying specification alignment..."
	@if [ -f scripts/spec_check.py ]; then \
		python scripts/spec_check.py; \
	else \
		echo "Error: scripts/spec_check.py not found."; \
		exit 1; \
	fi

clean:
	@echo "Cleaning environment..."
	rm -rf .venv
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	docker rmi $(DOCKER_IMAGE):$(DOCKER_TAG) || true
