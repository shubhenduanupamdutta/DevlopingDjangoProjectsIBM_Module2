# Django App Development - Module 2

## IBM Full Stack Developer Professional Certificate - Member Course

Building Full-Stack Web Applications with Django

---

## Building A Django Project

### Setup a Project with UV

```bash
uv init -p 3.11.13
uv sync
```

### Scaffold Django Project

- **Following Django specific code works with Django 5.2.5**

```bash
uv add Django
django-admin startproject myproject
```

## Scaffolding an App inside the project

```bash
cd myfirstproject
python manage.py startapp myapp
```

## Setup Database

In **myfirstproject** I am going with default option of sqlite3

```bash
python manage.py makemigrations
python manage.py migrate
```

## Deploying via Docker

Create a `.env` file in the root of your project with the following content:
Secret key can be generated using the following command:

```bash
python -c 'import secrets; print(secrets.token_hex(32))'
```

```bash
SECRET_KEY=<secretkey>
PYTHONUNBUFFERED=1
```

```bash
docker build . -t my-django-app:latest
docker run --env-file .env -p  8000:8000 my-django-app
```

- To stop the running container

```bash
docker ps
docker stop <container_id>
```

## Deploying via Docker on IBM Theia

### Install pipreqs

```bash
pip install pipreqs
pipreqs .
```

### Create Dockerfile

In root of the project i.e. `myfirstproject`

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Build and Run

```bash
docker build . -t my-django-app:latest && docker run -e PYTHONUNBUFFERED=1 -p  8000:8000 my-django-app
```

### Code Engine

```bash
APP_NAME=my-django-app
REGISTRY=us.icr.io
docker tag ${APP_NAME}:latest ${REGISTRY}/${SN_ICR_NAMESPACE}/${APP_NAME}:latest
docker push ${REGISTRY}/${SN_ICR_NAMESPACE}/${APP_NAME}:latest
```

Finally Deploy

```bash
ibmcloud ce application create --name ${APP_NAME} --image ${REGISTRY}/${SN_ICR_NAMESPACE}/${APP_NAME}:latest --registry-secret icr-secret --port 8000
```

### Check logs and events

```bash
ibmcloud ce app logs --application ${APP_NAME}
ibmcloud ce app events --application ${APP_NAME}
```
