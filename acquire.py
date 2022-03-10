import numpy as np
import pandas as pd
from pydataset import data
import os
import env


def get_telco_data():

    filename = 'telco.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)

    database = 'telco_churn'     
    get_db_url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/'
    query = '''
            SELECT * 
            FROM customers
            JOIN contract_types USING(contract_type_id)
            JOIN internet_service_types USING(internet_service_type_id)
            JOIN payment_types USING(payment_type_id)
            '''
     
    df = pd.read_sql(query, url)
    df.to_csv(filename, index=False)

    return df




