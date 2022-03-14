import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import env
import acquire 

def clean_telco(df):
    '''
        Function takes in the telco dataset and readies it for use ensuring all
        categories are usable for analysis
    '''
    # Drop any dropicate columns
    df.drop_duplicates()
    # Identify unnecessary columns    
#     drop_columns = ['customer_id',
#                     'payment_type_id',
#                     'internet_service_type_id',
#                     'contract_type_id']
    # Drop those unecessary columns listed
    #df = df.drop(columns = drop_columns)
    # Change the total_charges columns to be numeric and set invalids to NaN   
    df.total_charges = pd.to_numeric(df.total_charges, errors = 'coerce')
    # Identify types of dummies for dummy variables
    # Dummies that are easily binary and drop the first of them.
    dummies1 = pd.get_dummies(df[['gender', 'partner', 'dependents',
                                   'online_security', 'online_backup',
                                   'phone_service','device_protection',       
                                   'tech_support', 'streaming_tv',
                                   'streaming_movies', 'paperless_billing', 
                                   'churn']], drop_first = True)
    # Dummies that have multiple outcomes (more than 2)
    dummies2 = pd.get_dummies(df[['multiple_lines', 'contract_type',
                                   'internet_service_type', 'payment_type']])
   # List new duplicate columns
    drop_cols = ['payment_type_id', 'contract_type_id', 
                'gender', 'partner', 'dependents', 'online_security', 'phone_service',
                'online_backup', 'device_protection', 'tech_support', 'streaming_tv',
                'streaming_movies', 'paperless_billing', 'churn']
    # Drop those new duplicates
    df = df.drop(columns = drop_cols)
    # Concatenate orignal df and new dummy columns
    df = pd.concat([df, dummies1, dummies2], axis=1) 
    # Rename columns for better readability
    df.rename(columns ={'gender_Male': 'is_male',
                    'internet_service_type_id': 'internet_type',
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
                    'contract_type_Month-to-month': 'month_to_month',
                    'contract_type_One year': 'one_year',
                    'contract_type_Two year': 'two_year',
                    'internet_service_type_DSL': 'dsl_int',
                    'internet_service_type_Fiber optic': 'fiber_int',
                    'internet_service_type_None': 'no_internet',
                    'payment_type_Bank transfer (automatic)': 'bt_auto',
                    'payment_type_Credit card (automatic)': 'cc_auto',
                    'payment_type_Electronic check': 'elecc_nonauto',
                    'payment_type_Mailed check': 'mailc_nonauto'}, 
          inplace = True)                     
    return df

# Create a TVT split
def split_telco(df):
    '''
    This function takes in the dataframe and splits it into train, validate, and test. 
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

# To make the final product notebook cleaner, the two above function will be combined
# to perform all tasks in one call.
def prep_telco(df):
    '''
    Cleaning and splitting the data using the 2 functions above
    '''
    cleaned =clean_telco(df)
    train, validate, test = split_telco(cleaned)

    return train, validate, test 

