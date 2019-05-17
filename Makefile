docker-build-prod:
	docker-compose -f compose-prod.yml build

docker-build-dev:
	docker-compose -f compose-dev.yml build

docker-up-background-prod:
	docker-compose -f compose-prod.yml up -d

docker-up-background-dev:
	docker-compose -f compose-dev.yml up -d

docker-up-prod:
	docker-compose -f compose-prod.yml up

docker-up-dev:
	docker-compose -f compose-dev.yml up

ssh-django:
	docker exec -ti django_server bash

ssh-django-makemigrations:
	docker exec -ti django_server python manage.py makemigrations

ssh-psql:
	docker exec -ti postgres_server bash

ssh-nginx:
	docker exec -ti nginx_server bash

django-dev:
	python manage.py runserver --settings=config.settings.local

docker-clean-up:
	docker rm $(docker ps -a -q)
	docker rmi $(docker images -q)
	docker volume rm $(docker volume ls -q)

es-max-mv:
	sudo sysctl -w vm.max_map_count=262144
