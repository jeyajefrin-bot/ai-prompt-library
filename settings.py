INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'prompts',
]

</>Bash
pip install django psycopg2-binary redis
django-admin startproject prompt_library
cd prompt_library
python manage.py startapp prompts