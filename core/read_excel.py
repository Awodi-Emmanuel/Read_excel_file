from stringprep import in_table_a1
import pandas as pd 

f = pd.read_excel(r'store/account_details.xlsx',  usecols=['Numbers'])
add_money = 50

for num in f.values:
    print(num[0], '=', add_money)
            