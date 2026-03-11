# Dataset Download Instructions

## Option 1: Use the Provided Sample Dataset (Recommended)

The capstone project includes a sample dataset (`sales_data.csv`) that contains realistic sales and customer data. This dataset is already included in the project folder and is ready to use.

### Dataset Details:
- **File**: `sales_data.csv`
- **Size**: 10,000+ records (sample provided with 50 records)
- **Features**: 15 columns including customer demographics, product information, and sales data
- **Format**: CSV (Comma Separated Values)

### Dataset Schema:
| Column | Description | Data Type |
|--------|-------------|-----------|
| customer_id | Unique customer identifier | String |
| age | Customer age | Integer |
| gender | Customer gender | String |
| location | Customer location/city | String |
| income | Annual income | Integer |
| registration_date | Customer registration date | Date |
| purchase_date | Purchase transaction date | Date |
| product_category | Product category | String |
| brand | Product brand | String |
| price | Product price | Float |
| quantity | Quantity purchased | Integer |
| revenue | Total revenue (price × quantity) | Float |
| purchase_frequency | Purchases per year | Integer |
| avg_order_value | Average order value | Float |
| customer_lifespan | Years as customer | Float |

## Option 2: Generate Your Own Dataset

If you want to create a larger dataset or customize the data, you can use the provided Python script:

### Steps:
1. **Install Required Libraries**:
   ```bash
   pip install pandas numpy
   ```

2. **Run the Data Generator**:
   ```bash
   python generate_sample_data.py
   ```

3. **Customize the Dataset**:
   - Modify `n_records` parameter to change dataset size
   - Adjust probability distributions for different data patterns
   - Add new product categories or locations
   - Modify missing value percentages

## Option 3: Use Real-World Datasets

### Recommended Public Datasets:

#### 1. Kaggle E-commerce Dataset
- **URL**: https://www.kaggle.com/datasets/carrie1/ecommerce-data
- **Description**: Online retail data with customer transactions
- **Size**: 541,909 records
- **Features**: Customer ID, product description, quantity, price, date, country

#### 2. UCI Online Retail Dataset
- **URL**: https://archive.ics.uci.edu/ml/datasets/Online+Retail
- **Description**: Online retail transactions from UK-based company
- **Size**: 541,909 records
- **Features**: Invoice, stock code, description, quantity, invoice date, price, customer ID, country

#### 3. Amazon Customer Behavior Dataset
- **URL**: https://www.kaggle.com/datasets/mehdidag/amazon-customer-behavior-dataset
- **Description**: Amazon customer purchase behavior
- **Size**: 100,000+ records
- **Features**: Customer demographics, purchase history, ratings

### Data Preprocessing Required:
If using external datasets, you may need to:
- Clean and standardize column names
- Handle missing values appropriately
- Convert data types (dates, categories)
- Create derived features (CLV, recency, frequency)
- Ensure data privacy compliance

## Option 4: Create Synthetic Data with Faker

For more realistic synthetic data, you can use the Faker library:

### Installation:
```bash
pip install faker pandas numpy
```

### Example Code:
```python
from faker import Faker
import pandas as pd
import numpy as np

fake = Faker()

# Generate realistic customer data
def generate_customer_data(n_records=10000):
    data = []
    for i in range(n_records):
        record = {
            'customer_id': f"CUST_{i+1:05d}",
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'address': fake.address(),
            'city': fake.city(),
            'state': fake.state(),
            'zipcode': fake.zipcode(),
            'age': fake.random_int(min=18, max=80),
            'income': fake.random_int(min=20000, max=200000),
            'registration_date': fake.date_between(start_date='-3y', end_date='today'),
            'purchase_date': fake.date_between(start_date='-2y', end_date='today'),
            'product_category': fake.random_element(elements=('Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books')),
            'price': round(fake.random.uniform(10, 1000), 2),
            'quantity': fake.random_int(min=1, max=10),
        }
        record['revenue'] = record['price'] * record['quantity']
        data.append(record)
    
    return pd.DataFrame(data)

# Generate and save data
df = generate_customer_data(10000)
df.to_csv('synthetic_sales_data.csv', index=False)
```

## Dataset Requirements for the Project

### Minimum Requirements:
- **Size**: At least 1,000 records (10,000+ recommended)
- **Features**: 10+ columns including:
  - Customer demographics (age, gender, location, income)
  - Product information (category, price, brand)
  - Sales data (date, quantity, revenue)
  - Customer behavior (frequency, recency, CLV)

### Data Quality Considerations:
- **Missing Values**: 5-15% missing values for realistic analysis
- **Outliers**: Some outliers for statistical analysis practice
- **Data Types**: Mix of numerical, categorical, and date data
- **Time Range**: At least 1 year of transaction data

## Privacy and Ethics Notes

### Data Privacy:
- **No Real Personal Data**: Use only synthetic or anonymized data
- **GDPR Compliance**: Ensure data doesn't contain personally identifiable information
- **Academic Use Only**: Datasets should be used for educational purposes

### Ethical Considerations:
- **Bias Awareness**: Be mindful of potential biases in synthetic data
- **Fair Representation**: Ensure diverse representation in demographic data
- **Transparent Methodology**: Document data generation methods

## Troubleshooting

### Common Issues:

1. **File Not Found Error**:
   - Ensure `sales_data.csv` is in the same directory as your notebook
   - Check file path and permissions

2. **Encoding Issues**:
   - Try different encodings: `pd.read_csv('file.csv', encoding='utf-8')`
   - Or: `pd.read_csv('file.csv', encoding='latin-1')`

3. **Memory Issues**:
   - For large datasets, use chunking: `pd.read_csv('file.csv', chunksize=1000)`
   - Consider data sampling for initial analysis

4. **Date Parsing Errors**:
   - Specify date format: `pd.to_datetime(df['date'], format='%Y-%m-%d')`
   - Handle different date formats appropriately

## Support

If you encounter issues with the dataset:
1. Check the data quality report in your analysis
2. Verify column names and data types
3. Ensure all required features are present
4. Contact the instructor for dataset-related questions

Remember: The goal is to demonstrate your data analysis skills, not to work with perfect data. Real-world data is messy, and handling that messiness is part of the learning process!





