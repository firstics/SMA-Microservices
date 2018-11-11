"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")
STATIC_DIR = os.path.join(BASE_DIR,"static")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.fashionisland.co.th'
#192.19.0.90 , mail.fashionisland.co.th
EMAIL_PORT = 25
EMAIL_HOST_USER = 'webconsign@fashionisland.co.th'
EMAIL_HOST_PASSWORD = 'Webc0ns!gn'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '286^ac1aqiki^-mi3y4u^*-vpv8xc$31o1g_c1*s5tf!_+p#td'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

AUTH_USER_MODEL = 'accounts.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crontab',
    'accounts',
    'record',
    'rest_framework',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "tg3database",
#         "USER": "tg3database",
#         "PASSWORD": "tg3:tg3:tg3",
#         "HOST": "tg3database.cjessi7ziwty.ap-southeast-1.rds.amazonaws.com",
#         "PORT": "5432",
#     }

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
         "NAME": "d93a1mai19ljon",
         "USER": "tmlzgdxmunhgfi",
         "PASSWORD": "8e81e59b1b9f4e3d03767ea29ad4b5579295c6a3e80d49dd93ba55c12bfe84e4",
         "HOST": "ec2-54-204-14-96.compute-1.amazonaws.com",
         "PORT": "5432",
    },
    'authen-replica': {
         "ENGINE": "django.db.backends.postgresql_psycopg2",
         "NAME": "dc97q6s1c395au",
         "USER": "qejazfyokqoxby",
         "PASSWORD": "34f4ec30e0ebc82d9066712c7fa56651b28d8c66344d1cea55a299a60c1a5d63",
         "HOST": "ec2-54-83-49-109.compute-1.amazonaws.com",
         "PORT": "5432",
    },
    'service-primary': {
         "ENGINE": "django.db.backends.postgresql_psycopg2",
         "NAME": "d3f9rr1b6h79pv",
         "USER": "kguqgvfdvgvkci",
         "PASSWORD": "d1af93734ca5a6aa16b2b60a697b0fb9fa961902da99ca1e7b272a19efc28c97",
         "HOST": "ec2-23-23-153-145.compute-1.amazonaws.com",
         "PORT": "5432",
    },
    'service-replica-1': {
         "ENGINE": "django.db.backends.postgresql_psycopg2",
         "NAME": "dceou3smaatqgg",
         "USER": "uvhuaggetxwkxl",
         "PASSWORD": "2a745351179030224365e6ffeeee89dc1e074eeef687e7698f5f38d71f6131bc",
         "HOST": "ec2-23-23-153-145.compute-1.amazonaws.com",
         "PORT": "5432",
    },
    'service-replica-2': {
         "ENGINE": "django.db.backends.postgresql_psycopg2",
         "NAME": "dcfr5p6i1sk8bo",
         "USER": "pittocbedfhxel",
         "PASSWORD": "9474ca21fc2881136fb5de083cb395cd5acb6907d6bbe39affcb83758cae32fc",
         "HOST": "ec2-23-23-153-145.compute-1.amazonaws.com",
         "PORT": "5432",
    },
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql_psycopg2",
    #     "NAME": "Skittle",
    #     "HOST": "localhost",
    #     "PORT": "5432",
    # }
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql_psycopg2",
    #     "NAME": "dekfcnkjsj60g",
    #     "USER": "jzcigerblgrzng",
    #     "PASSWORD": "5e43154c9565575727b3d831d7d90ed7effdc66d50545ac7d2a0ae0fdb7ece62",
    #     "HOST": "ec2-54-225-103-167.compute-1.amazonaws.com",
    #     "PORT": "5432",
    # }
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql_psycopg2",
    #     "NAME": "consigdb",
    #     "USER": "consigadmin",
    #     "PASSWORD": "c0n$!gnp@$$w0rd",
    #     "HOST": "localhost",
    #     "PORT": "",
    # }
}

#DATABASE_ROUTERS = ['accounts.routers.AuthRouter', 'accounts.routers.ServiceRouter']

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },    
]

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.TokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     )
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# CRON_CLASSES = [
#     "record.cron.RecordScheduler",
# ]

CRONJOBS = [
    ('0 1 * * *', 'record.cron.myScheduler')
]
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bangkok'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    STATIC_DIR,
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'