import env
import numpy as np
import pandas as pd
import acquire as aq
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

def prep_telco(telco_df):
    '''
        Function takes in the telco dataset and readies it for use ensuring all
        categories are 
    '''
    telco_df = telco_df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'])
    
    telco_df.total_charges = telco_df.total_charges.replace(' ', 0).astype(float)
    
    cat_columns = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type']

    for col in cat_columns:
        telco_dummy = pd.get_dummies(telco_df[col],
                                     prefix=telco_df[col].name,
                                     dummy_na=False,
                                     drop_first = True)
        telco_df = pd.concat([telco_df, telco_dummy], axis=1)
        telco_df = telco_df.drop(columns=[col])    
    return telco_df 

def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test