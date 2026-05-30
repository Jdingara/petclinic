import django
from django.conf import settings


def pytest_configure(config):
    settings.DJANGO_SETTINGS_MODULE = "config.settings"
