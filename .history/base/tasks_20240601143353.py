from celery import shared_task
from .seed import register_user_to_send_mail
@shared_task(bind=True)
def fun1(self,email,fullname):
    register_user_to_send_mail([email],fullname).dea
    return "DONE"