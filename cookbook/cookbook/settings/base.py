"""
The Django settings that will be shared with all environments under project.
"""
import environ

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env.bool('DJANGO_DEBUG', False)
DATABASES = {
    'default': env.db()
}