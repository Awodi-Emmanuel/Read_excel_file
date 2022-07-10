from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func, add
from core.periodic_task import some_task
# from celery import  
from .read_excel import cele_test
from django.views.generic.edit import FormView
from core.forms import FeedbackForm

class FeedbackView(FormView):
    template_name = 'feedback/contact.html'
    form_class = FeedbackForm
    success_url = '/'
    
    def form_valid(self, form):
        form.send_email()
        return super(FeedbackView, self).form_invalid(form)


import pandas as pd 


def test(request):
    # acct = pd.read_excel(r'/var/www/html/emmy/Read_excel_file/core/store/account_details.xlsx',  usecols=['Numbers'])
    # cele_test().delay(acct)
    # add().delay(7,8)
    some_task.delay()    
    return HttpResponse("Done")