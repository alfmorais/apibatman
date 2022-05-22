build:
	@docker-compose build

build:
	@docker-compose build --no-cache

tests:
	@echo "--> Testing on Docker."
	docker-compose run api pytest -s --cov-report term --cov-report html

run:
	@docker-compose up

makemigrations:
	@docker-compose run api batman/manage.py makemigrations

migrate:
	@docker-compose run api batman/manage.py migrate

install-requirements:
	@pip install -r requirements.txt

compile-requirements:
	@rm -rf requirements.txt
	@pip-compile requirements.in
