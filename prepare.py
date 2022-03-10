import env
import numpy as np
import pandas as pd
import acquire as aq
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

def prep_telco(df):
    '''
        Function takes in the telco dataset and readies it for use ensuring all
        categories are usable for analysis
    '''
# Drop unnecessary columns that contain dupilicated information    
    df = df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id'])
# Change the Total Changes column to a float    
    df.total_charges = df.total_charges.replace(' ', 0).astype(float)
# Identify columns to be receive dummies   
    cat_columns = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type']
# Create dummies
    for col in cat_columns:
        dummies = pd.get_dummies(df[col],
                                     prefix=df[col].name,
                                     dummy_na=False,
                                     drop_first = True)
        df = pd.concat([df, dummies], axis=1)
        df = df.drop(columns=[col])    
    return df

# Create a TVT split
def train_validate_test_split(df, target, seed=1349):
    '''
    This function takes in a dataframe and splits it into train, validate, and test. 
    Test is first extracted as 20% test, 80% train_validate split.
    Then from the remaining 80%, the train and validate are extracted using a 70/30
    split respectively. The function then returns them in the order of train,
    validate, and test.
    '''   
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test