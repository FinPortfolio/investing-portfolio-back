.PHONY: tests

db-up:
	docker compose -f infra/dev/docker-compose.dev.yaml up -d --build pg

db-down:
	docker compose -f infra/dev/docker-compose.dev.yaml down

dev-up:
	docker compose -f infra/dev/docker-compose.dev.yaml up -d --build

dev-down:
	docker compose -f infra/dev/docker-compose.dev.yaml down

tests:
	docker compose -f infra/test/docker-compose.test.yaml up --build --abort-on-container-exit --exit-code-from backend_test
