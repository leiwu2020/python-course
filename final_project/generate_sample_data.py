#!/usr/bin/env python3
"""
Sample Data Generator for Capstone Project
Generates realistic sales and customer data for analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_sample_data(n_records=10000):
    """Generate sample sales data for the capstone project"""
    
    # Set random seed for reproducibility
    np.random.seed(42)
    random.seed(42)
    
    # Customer demographics
    genders = ['Male', 'Female', 'Other']
    locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
                'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
                'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte',
                'San Francisco', 'Indianapolis', 'Seattle', 'Denver', 'Boston']
    
    categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books']
    brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D', 'Brand E']
    
    # Generate base data
    data = []
    
    for i in range(n_records):
        # Customer ID
        customer_id = f"CUST_{i+1:05d}"
        
        # Demographics
        age = np.random.normal(35, 12)
        age = max(18, min(80, int(age)))  # Clamp between 18-80
        
        income = np.random.lognormal(10.5, 0.5)  # Log-normal for realistic income distribution
        income = max(20000, min(200000, int(income)))
        
        gender = np.random.choice(genders, p=[0.48, 0.48, 0.04])
        location = np.random.choice(locations)
        
        # Registration date (last 3 years)
        reg_date = datetime.now() - timedelta(days=np.random.randint(30, 1095))
        
        # Purchase date (after registration)
        purchase_date = reg_date + timedelta(days=np.random.randint(1, (datetime.now() - reg_date).days))
        
        # Product information
        category = np.random.choice(categories, p=[0.35, 0.25, 0.20, 0.15, 0.05])
        brand = np.random.choice(brands)
        
        # Price varies by category
        base_prices = {'Electronics': 200, 'Clothing': 50, 'Home & Garden': 80, 'Sports': 100, 'Books': 15}
        base_price = base_prices[category]
        price = max(10, np.random.normal(base_price, base_price * 0.3))
        
        # Purchase behavior
        quantity = np.random.poisson(2) + 1  # At least 1 item
        revenue = price * quantity
        
        # Customer behavior metrics
        purchase_frequency = np.random.poisson(3) + 1  # Purchases per year
        avg_order_value = revenue * np.random.uniform(0.8, 1.2)  # Slight variation
        customer_lifespan = (datetime.now() - reg_date).days / 365.25  # Years as customer
        
        # Add some missing values (5-10% missing)
        if np.random.random() < 0.08:
            age = np.nan
        if np.random.random() < 0.06:
            income = np.nan
        if np.random.random() < 0.05:
            gender = np.nan
        if np.random.random() < 0.04:
            location = np.nan
        
        # Create record
        record = {
            'customer_id': customer_id,
            'age': age,
            'gender': gender,
            'location': location,
            'income': income,
            'registration_date': reg_date.strftime('%Y-%m-%d'),
            'purchase_date': purchase_date.strftime('%Y-%m-%d'),
            'product_category': category,
            'brand': brand,
            'price': round(price, 2),
            'quantity': quantity,
            'revenue': round(revenue, 2),
            'purchase_frequency': purchase_frequency,
            'avg_order_value': round(avg_order_value, 2),
            'customer_lifespan': round(customer_lifespan, 2)
        }
        
        data.append(record)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Add some outliers for analysis
    outlier_indices = np.random.choice(df.index, size=int(0.03 * len(df)), replace=False)
    df.loc[outlier_indices, 'revenue'] *= np.random.uniform(3, 8, len(outlier_indices))
    df.loc[outlier_indices, 'avg_order_value'] *= np.random.uniform(2, 5, len(outlier_indices))
    
    return df

def main():
    """Generate and save the sample dataset"""
    print("Generating sample sales data...")
    
    # Generate data
    df = generate_sample_data(10000)
    
    # Save to CSV
    output_file = 'sales_data.csv'
    df.to_csv(output_file, index=False)
    
    print(f"✅ Sample dataset generated successfully!")
    print(f"📁 File saved as: {output_file}")
    print(f"📊 Dataset shape: {df.shape}")
    print(f"💰 Total revenue: ${df['revenue'].sum():,.2f}")
    print(f"👥 Unique customers: {df['customer_id'].nunique()}")
    print(f"📅 Date range: {df['purchase_date'].min()} to {df['purchase_date'].max()}")
    
    # Display sample
    print("\n📋 Sample data preview:")
    print(df.head())
    
    # Data quality summary
    print("\n🔍 Data quality summary:")
    print(f"Missing values: {df.isnull().sum().sum()}")
    print(f"Duplicate rows: {df.duplicated().sum()}")
    
    return df

if __name__ == "__main__":
    df = main()

