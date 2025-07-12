# alx_travel_app/celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_travel_app.settings")

app = Celery("alx_travel_app")

# broker & backend are read from settings via Django’s config
app.config_from_object("django.conf:settings", namespace="CELERY")

# autodiscover tasks.py in all INSTALLED_APPS
app.autodiscover_tasks()
