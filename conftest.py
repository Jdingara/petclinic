import os
os.environ.setdefault('DJANGO_SECRET_KEY', 'test-only-not-for-production')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
