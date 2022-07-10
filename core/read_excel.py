from django.http import HttpResponse
from django.shortcuts import render
# from core.tasks import test_func
# from celery import shared_task

import pandas as pd 
from celery import shared_task
# import os



# def my_celery():
#     test_func.delay()
#     f = pd.read_excel(r'store/account_details.xlsx',  usecols=['Numbers'])
#     print(f)
#     add_money = 50

#     for num in f.values:
#         print(num[0], '=', add_money)
@shared_task(bind=True)
def cele_test(n):
    add_money = 50
    for num in n.values:
        print(num[0], add_money)

# accounts = pd.read_excel(r'/var/www/html/emmy/Read_excel_file/core/store/account_details.xlsx',  usecols=['Numbers'])
# cele_test(accounts)
# cele_test(n = pd.read_excel(r'/var/www/html/emmy/Read_excel_file/core/store/account_details.xlsx',  usecols=['Numbers']))
