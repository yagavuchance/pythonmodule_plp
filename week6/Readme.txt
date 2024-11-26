README: Bank Churn Data Analysis Project
Project Overview
This project focuses on analyzing customer churn in a banking dataset (Bank_Churn.csv). Using Python, we explore and visualize the data to derive insights such as churn rates, regional churn trends, and demographic distributions. The findings can help understand customer behavior and identify factors influencing churn.

Dataset: Bank_Churn.csv
Description:
The dataset contains information about bank customers, including demographic, financial, and churn-related attributes.

Key Columns:
CustomerId: Unique identifier for each customer.
Surname: Customer's last name.
CreditScore: Credit score of the customer.
Geography: Region of the customer (e.g., France, Germany, Spain).
Gender: Customer's gender.
Age: Customer's age.
Balance: Bank account balance of the customer.
NumOfProducts: Number of products the customer is using.
HasCrCard: Whether the customer has a credit card (1 = Yes, 0 = No).
IsActiveMember: Whether the customer is an active bank member (1 = Yes, 0 = No).
EstimatedSalary: Estimated annual salary of the customer.
Exited: Churn status (1 = Customer has left, 0 = Customer is retained).
Features of the Script

1. Data Exploration
Displays the first five rows of the dataset.
Prints dataset information, such as column names, data types, and non-null counts.
Provides summary statistics (mean, median, standard deviation, etc.).
Checks for missing values in the dataset.

2. Basic Data Analysis
Overall Churn Rate: Calculates the percentage of customers who have churned.
Churn Rate by Geography: Analyzes churn rates for each geographical region.

3. Visualizations
Bar Chart: Churn rates by geography.
Histogram: Distribution of customers by age.
Scatter Plot: Relationship between account balance and customer age.

4. Findings and Observations
Summarizes key insights derived from the analysis, such as:
Regional differences in churn rates.
Demographic trends like age distribution.
Lack of strong correlation between age and balance.
How to Run the Code

Prerequisites:
Install the required Python libraries:

bash

pip install pandas matplotlib

Ensure the dataset Bank_Churn.csv is placed in the path specified in the script. Update the path as needed.

Steps to Execute:
Open the script in a Python IDE or text editor.
Update the file path to Bank_Churn.csv if necessary.

Run the script:

python data_analysis.py

View the printed results in the terminal and visualize the graphs generated.

Expected Output
Terminal Outputs:

First five rows of the dataset.
Dataset information and summary statistics.
Missing value counts.
Churn rate and churn rates by geography.
Visualizations:

A bar chart showing churn rates across regions.
A histogram depicting age distribution.
A scatter plot illustrating the relationship between balance and age.