build:
	@sudo docker compose build

build-no-cache:
	@sudo docker compose build --no-cache

run:
	@sudo docker compose up

tests:
	@sudo docker compose run --rm batmanapi sh -c "python manage.py test --verbosity 2 --force-color"

migrate:
	@sudo docker compose run --rm batmanapi sh -c "python manage.py migrate"

create-migrate:
	@sudo docker compose run --rm batmanapi sh -c "python manage.py makemigrations"

create-superuser:
	@sudo docker compose run --rm batmanapi sh -c "python manage.py createsuperuser"

install-requirements:
	@pip install -r requirements.txt
	@pip install -r requirements-dev.txt
