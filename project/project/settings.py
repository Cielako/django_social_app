"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from dotenv import load_dotenv
from pathlib import Path

# Loads all secrets from our secret file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

print("BASE_DIR is", PROJECT_ROOT)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    'rest_framework.authtoken',  # For sessions tokens
    # if u wish to use apps form subfoldersjust rename variable name
    # in each app u wish to example: name=apps.newapp and use it here
    "core",
    "users",
    "user_panel",

]



MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR,'templates')], #path to templates folder in local system.
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# CUSTOM AUTHENTICATION

# AUTH_USER_MODEL - Lets our project know we changed default auth user model
# AUTHENTICATION_BACKENDS - Changing standard behaviour of authentication
AUTH_USER_MODEL = 'users.CustomUser'
AUTHENTICATION_BACKENDS = [
    'users.backends.UsernameOrEmailBackend',  # Your custom backend
    'django.contrib.auth.backends.ModelBackend',  # Default backend
] # nowy

# CONFIGURATION Django Rest Framework
REST_FRAMEWORK = {
    # Autentykacja - możesz użyć JWT do uwierzytelniania
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT Authentication
        # 'rest_framework.authentication.SessionAuthentication',  # Autentykacja sesji (opcjonalnie)
    ],
    
    # Renderery - możesz zwrócić odpowiedzi w formacie JSON
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],

    # Opcjonalnie - konfiguracja paginacji (jeśli używasz)
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # Liczba elementów na stronę
}

from datetime import timedelta

# Konfiguracja SimpleJWT (JWT)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),  # Czas życia tokenu dostępu (np. 1 godzina)
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),  # Czas życia tokenu odświeżania (np. 7 dni)
    'ROTATE_REFRESH_TOKENS': True,  # Opcja rotacji tokenów odświeżania
    'BLACKLIST_AFTER_ROTATION': True,  # Opcja czarnej listy tokenów po rotacji
}

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "pl"

LOGIN_REDIRECT_URL = 'user_dashboard'

LOGIN_URL = 'login'

LOGOUT_REDIRECT_URL = '/'

SESSION_COOKIE_AGE = 7 * 24 * 60 * 60

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


#STATIC_URL = prefix or URL prepend to your static files
#STATICFILES_DIRS - django will search here for static files
#STATIC_ROOT - folder where static files will be stored after using manage.py
#MEDIA ROOT - folder where files uploaded using FileField will go
STATIC_URL = 'static/'
STATICFILES_DIRS = [ # Here
    BASE_DIR / 'core/static/',
    BASE_DIR / 'users/static',
    BASE_DIR / 'project/static',
    BASE_DIR / 'user_panel/static',
]
#STATICFILES_ROOT = os.path.join(BASE_DIR, "static")
STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"


# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
