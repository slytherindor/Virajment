build:
	docker-compose build

up:
	docker-compose up -d app

test: up
		docker-compose run --rm --no-deps --entrypoint=pytest app /tests/integration /tests/e2e

logs:
	docker-compose logs app | tail -100

down:
	docker-compose down

all: down build up test

db-up: 
	docker-compose -f docker-compose-integration.yaml up

db-down: 
	docker-compose -f docker-compose-integration.yaml down