from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ReadExcel.settings')

app = Celery('ReadExcel')
app.conf.enable_utc = False

app.conf.update(timezone = 'Africa/Lagos')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-birthday-wishes-48': {
        'task': 'core.periodic_task.some_task',
        'schedule': crontab(hour=0, minute=40,),
        #'args': (2,)
    }
    
}

# Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')