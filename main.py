### Importing the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Importing the Dataset
dataset = pd.read_csv("Salary_Data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

### Splitting for Train and Test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

### Training the Simple Linear Regression Model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

### Predicting Test set Results
y_pred = regressor.predict(X_test)

### Visualising the Training set Results
plt.figure(figsize=(15,8))
plt.scatter(X_train,y_train, color="red")
plt.plot(X_train,regressor.predict(X_train), color="blue", linestyle="-")
plt.title("Salary vs Experience (Train)")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()

### Visualising the Test set Results
plt.scatter(X_test,y_test,color="red")
plt.plot(X_train,regressor.predict(X_train),color="blue", linestyle="--")
plt.title("Salary vs Experience (Test)")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()

"""
### How much salary  get who 12 experience
years_of_experience = np.array([[12]])
predicted_salary = regressor.predict(years_of_experience)

print(predicted_salary)


### Equation of regression 
b0 = regressor.intercept_
b1 = regressor.coef_[0]

print(f" y = {b0:.2f} + {b1:.2f} * X")
"""
