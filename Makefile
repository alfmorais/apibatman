build:
	@docker-compose build

build:
	@docker-compose build --no-cache

test:
	@docker-compose run api pytest -s

run:
	@docker-compose run api

makemigrations:
	@docker-compose run api batman/manage.py makemigrations

migrate:
	@docker-compose run api batman/manage.py migrate

install-requirements:
	@pip install -r requirements.txt

compile-requirements:
	@rm -rf requirements.txt
	@pip-compile requirements.in
