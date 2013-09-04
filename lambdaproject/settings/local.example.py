from base import *
# Domain your instance should use, for example: 'http://example.com' (no / behind the path)
DOMAIN = 'http://localhost:8000'

# Domain of your website, for example: 'http://example.com' (no / behind the path)
WEBSITE_URL = 'http://localhost'

AUTHOR_NAME = 'Author Name'

CONTACT_EMAIL = 'root@example.com'

# Django settings for lambdaproject.project
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# If you use an virtualenv (you schould) enter it here
VIRTUALENV = ABSOLUTE_PATH + '/.venv/lib/python2-6/sites-packages'
# VIRTUALENV = ABSOLUTE_PATH + '/.venv/lib/python2.7/site-packages'

# The guys who will get an email if something is wrong
ADMINS = (
    ('admin', 'root@localhost'),
)

# Your database settings, sqlite is good for development and testing, not for deployment
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'lambda.sql',            # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de-de'

