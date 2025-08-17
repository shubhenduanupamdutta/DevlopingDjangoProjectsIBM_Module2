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
