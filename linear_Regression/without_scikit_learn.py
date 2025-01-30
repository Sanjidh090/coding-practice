import numpy as np
import pandas as pd

# Load dataset
data = pd.read_csv(r"C:\Users\sanji\Downloads\Salary_dataset.csv")
data = data.drop('Unnamed: 0', axis=1)

# Prepare data
y = data['Salary']
X = data['YearsExperience']

# Compute parameters manually
n = len(X)
sum_X = X.sum()
sum_y = y.sum()
sum_Xy = (X * y).sum()
sum_X_squared = (X ** 2).sum()

# Compute Slope (m) and Intercept (c)
m = (n * sum_Xy - sum_X * sum_y) / (n * sum_X_squared - sum_X ** 2)
c = (sum_y - m * sum_X) / n

# Display the equation
print(f"Equation: Salary = {m:.2f} * Experience + {c:.2f}")

# Predict salary for 10 years of experience
experience = 10
predicted_salary = m * experience + c
print(f"Predicted Salary for 10 Years Experience: ${predicted_salary:,.2f}")

# Save predictions
data['Predicted_Salary'] = m * data['YearsExperience'] + c
data.to_csv("salary_predictions.csv", index=False)
print("Predictions saved to salary_predictions.csv")
