# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r'C:\Users\stevo\Downloads\pythonmodule\week6\Bank_Churn.csv')  # Provide the full path
print(data.head())


# Step 1: Data Exploration
print("First 5 rows of the dataset:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nSummary Statistics:")
print(data.describe())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Step 2: Basic Data Analysis
# Calculate churn rate
churn_rate = data['Exited'].mean() * 100
print(f"\nChurn Rate: {churn_rate:.2f}%")

# Group by geography and calculate churn rate
geo_churn = data.groupby('Geography')['Exited'].mean() * 100
print("\nChurn Rate by Geography:")
print(geo_churn)

# Step 3: Visualizations
# Churn Rate by Geography (Bar Chart)
geo_churn.plot(kind='bar', color='skyblue', title='Churn Rate by Geography')
plt.ylabel('Churn Rate (%)')
plt.show()

# Age Distribution (Histogram)
data['Age'].plot(kind='hist', bins=20, color='orange', title='Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Balance vs. Age (Scatter Plot)
plt.scatter(data['Age'], data['Balance'], alpha=0.5, color='green')
plt.title('Balance vs. Age')
plt.xlabel('Age')
plt.ylabel('Balance')
plt.show()

# Step 4: Findings and Observations
print("\nFindings:")
print("- The churn rate is relatively low but varies significantly across regions.")
print("- Age distribution shows most customers are in the middle-age range.")
print("- No clear trend observed between balance and age in the scatter plot.")

