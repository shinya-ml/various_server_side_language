DB_NAME=todo_app
DB_USER=root
DB_PASSWORD=p@ssw0rd
FLYWAY_CONF?=-url=jdbc:postgresql://db:5432/$(DB_NAME) -user=$(DB_USER) -password=$(DB_PASSWORD)

up:
	docker compose up --build -d

down:
	docker compose down --volumes --remove-orphans

logs:
	docker compose logs -f

flyway/info:
	docker compose run --rm flyway $(FLYWAY_CONF) info
flyway/baseline:
	docker compose run --rm flyway $(FLYWAY_CONF) baseline
flyway/migrate:
	docker compose run --rm flyway $(FLYWAY_CONF) migrate

psql:
	docker compose exec db psql --username=$(DB_USER) --dbname=$(DB_NAME)

postgresql/init:
	docker compose exec db psql --username=$(DB_USER) --command="create database $(DB_NAME)"
__postgresql/drop:
	docker compose exec db psql --username=$(DB_USER) --command="drop database $(DB_NAME)"
