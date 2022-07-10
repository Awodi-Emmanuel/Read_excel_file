from celery.schedules import crontab
from celery import periodic_task

@periodic_task(run_every=(crontab(minute='/5')), name="some_task", ignore_result=True)
def some_task():
    print("Running periodic task!")