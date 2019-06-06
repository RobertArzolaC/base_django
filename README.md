# Example Project for a Dockerized Django REST, Gunicorn and Nginx in Development

This is a small contribution for the community in order to facilitate the development of applications.

This is an example of a project that uses the following technologies:
+ Django REST APIs
+ Docker with Docker Compose


## System Requirements

+ [Git](https://git-scm.com/)
+ [Docker](https://www.docker.com/)
+ [PostgreSQL](http://www.postgresql.org/)
+ [Docker Compose](https://docs.docker.com/compose/)


## Setup Local Environment
### First things, first. Clone the repo

```
git clone https://github.com/RobertArzolaC/base_django.git
```


### To setup a Dockerized development environment

In my opinion, this is the easiest way to get up and running.


#### 1. Create `.env` file

[Example .env file](https://docs.google.com/document/d/1tdUjDeGbmv6caLwLjt6ctVBVBOO-ZcTnEsHvMWM_rz0/edit?usp=sharing)


#### 2. Build docker container

```
make docker-build-dev
make docker-up-dev
```

Visit [http://localhost/admin](http://localhost/admin). You should see admin django ;)


## Languages used
+ [Python](https://www.python.org/)


## Tools used
+ [Nginx](https://www.nginx.com/)
+ [Gunicorn](https://gunicorn.org/)
+ [Docker 1.12.1](https://www.docker.com/)
+ [Django 2.1.7](https://www.djangoproject.com/)
+ [PostgreSQL 9.6.0](http://www.postgresql.org/)
+ [Docker compose 1.8.0](https://docs.docker.com/compose/)
+ [Django REST Framework 3.9.1](http://www.django-rest-framework.org/)


## Helpful resources
+ [Django Development with Docker Compose and Machine](https://realpython.com/django-development-with-docker-compose-and-machine/)
+ [Dockerizing Django projects](http://ruddra.com/2016/08/14/docker-django-nginx-postgres/)
+ [Extension of Owais Lane's blog post](http://geezhawk.github.io/using-react-with-django-rest-framework)
+ [YouTube Playlist on Django Rest Framework](https://www.youtube.com/playlist?list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS)
+ [JSON Web Tokens With Django REST Framework](https://www.youtube.com/watch?v=Fhcn2qx-4VQ)
+ [Full Stack Python](http://www.fullstackpython.com/)
+ [Write your first Django App](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)
+ [Quick Django tutorial](http://drksephy.github.io/2015/07/16/django/)
+ [Django REST framework](http://www.django-rest-framework.org/tutorial/1-serialization/)


## Authors

* **Robert Arzola Castillo** - *Initial work*


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
