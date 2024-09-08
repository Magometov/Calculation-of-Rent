"""Celery config"""

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings")
app = Celery("src")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_connection_retry_on_startup = True

app.conf.timezone = "Europe/Moscow"

app.conf.imports = [
    "src.apps.tasks.tasks.public_utilities.calculating_utilities",
]

app.conf.beat_schedule = {
    "test_celery_task": {
        "task": "test_celery_task",
        "schedule": crontab(hour=16, minute=25),
        "options": {
            "queue": "periodic",
        },
    },
}
