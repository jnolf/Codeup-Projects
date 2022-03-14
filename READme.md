Classification Project - Telco Churn 
Codeup - Innis Cohort - March 2022  
----
## PROJECT OVERVIEW  
----  
### 1.  Goals:
The goal of this project is to identify key drivers of churn for Telco, a telecommunications company, and make recommendations to reduce churn in order to increase customer retention, and ultimately increase revenue. Churn is another term for attrition. It represents customers leaving and turning away from Telco services. Once drivers are identified, machine learning and statistical analysis will provide a measure for predicting future churn in order to effectively use Company tools to increase attrition.  In the end, the following deliverables will be available:

- This README file - provides an overview of the project and steps for project reproduction.  
- Draft Jupyter Notebook - provides all steps taken to produce the project.
- Python Module File - provides code that will allow for reproducibility.
- acquire.py - used to acquire data
- prepare.py - used to prepare data
- Report Jupyter Notebook - provides final presentation-ready assessment and recommendations. 
- .csv File - provides primary data used to make predictions & recommendations.  
----  
### 2. DESCRIPTION:

This project will start with data acquisition. From that point, it will move into cleaning and wrangling the data. Exploration will follow in order to look into possible drivers of churn along with models to predict churn based on present Telco data. Once insights are found and presented, a final report will be created that includes all code that allows for reproducibility along with a .csv file that predicts probability of churn for customer ids based on the most accurate model.    
----  
#### INITIAL QUESTIONS: 

- Do month-to-month customers really churn at a higher rate than all others?
- In what year do most customers churn?
- Do customers that churn pay more than other customers?
- Is churn independent of internet service type?  
—---  
## DATA DICTIONARY:

The final DataFrame used to explore the data for this project contains the following variables (columns).  The variables, along with their data types, are defined below:  


|  Variables             |    Data Type                                |    Definition             |
| :--------------------:   | :----------------------------------------: | :--------------------: |
customer_id           |               object             | unique identifier for each customer |  
is_senior                |                 integer (whole number)	|  senior citizen (65+), 0= no, 1=yes| 
tenure_months       |                      integer (whole number)	| length of customer service in months|
monthly_charges     |                    float (decimal)	| current monthly charges in USD |
total_charges            |               float (decimal)	| sum of all charges for tenure in USD |
contract_type             |               object	| type of contract customer signed: month-to-month, One year, Two year|
internet_service_type |               object	| type of internet service customer has or had: Fiber optic, DSL, None|	
payment_type |   object	| type of payment method customer uses or used: Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic) |
is_male_Male         |   integer ( boolean 0,1)	| binary gender identity 0= male, 1=female|  	
has_partner_Yes    |                       integer ( boolean 0,1)	| has spouse, partner, or significant other, 0= no, 1=yes||
has_dependents_Yes     |  integer ( boolean 0,1)	| has dependent(s), children or otherwise, 0= no, 1=yes|
has_phone_service_Yes |                    integer ( boolean 0,1)	| is or was a phone customer, 0= no, 1=yes|
has_multiple_lines_No phone service |      integer ( boolean 0,1)	| didn’t or doesn’t have phone service, 0= no, 1=yes|
has_multiple_lines_Yes   |                 integer ( boolean 0,1)	| has or had multiple phone lines, 0= no, 1=yes|
has_online_security_Yes   |  integer ( boolean 0,1)| internet option: has or had service add-on, 0= no, 1=yes|
has_online_backup_Yes  | integer ( boolean 0,1) | internet option: has or had service add-onr, 0= no, 1=yes|
has_device_protection_Yes  |  integer ( boolean 0,1)|  internet option: has or had service add-on, 0= no, 1=yes|
has_tech_support_Yes  |               integer ( boolean 0,1)	| internet option: has or had service add-on, 0= no, 1=yes|
has_streaming_tv_Yes   |          integer ( boolean 0,1)	| internet option: has or had service add-on, 0= no, 1=yes|
has_streaming_movies_Yes  |       integer ( boolean 0,1)	| internet option: has or had service add-on, 0= no, 1=yes|
has_paperless_billing_Yes |    integer ( boolean 0,1)|  customer bill is or was paperless, 0= no, 1=yes |
did_churn_Yes (target) |            integer ( boolean 0,1)	| customer services have been cancelled, 0= no, 1=yes|   
contract_type_One year  |                  integer ( boolean 0,1|  customer has or did have 1 year contract, 0= no, 1=yes|
contract_type_Two year  |                  integer ( boolean 0,1) | customer has or did have 2 year contract, 0= no, 1=yes|	
internet_service_type_Fiber optic  | integer ( boolean 0,1)|  is or was a fiber optic internet customer,  0= no, 1=yes |
internet_service_type_None     | integer ( boolean 0,1)| s or was an internet customer,  0= no, 1=yes |
payment_type_Credit card (automatic)   |   integer ( boolean 0,1)	| payment type is or was credit card, 0= no, 1=yes |	
payment_type_Electronic check     |        integer ( boolean 0,1)	| payment type is or was electronic check, 0= no, 1=yes |	
payment_type_Mailed check       |          integer ( boolean 0,1)	| payment type is or was check via post, 0= no, 1=yes |	
—---
## PROCESS:
The following outlines the process taken through the Data Science Pipeline to complete this project.  

Plan ➜ Acquire ➜ Prepare ➜ Explore ➜ Model & Evaluate ➜ Deliver

### 1. PLAN
- Define the project goal
- Determine proper format for the audience
- Asked questions that would lead to final goal


### 2. ACQUIRE
- Create a function to pull appropriate information from the telco_churn_db
- Create and save an acquire.py file and made it available to import

### 3. PREPARE
- Create a function that will do the following
- Remove any duplicate data that in repetitive
- Ensure all data types are usable
- Use encoding to ensure categories are usable for machine learning
- Rename columns to improve readability
- Add a function that splits the acquired data into Train, Validate, and Test sets
- 20% is originally pulled out in order to test in the end
- From the remaining 80%, 30% is pullout out to validate training
- The remaining data is used as testing data
- In the end, there should be a 56% Train, 24% Validate, and 20% Test split 
- Create a prepare.py file with all the functions in this section


### 4.EXPLORE
- Create an exploratory workbook
- Use the initial questions to help explore the data
- Make visualizations to help with understanding drivers
- Use stats testing on established hypotheses

### 5. MODEL & EVALUATE
- Use models to evaluate true drivers of churn
- Make predictions of models and what they say about the data
- Compare all models to evaluate the best for use

### 6. DELIVERY
- Present a final Jupyter Notebook
- Make available modules used and project files on Github  
—---  
## REPRODUCIBILITY: 
	
### Steps to Reproduce

1. Have your env file with proper credentials saved to the working directory

2. Ensure that a .gitignore is properly made in order to keep privileged information private

3. Clone repo from github to ensure availability of the acquire and prepare imports

4. Ensure pandas, numpy, matplotlib, scipy, sklearn, and seaborn are available

5. Follow steps outline in this README.md to run Telco - Final Report.ipynb  
—---  
## KEY TAKEAWAYS:

### Conclusions
- Churning customers are paying higher monthly charges versus other non-churning customers.
- Most customer churn happens within the first year of tenure.
- Internet service type is related to customer churn.
- Month-to-month customers churn at a much higher rate versus other contract types.
### Recommendations
- Create a marketing program that directly influences these categories
- Decrease the price increase on month-to-month contracts in order to influence attrition positively.
- Offer incentivization programs that place customers into longer term contracts.
- Look for ways to bring savings to Fiber customers in order to keep them aboard.
### Next Steps
In the future we will be able to use this model in order to predict with 80% accuracy whether or not a customer will churn. Knowing this information will allow us to better focus resources and marketing campaigns in order to reduce customer churn in the future and better effect our bottom line.
A further dive into the data with more time allowed will help in improving the accuracy of our model by identifying more conclusive and impactful drivers.  
—---  



