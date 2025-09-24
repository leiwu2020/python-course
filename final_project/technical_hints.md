# Technical Hints and Recommendations

## Recommended Libraries and Tools

### Core Data Analysis
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import classification_report, confusion_matrix, r2_score
```

### Advanced Visualization
```python
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
```

### Optional Dashboard Tools
```python
import streamlit as st
import dash
from dash import dcc, html
```

## Technical Implementation Strategy

### 1. Data Loading and Exploration
**Best Practices:**
- Use `pd.read_csv()` with appropriate parameters for data types
- Implement `df.info()`, `df.describe()`, and `df.head()` for initial exploration
- Create a data quality report function:
```python
def data_quality_report(df):
    """Generate comprehensive data quality report"""
    report = {
        'shape': df.shape,
        'missing_values': df.isnull().sum(),
        'duplicates': df.duplicated().sum(),
        'data_types': df.dtypes,
        'memory_usage': df.memory_usage(deep=True)
    }
    return report
```

### 2. Data Cleaning Techniques
**Missing Value Handling:**
- Numerical: Use median for skewed distributions, mean for normal distributions
- Categorical: Use mode or create "Unknown" category
- Time series: Forward fill or interpolation

**Outlier Detection:**
```python
# IQR Method
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Z-score Method
from scipy.stats import zscore
z_scores = np.abs(zscore(df['column']))
outliers = df[z_scores > 3]
```

### 3. Feature Engineering
**Derived Features:**
```python
# Customer Lifetime Value
df['clv'] = df['avg_order_value'] * df['purchase_frequency'] * df['customer_lifespan']

# Purchase Recency (days since last purchase)
df['recency'] = (pd.Timestamp.now() - pd.to_datetime(df['last_purchase'])).dt.days

# RFM Analysis
def calculate_rfm(df):
    # Recency, Frequency, Monetary analysis
    rfm = df.groupby('customer_id').agg({
        'purchase_date': 'max',  # Recency
        'order_id': 'count',     # Frequency
        'revenue': 'sum'         # Monetary
    })
    return rfm
```

### 4. Statistical Analysis Implementation
**Correlation Analysis:**
```python
# Correlation matrix
correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.show()
```

**Hypothesis Testing:**
```python
# T-test example
from scipy.stats import ttest_ind
group1 = df[df['segment'] == 'A']['revenue']
group2 = df[df['segment'] == 'B']['revenue']
t_stat, p_value = ttest_ind(group1, group2)
print(f"T-statistic: {t_stat}, P-value: {p_value}")
```

### 5. Visualization Best Practices
**Effective Plot Types:**
- **Distribution**: Histograms, box plots, violin plots
- **Relationships**: Scatter plots, correlation heatmaps
- **Trends**: Line plots, area charts
- **Comparisons**: Bar charts, grouped bar charts
- **Composition**: Pie charts, stacked bar charts

**Styling Guidelines:**
```python
# Set consistent style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Create publication-ready plots
def create_professional_plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    # Your plotting code here
    ax.set_title('Professional Title', fontsize=16, fontweight='bold')
    ax.set_xlabel('X Label', fontsize=12)
    ax.set_ylabel('Y Label', fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('plot.png', dpi=300, bbox_inches='tight')
    plt.show()
```

### 6. Machine Learning Pipeline
**Data Preprocessing:**
```python
# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)
```

**Model Evaluation:**
```python
# Classification metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_classification(y_true, y_pred):
    metrics = {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average='weighted'),
        'recall': recall_score(y_true, y_pred, average='weighted'),
        'f1': f1_score(y_true, y_pred, average='weighted')
    }
    return metrics

# Feature importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
```

### 7. Business Analysis Framework
**Key Metrics to Calculate:**
- Customer Acquisition Cost (CAC)
- Customer Lifetime Value (CLV)
- Revenue per Customer
- Purchase Frequency
- Average Order Value
- Customer Retention Rate

**Segmentation Approaches:**
- RFM Analysis (Recency, Frequency, Monetary)
- Demographic segmentation
- Behavioral segmentation
- Value-based segmentation

### 8. Performance Optimization
**Memory Management:**
```python
# Optimize data types
df['category'] = df['category'].astype('category')
df['date'] = pd.to_datetime(df['date'])
df['price'] = pd.to_numeric(df['price'], downcast='float')
```

**Code Organization:**
```python
# Create modular functions
class SalesAnalyzer:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.preprocessed = False
    
    def preprocess_data(self):
        # Preprocessing logic
        self.preprocessed = True
    
    def analyze_customer_segments(self):
        # Segmentation analysis
        pass
    
    def generate_insights(self):
        # Business insights
        pass
```

### 9. Common Pitfalls to Avoid
- **Data Leakage**: Don't use future information to predict past events
- **Overfitting**: Use cross-validation and regularization
- **Missing Value Bias**: Understand why data is missing
- **Correlation vs Causation**: Don't assume causation from correlation
- **Sample Size**: Ensure adequate sample sizes for statistical tests

### 10. Advanced Techniques (Bonus Points)
**Ensemble Methods:**
```python
from sklearn.ensemble import VotingClassifier, BaggingClassifier
from sklearn.model_selection import cross_val_score

# Voting classifier
voting_clf = VotingClassifier([
    ('rf', RandomForestClassifier()),
    ('lr', LogisticRegression()),
    ('svm', SVC())
])
```

**Feature Engineering:**
```python
# Polynomial features
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Feature selection
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(f_classif, k=10)
X_selected = selector.fit_transform(X, y)
```

## Recommended Project Structure
```
final_project/
├── data/
│   └── sales_data.csv
├── notebooks/
│   └── analysis_notebook.ipynb
├── src/
│   ├── data_processing.py
│   ├── visualization.py
│   ├── modeling.py
│   └── utils.py
├── outputs/
│   ├── plots/
│   ├── models/
│   └── reports/
├── requirements.txt
└── README.md
```

## Debugging Tips
- Use `df.info()` and `df.describe()` frequently
- Check data types with `df.dtypes`
- Validate assumptions with `df.isnull().sum()`
- Use `assert` statements for data validation
- Test functions with small datasets first
- Use logging for debugging complex pipelines

## Resources for Further Learning
- Pandas documentation: https://pandas.pydata.org/docs/
- Scikit-learn user guide: https://scikit-learn.org/stable/user_guide.html
- Matplotlib gallery: https://matplotlib.org/stable/gallery/
- Seaborn examples: https://seaborn.pydata.org/examples/
- Business analytics best practices: Focus on actionable insights

