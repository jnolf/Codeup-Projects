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
    df = df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'])
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
        df.rename(columns ={ 'gender_Male': 'is_male',
                     'partner_Yes': 'has_partner',
                     'dependents_Yes': 'has_dependents',
                     'online_security_Yes': 'online_security',
                     'online_backup_Yes': 'online_backup',
                     'phone_service_Yes': 'phone_service',
                     'device_protection_Yes': 'device_protection',
                     'tech_support_Yes': 'tech_support',
                     'streaming_tv_Yes': 'streaming_tv',
                     'streaming_movies_Yes': 'streaming_movies',
                     'paperless_billing_Yes': 'paperless_billing',
                     'churn_Yes': 'churn',
                     'multiple_lines_No': 'one_line',
                     'multiple_lines_No phone service': 'no_phone_service',
                     'multiple_lines_Yes': 'has_multiple_lines',
                     'contract_type_Month-to-month': 'month_to_month_contract',
                     'contract_type_One year': 'one_year_contract',
                     'contract_type_Two year': 'two_year_contract',
                     'internet_service_type_DSL': 'has_dsl',
                     'internet_service_type_Fiber optic': 'has_fiber_optic',
                     'internet_service_type_None': 'no_internet',
                     'payment_type_Bank transfer (automatic)':'bank_transfer_auto',
                     'payment_type_Credit card (automatic)': 'credit_card_auto',
                     'payment_type_Electronic check': 'electronic_check_nonauto',
                     'payment_type_Mailed check': 'mailed_check_nonauto'},
                  inplace=True)                     
    return df

# Create a TVT split
def split_data(df):
    '''
    This function takes in a dataframe and splits it into train, validate, and test. 
    Test is first extracted as 20% test, 80% train_validate split.
    Then from the 80%, the train and validate are extracted using a 70/30
    split respectively. The function then returns them in the order of train,
    validate, and test.
    '''   
    train_validate, test = train_test_split(df, test_size=.2, 
                                            random_state=123, 
                                            stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.churn)
    return train, validate, test