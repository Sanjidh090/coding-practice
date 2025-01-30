import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load dataset
df = pd.read_csv(r"C:\Users\sanji\Downloads\Salary_dataset.csv")
df = df.drop('Unnamed: 0', axis=1)

# Prepare data
X = df[["YearsExperience"]]  # Independent variable
y = df["Salary"]  # Dependent variable

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Get parameters
m = model.coef_[0]  # Slope
c = model.intercept_  # Intercept
print(f"Equation of the Line: Salary = {m:.2f} * Experience + {c:.2f}")

# Predictions
y_pred = model.predict(X_test)

# Predict salary for 10 years of experience
experience = np.array([[10]])
predicted_salary = model.predict(experience)
print(f"Predicted Salary for 10 Years Experience: ${predicted_salary[0]:,.2f}")

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")

# Plot results
plt.scatter(X_train, y_train, color='blue', label="Training Data")
plt.scatter(X_test, y_test, color='red', label="Testing Data")
plt.plot(X, model.predict(X), color='green', linewidth=2, label="Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary Prediction using Linear Regression")
plt.legend()
plt.show()
