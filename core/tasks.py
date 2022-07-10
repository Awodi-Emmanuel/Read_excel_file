from core.models import Widget
 
from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    for i in range(100):
        print(i)
    return "Done"

@shared_task
def add(x, y):
    return x + y

from celery.utils.log import get_task_logger
from .emails import send_feedback_email

logger = get_task_logger(__name__)

@shared_task(name="Send_feedback-email_task")
def send_feedback_email_task(email, message):
    """send an email when feedback form is filled successfully"""
    logger.info("sent feedback email")
    return send_feedback_email(email, message)

    