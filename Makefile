#!/usr/bin/make



hello:
	echo "Hello, World"
run:
	python3 manage.py runserver
migrations:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
createsuperuser:
	python3 manage.py createsuperuser
lint:
	./bin/lint
test:
	python3 manage.py test
