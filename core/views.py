from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func, add
# from celery import  
# from .read_excel import cele_test


import pandas as pd 
from celery import shared_task

def test(request):
    # cele_test.delay()
    add.delay(7,8)
    
    return HttpResponse("Done")