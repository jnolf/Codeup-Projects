import numpy as np
import pandas as pd
import os
from env import username, password, host

def get_telco_data(use_cache=True):
    '''This function returns the data from the telco_churn database in Codeup Data Science Database. 
    In my SQL query I have joined all 4 tables together, so that the resulting dataframe contains all the contract, 
    payment, and internet service options.
    '''
    if os.path.exists('telco.csv') and use_cache:
        print('Using cached csv')
        return pd.read_csv('telco.csv')
    print('Acquiring data from SQL database')

    database_url_base = f'mysql+pymysql://{username}:{password}@{host}/'
    query = '''
    SELECT *
    FROM customers
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN contract_types USING (contract_type_id)
    JOIN payment_types USING (payment_type_id)
    '''
    df = pd.read_sql(query, database_url_base + 'telco_churn')
    df.to_csv('telco.csv', index=False)
    return df

get_telco_data()




