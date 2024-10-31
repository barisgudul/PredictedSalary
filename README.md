# Simple Linear Regression - Salary Prediction

This project implements a Simple Linear Regression model using Python to predict salaries based on years of experience. Given a dataset of experience in years and corresponding salaries, the model is trained to understand the linear relationship between these two variables.
---
# Table of Contents

1. [Simple Linear Regression - Salary Prediction](#simple-linear-regression---salary-prediction)
2. [Dataset](#dataset)
   - [Sample Data](#sample-data)
3. [Project Steps](#project-steps)
   - [1. Import Libraries](#1-import-libraries)
   - [2. Load Dataset](#2-load-dataset)
   - [3. Split Data](#3-split-data)
   - [4. Train the Model](#4-train-the-model)
   - [5. Make Predictions](#5-make-predictions)
   - [6. Visualize Results](#6-visualize-results)
   - [7. Single Prediction](#7-single-prediction)
   - [8. Regression Equation](#8-regression-equation)
   - [9. Visualizations](#9-visualizations)
---
## Dataset

The dataset (`Salary_Data.csv`) includes two columns:
- `YearsExperience`: The number of years an employee has worked.
- `Salary`: The salary corresponding to each level of experience.

### Sample Data

| YearsExperience | Salary   |
|-----------------|----------|
| 1.1             | 39343.00 |
| 2.0             | 43525.00 |
| 3.0             | 60150.00 |
| ...             | ...      |
| 10.5            | 121872.00|

## Project Steps

1. **Import Libraries**: Necessary libraries such as `pandas`, `numpy`, and `matplotlib` for data manipulation and visualization, as well as `LinearRegression` from `sklearn` for the model.

2. **Load Dataset**: The `Salary_Data.csv` file is loaded and split into input (`X`) and output (`y`) variables.

3. **Split Data**: The data is divided into training and testing sets using an 80-20 split.

4. **Train the Model**: A Simple Linear Regression model is trained on the training set.

5. **Make Predictions**: The model predicts salaries for the test set.

6. **Visualize Results**:
    - Training data and regression line.
    - Testing data with the regression line applied.

7. **Single Prediction**:
   Predicts the salary of an employee with 12 years of experience.

8. **Regression Equation**:
   The equation of the regression line is printed as \( y = b_0 + b_1 \times x \), where \( b_0 \) is the intercept and \( b_1 \) is the coefficient (slope).

9. **Visualizations**:
    -### Salary vs Experience (Test)
     ![Salary vs Experience (Train)](Salary_vs_Experience(train).png)
   ---
    -### Salary vs Experience (Train)
     ![Salary vs Experience (Test)](Salary_vs_Experience(test).png)
