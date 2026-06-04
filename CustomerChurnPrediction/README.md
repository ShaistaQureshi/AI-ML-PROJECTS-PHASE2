# Customer Churn Prediction Pipeline

## Objective
Build an end-to-end machine learning pipeline to predict customer churn using the Telco Customer Churn dataset.

## Dataset
The project uses the Telco Customer Churn dataset containing customer demographics, subscription details, contract information, and billing records.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

## Project Workflow
1. Data Loading
2. Data Cleaning
3. Missing Value Handling
4. Feature Selection
5. Data Preprocessing
   - StandardScaler for numerical features
   - OneHotEncoder for categorical features
6. Pipeline Construction using Scikit-learn Pipeline API
7. Random Forest Classification
8. Hyperparameter Tuning using GridSearchCV
9. Model Evaluation
10. Model Export using Joblib

## Model Performance

### Best Parameters
- max_depth = 10
- n_estimators = 100

### Results
- Best Cross Validation Accuracy: **80.1%**
- Final Test Accuracy: **79.3%**

