"""
Django settings for benefits project.
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() == "true"

ADMIN = os.environ.get("DJANGO_ADMIN", "False").lower() == "true"

ALLOWED_HOSTS = []

if DEBUG:
    ALLOWED_HOSTS.extend([
        'localhost',
        '127.0.0.1',
        '[::1]'
    ])

# Application definition

INSTALLED_APPS = [
    "django.contrib.sessions",
    "django.contrib.staticfiles",

    "benefits.core",
    "benefits.discounts",
    "benefits.eligibility"
]

if ADMIN:
    INSTALLED_APPS.extend([
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.messages",
    ])

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    "benefits.core.middleware.DebugSession"
]

if ADMIN:
    MIDDLEWARE.extend([
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ])

ROOT_URLCONF = "benefits.urls"

template_ctx_processors = [
    "django.template.context_processors.request",
]

if DEBUG:
    template_ctx_processors.extend([
        "django.template.context_processors.debug",
        "benefits.core.context_processors.debug",
    ])

if ADMIN:
    template_ctx_processors.extend([
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ])

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "benefits", "templates")
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": template_ctx_processors,
        },
    },
]

WSGI_APPLICATION = "benefits.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ["DJANGO_DB"] + ".db",
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = []

if ADMIN:
    AUTH_PASSWORD_VALIDATORS.extend([
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
    ])

# Internationalization

LANGUAGE_CODE = "en"

LANGUAGES = [
  ("en", "English"),
  ("es", "Español")
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "benefits", "locale")
]

USE_I18N = True
USE_L10N = True

TIME_ZONE = "UTC"
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "benefits", "static")
]
STATIC_ROOT = "/var/www/static/"
