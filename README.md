# django_social_app
Social app project in Python language using Django REST framework
## Table of Contents
- [Description](#description)
- [Technology](#technology)

## Description
- Create social app from scratch, app will be a playground to learn new things, and test current knowledge. 

## Technology
:small_orange_diamond: Language: Python 3.12.7 [:arrow_forward:](https://www.python.org/downloads/windows/) </br>
:small_orange_diamond: Database: PostgreSQL 17.0 [:arrow_forward:](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) </br>
:small_orange_diamond: Backend: Django 5.1.2 [:arrow_forward:](https://docs.djangoproject.com/en/5.1/releases/5.1.2/) </br>
:small_orange_diamond: API: django REST framework 3.15.2 [:arrow_forward:](https://www.django-rest-framework.org) </br>

## Project structure 
```
project/
│
├── project         # Project-level settings and configuration
├── apps            # Contains all apps used in project 
│   ├── core        # App will contain core features
│   ├── users       # App will contain all user features
├── static          # contains subfolders with styles of templates
```
to set static in project just write inside settings.py this line:
```STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]``` 


