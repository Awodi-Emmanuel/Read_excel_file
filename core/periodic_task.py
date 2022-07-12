from celery.schedules import crontab
# from celery import periodic_task
from celery import shared_task

# @periodic_task(run_every=(crontab(minute='/5')), name="some_task", ignore_result=True)
@shared_task(bind=True)
def some_task(what):
    print("Happy birthday!")
    