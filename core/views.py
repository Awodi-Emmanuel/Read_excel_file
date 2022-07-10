from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func, add
# from celery import  
# from .read_excel import cele_test
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
from celery import shared_task

def test(request):
    # cele_test.delay()
    add.delay(7,8)
    
    return HttpResponse("Done")