from stringprep import in_table_a1
import pandas as pd 
from celery import shared_task

@shared_task
def my_celery(request):
    
    f = pd.read_excel(r'store/account_details.xlsx',  usecols=['Numbers'])
    add_money = 50

    for num in f.values:
        f.delay()
        print(num[0], '=', add_money)
    
    return "Done" 

                