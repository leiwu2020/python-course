# Capstone Project: Sales Data Analysis & Machine Learning Dashboard

## Project Overview
This capstone project presents an end-to-end data analysis and visualization dashboard using a dataset of ~10,000 customer sales transactions. The goal is to demonstrate proficiency in Python programming, data manipulation, statistical analysis, visualization, and machine learning. The project delivers a complete analytical pipeline—from raw data to business insights and trained machine learning models.

---

## 1. Project Structure

.
├── analysis_notebook.ipynb
├── data/sales_data.csv (not included)
├── models/...
├── visualizations/...
├── requirements.txt
├── presentation.pdf
├── README.md
└── Business_Recommendations.md

---

## 2. Setup Instructions

### Prerequisites
- Python 3.8+
- Jupyter Notebook or JupyterLab
- pip or conda

### Install Dependencies
pip install -r requirements.txt

### Launch Notebook
jupyter notebook analysis_notebook.ipynb

Ensure the sales_data.csv file is placed in the correct directory or update the path in the notebook.

---

## 3. Dataset Description

The dataset includes ~10,000 rows and 15+ features:

### Customer Demographics
- Age  
- Gender  
- Location  
- Income  

### Product Information
- Category  
- Brand  
- Price  

### Transaction Information
- Transaction date  
- Quantity  
- Revenue  

### Behavioral Metrics
- Average order value  
- Purchase frequency  
- Customer lifespan  

---

## 4. Analysis Pipeline Summary

### 4.1 Data Loading & Exploration
- Loaded dataset using pandas
- Displayed dataset shape, columns, and data types
- Identified and handled missing values
- Performed exploratory data analysis (EDA)
- Conducted data quality assessment

### 4.2 Data Cleaning & Preprocessing
- Imputed missing values (median for numeric, mode for categorical)
- Standardized formats
- Created derived columns (e.g., calculated_revenue)
- Engineered High_Value_Customer target label (top 30% of revenue)
- Encoded categorical variables (LabelEncoder + One-Hot Encoding)
- Scaled numerical features using StandardScaler
- Built final feature set of 39 predictors

### 4.3 Statistical Analysis
- Descriptive statistics for key metrics
- Correlation analysis with heatmaps
- Hypothesis testing (t-tests, chi-square tests)
- Confidence interval calculations
- Identified statistically significant trends

### 4.4 Data Visualization
Created and saved visualizations including:
- Histograms
- Box plots
- Scatter plots
- Bar charts
- Heatmaps
- Time series trends
- Category and brand breakdowns
- Feature importance charts

All plots include titles, labels, and styling, and are saved in the visualizations/ folder.

### 4.5 Machine Learning Implementation

#### Classification Model
Goal: Predict whether a customer is a High Value Customer  
Model: RandomForestClassifier  
Performance:
- Accuracy: 97%
- Strong precision/recall balance  
Artifacts Saved:
- random_forest_classifier.pkl (trained classification model)
- scaler_classification.pkl (feature scaling for classification)
- label_encoder_gender.pkl (encodes gender for model input)
- final_features.pkl (ordered feature list used by the model)
- feature_cols_base.pkl (base numeric features)
- one_hot_columns.pkl (encoded categorical features)

#### Regression Model
Goal: Predict revenue  
Model: GradientBoostingRegressor  
Performance:
- MAE: ~$25  
- RMSE: ~$41  
- R² Score: 0.97  
Artifacts Saved:
- gradient_boosting_regressor.pkl (trained regression model)
- scaler_regression.pkl (feature scaling for regression)
- final_features.pkl (same feature set as classification)
- feature_cols_base.pkl (base numeric features)
- one_hot_columns.pkl (encoded categorical features)

---

## 5. Deliverables Checklist

- analysis_notebook.ipynb ✔  
- requirements.txt ✔  
- README.md ✔  
- presentation.pdf ✔  
- ML Model Pickles (models/) ✔  
- Saved Visualizations (visualizations/) ✔  
- Business Insights & Recommendations ✔  

---

## 6. Running the Machine Learning Models

Example usage:

import pickle
rf = pickle.load(open("models/scaler_classification.pkl", "rb"))

Models require the same feature preprocessing pipeline used during training.

---

## 7. Bonus Features
- Streamlit or Dash interactive dashboard
- Ensemble ML enhancements

---

## 8. Conclusion
This project demonstrates full mastery of data wrangling, statistical analysis, visualization, and machine learning. It converts raw sales data into insights and features production-ready models that support revenue optimization, customer segmentation, and strategic business planning.
