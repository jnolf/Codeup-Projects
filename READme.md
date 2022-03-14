Classification Project - Telco Churn 
Codeup - Innis Cohort - March 2022

===

## I. PROJECT OVERVIEW

### 1.  Goal:
The goal of this project is to identify key drivers of churn for Telco Communications. Reducing churn means increasing attrition of customers which will, in turn, lead to increases in future revenue. Using machine learning and statistical analysis, predictions of future churn will also be identified with recommendations to follow for prevention will be made in order to improve customer retention.

### 2. DESCRIPTION:

With an ever-competitive telecommunications market, it is vital to understand your customer base in order to prevent customer churn and maximize retention.  It is far less expensive to keep an existing customer than it is to acquire a new one for the long term when marketing costs are included. Therefore, it is important to identify drivers of churn in an effort to prevent attrition. Thus, retaining current customers for the long term.  Ultimately, customer retention is important for maintaining and increasing profit.  This project will identify key drivers of churn for the Telco dataset and use modeling and statistics to identify ways to prevent churn in the future. Ultimately it will provide a recommendation that could be used by Telco or other customer-based service companies to maximize retention. 

#### INITIAL QUESTIONS: 

Do month-to-month customers really churn at a higher rate than all others?
In what year do most customers churn?
Do customers that churn pay more than other customers?
Is churn independent of internet service type?

### 3. DELIVERABLES:
README file - provides an overview of the project and steps for project reproduction.  
Draft Jupyter Notebook - provides all steps taken to produce the project.
Python Module File - provides reproducible code for acquiring,  preparing, exploring, & testing the data.
acquire.py - used to acquire data
prepare.py - used to prepare data
Report Jupyter Notebook - provides final presentation-ready assessment and recommendations. 
.csv File - provides primary data used to make predictions & recommendations. 


## II. DATA CONTEXT

## DATA DICTIONARY:

The final DataFrame used to explore the data for this project contains the following variables (columns).  The values of the Features, as well as their data types, are defined below: 

|  Variables             |  Definition                                |  
| :--------------------:   | :----------------------------------------: |
|  churn           |  customer has left and canceled services     |
|  customer_id        |  unique identifier for each customer       |
|  is_senior             |  qualifies as senior citizen (65+)         |
|  tenure *              |  length of customer service in months      |
|  multiple_lines        |  customer has multiple phone lines           |
|  monthly_charges *     |  current monthly charges in USD            |
|  total_charges         |  sum of all charges for tenure in USD      |
|  internet_service_type  | describes the type of internet service      |
|  is_male               |  binary gender identity is male          |
|  has_partner           |  has spouse, partner, or significant other |
|  has_dependent         |  has dependent(s), children or otherwise   |
|  no_phone_service     |  customer with no phone service             |
|  one_line              |  customer with one phone line                 |
|  no_internet          |  customer with  no internet service            |
|  dsl_int                  |  uses Telco dsl internet service         | 
|  fiber_int              |  uses Telco fiber optic internet service         |
|  streaming_tv          |  internet option: has  service add-on    |
|  streaming_movies      |  internet option: has service add-on   |
|  online_security       |  internet option: has service add-on    |
|  online_backup         |  internet option: has service add-on   |
|  device_protection     |  internet option: has service add-on   |
|  tech_support          |  internet option: has service add-on   |
|  mailed_check          |  payment type is mailed check non autopay     |
|  elecc_nonauto    |  payment type is electronic check/non autopay   |
|  bt_auto         |  payment type is bank transfer/autopay      |
|  cc_auto           |  payment type is credit card/autopay       |
|  paperless_billing     |  customer billing option is paperless         |
|  month_to_month          |  customer’s contract renewal is monthly  |
|  one_year          |  customer’s contract renewal is annually    |
|  two_year          |  customer’s contract renewal is biannually   |


## III. PROCESS:

This project resulted from following the Data Science Pipeline using the following steps:  

Plan➜ Acquire ➜ Prepare ➜ Explore ➜ Model & Evaluate ➜ Deliver

#### 1. Planning
Define the project goal
Determine proper format for the audience
Asked questions that would lead to final goal

#### 2. Acquisition
Create a function to pull appropriate information from the telco_churn_db
Create and save an acquire.py file and made it available to import

#### 3. Preparation
Create a function that will do the following
Remove any duplicate data that in repetitive
Ensure all data types are usable
Use encoding to ensure categories are usable for machine learning
Rename columns to improve readability
Add a function that splits the acquired data into Train, Validate, and Test sets
20% is originally pulled out in order to test in the end
From the remaining 80%, 30% is pullout out to validate training
The remaining data is used as testing data
In the end, there should be a 56% Train, 24% Validate, and 20% Test split 
Create a prepare.py file with all the functions in this section

#### 4. Exploration
Create an exploratory workbook
Use the initial questions to help explore the data
Make visualizations to help with understanding drivers
Use stats testing on established hypotheses

#### 5. Modeling & Evaluation
Use models to evaluate true drivers of churn
Make predictions of models and what they say about the data
Compare all models to evaluate the best for use

#### 6. Deliver
Present a final Jupyter Notebook
Make available modules used and project files on Github


## IV. REPRODUCIBILITY: 
	
### Steps to Reproduce

1.) Have your env file with proper credentials saved to the working directory

2.) Ensure that a .gitignore is properly made in order to keep privileged information private

3.) Clone repo from github to ensure availability of the acquire and prepare imports

4.) Ensure pandas, numpy, matplotlib, scipy, sklearn, and seaborn are available

5.) Follow steps outline in this README.md to run Telco - Final Report.ipynb

## V. Key Findings and Takeaways

Churning customers are paying higher monthly charges versus other non-churning customers.
Most customer churn happens within the first year of tenure.
Internet service type is related to customer churn.
Month-to-month customers churn at a much higher rate versus other contract types.



