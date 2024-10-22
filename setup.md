# VENV
* Tworzymy wirtualne środowisko python -m venv env
* Instalujemy wszystkie potrzebne biblioteki pip install -r requirements.txt
* Aktywacja venv -  .\env\Scripts\activate   
* Deaktywacja venv - deactivate 

# DJANGO
* Utworzenie projektu - django-admin startproject project
* Przechodzimy do utworzonego projektu - cd project
* Utworzenie aplikacji na serwerze - Python manage.py startapp api
* Jeżeli pomyliliśmy się w nazwie aplikacji należy usunąć folder z aplikacją i
skorzystać z komendy -  python manage.py remove_stale_contenttypes --include-stale-apps
* Uruchomienie serwera Django - python GymProject\manage.py runserver 
* Wstępna migracja danych ( wrazie gdyby baza się wysypała) -  python GymProject\manage.py makemigrations app
* Migracja danych (weryfikacja) - python GymProject\manage.py makemigrations 
* Migracja danych (realizacja) - python GymProjectt\manage.py migrate
* Zbieramy pliki statyczne - python GymProject\manage.py collectstatic  
* Utworzenie super użytkownika (przechowujemy w bazie danych Firebase)  - python GymProject\manage.py createsuperuser

* Routing w naszej aplikaji umożliwia nawigowanie między komponentami 
aplikacji bez potrzeby przeładowywania jej.

* views - plik który odpowiada za renderowanie stron, a raczek określa
co dokładnie ma zostać wyrenderowane. 


# Opis struktury przykładowego projektu DJANGO 
myproject/
│
├── manage.py                   # Script for running Django commands
├── myproject/
│   ├── __init__.py              # Makes this directory a Python package
│   ├── asgi.py                  # ASGI config for asynchronous support
│   ├── settings.py              # Project-wide settings
│   ├── urls.py                  # Project-wide URL routing
│   ├── wsgi.py                  # WSGI config for deployment
│   └── settings/
│       ├── __init__.py          # Makes settings a package
│       ├── base.py              # Base settings shared across environments
│       ├── development.py       # Development environment settings
│       └── production.py        # Production environment settings
│
└── myapp/
    ├── __init__.py              # Makes this directory a Python package
    ├── admin.py                 # Admin site configurations
    ├── apps.py                  # App configurations
    ├── models.py                # Database models
    ├── migrations/              # Database migration files
    ├── views/                   # Views package
    │   ├── __init__.py          # Makes views a package
    │   ├── user_views.py        # Views related to user management
    │   └── post_views.py        # Views related to post management
    ├── serializers/             # Serializers package
    │   ├── __init__.py          # Makes serializers a package
    │   ├── user_serializers.py  # Serializers for user models
    │   └── post_serializers.py  # Serializers for post models
    ├── urls.py                  # App-specific URL routing
    ├── permissions.py           # Custom permission classes
    ├── filters.py               # Custom filters
    ├── signals.py               # Signal handlers
    ├── pagination.py            # Custom pagination classes
    ├── tasks.py                 # Celery tasks or background tasks
    ├── tests/
    │   ├── __init__.py          # Makes tests a package
    │   ├── test_views.py        # Unit tests for views
    │   ├── test_models.py       # Unit tests for models
    │   └── test_serializers.py  # Unit tests for serializers
    └── utils/
        ├── __init__.py          # Makes utils a package
        ├── helpers.py           # Helper functions
        └── validators.py        # Custom validators


## Tworzymy konto użytkownika dla naszej bazy danych
CREATE USER 'admin'@'localhost' IDENTIFIED BY '**********';
grant all on sitedb.* to 'admin'@'localhost';

## Objaśnienie poszczególnych plików w Django 
views.py - zwraca odpowiednie widoki
urls.py - odpowiada za mapowanie naszych stron 
models.py - w tym pliku definiujemy nasze pola i zachowania danych które przechowujemy 
admin.py - w tym pliku rejestrujemy nasze modele, aby  były widoczne w panelu administracyjnym 
static -  w tym folderze przechowujemy pliki CSS, JS zdjęcia itp. 
templates - tutaj przechowujemy pliki html, często zawiera się w nich csrf_token (zabezpieczenie przed niekontrolowanym wykonaniem operacji).
