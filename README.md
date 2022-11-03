# Django/PostgreSQL Base Project with Docker Compose

This repository contains Base Django/PostgreSQL project with Docker Compose.

# Quickstart Docker Setup
Before starting, install Docker Compose.
https://docs.docker.com/compose/install/

Docker Compose to set up and run a simple Django/PostgreSQL app.
https://docs.docker.com/samples/django/

# Usage

Run services in the background:
`docker-compose up -d`

Run services in the foreground:
`docker-compose up --build`

Inspect volume:
`docker volume ls`
and
`docker volume inspect <volume name>`

Prune unused volumes:
`docker volume prune`

View networks:
`docker network ls`

Bring services down:
`docker-compose down`

Open a bash session in a running container:
`docker exec -it <container ID> /bin/bash`

# Django Commands
*Note first start Docker on your system*

1. Create Project
`docker-compose run web django-admin startproject`

2. Create app
`docker-compose run web django-admin startapp appname`