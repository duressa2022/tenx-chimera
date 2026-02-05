DOCKER_IMAGE=chimera-test
DOCKER_TAG=latest
DOCKERFILE=infra/Dockerfile

.PHONY: build test shell

build:
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) -f $(DOCKERFILE) ..

test:
	docker run --rm $(DOCKER_IMAGE):$(DOCKER_TAG)

shell:
	docker run --rm -it $(DOCKER_IMAGE):$(DOCKER_TAG) /bin/bash
