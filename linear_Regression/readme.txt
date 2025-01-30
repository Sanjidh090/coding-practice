📈 Exploring Linear Regression: Theory & Implementation!

A few days ago, in my forecasting class, I was introduced to Linear Regression and its formula for predicting data. Since I already knew that Linear Regression is widely used in Machine Learning, I decided to implement it myself!

But instead of just using libraries, I took it a step further and implemented Linear Regression in two ways:

 ✅ With Scikit-Learn – Using LinearRegression to quickly train a model.

 ✅ Without Scikit-Learn – Manually calculating the parameters to understand the math behind it.

💡 The Theory Behind Linear Regression:

 Linear Regression finds a relationship between independent (X) and dependent (Y) variables by fitting a straight line:

Y=mX+cY = mX + cwhere m is the slope and c is the intercept.

💡 The Logic Behind My Implementation:

 📌 With Scikit-Learn, the model learns m and c automatically using Least Squares Regression.

 📌 Without Scikit-Learn, I manually computed m and c using:

Slope (m):

Multiply the number of data points (n) by the sum of the product of X and Y values. Then, subtract the product of the sum of X values and the sum of Y values. Divide this result by the difference between the product of n and the sum of the squares of X values, and the square of the sum of X values.

Intercept (c):

Subtract the product of the slope (m) and the sum of X values from the sum of Y values. Then, divide the result by n.

This helped me gain a deeper understanding of how the algorithm works rather than just using it as a black box!



#MachineLearning #LinearRegression #Python #ScikitLearn #Forecasting 
