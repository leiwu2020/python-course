# app.py

import datetime as dt
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.metrics import (
    accuracy_score,
    r2_score,
    mean_squared_error,
)

# -----------------------------
# PATHS
# -----------------------------
BASE_DIR = Path("/Users/tristanpoul/Library/CloudStorage/GoogleDrive-tpoul@scu.edu/Shared drives/OMIS 114 Capstone")
DATA_PATH = BASE_DIR / "data" / "sales_data.csv"

# -----------------------------
# STREAMLIT CONFIG
# -----------------------------
st.set_page_config(
    page_title="Sales & Customer Insights Dashboard",
    layout="wide"
)

sns.set_style("darkgrid")
plt.rcParams["figure.figsize"] = (10, 5)

PRIMARY_RED = "#862633"
PRIMARY_GRAY = "#5b6770"
PRIMARY_GREEN = "#737b4c"
PRIMARY_YELLOW = "#eaaa00"

# -----------------------------
# DATA LOADING & PREP
# -----------------------------
@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        st.error(f"Data file not found at: {path}")
        return pd.DataFrame()

    df = pd.read_csv(
        path,
        dtype={
            "customer_id": "string",
            "gender": "string",
            "location": "string",
            "product_category": "string",
            "brand": "string",
        },
    )

    # Parse dates
    df["purchase_date"] = pd.to_datetime(df.get("purchase_date"), errors="coerce")
    df["registration_date"] = pd.to_datetime(df.get("registration_date"), errors="coerce")

    # Basic cleaning (consistent with ML part of your notebook)
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())

    cat_cols = df.select_dtypes(include=["object", "string"]).columns.tolist()
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Revenue consistency
    if {"price", "quantity"}.issubset(df.columns):
        df["calculated_revenue"] = df["price"] * df["quantity"]
        df["revenue"] = df["revenue"].fillna(df["calculated_revenue"])

    return df


@st.cache_data
def compute_rfm(df: pd.DataFrame) -> pd.DataFrame:
    if "customer_id" not in df.columns or "purchase_date" not in df.columns or "revenue" not in df.columns:
        return pd.DataFrame()

    current_date = df["purchase_date"].max() + dt.timedelta(days=1)

    if "purchase_frequency" in df.columns:
        freq_agg = "max"
    else:
        # fallback: transaction count
        freq_agg = "size"

    rfm = df.groupby("customer_id").agg({
        "purchase_date": lambda x: (current_date - x.max()).days,  # Recency
        "purchase_frequency": freq_agg if "purchase_frequency" in df.columns else freq_agg,
        "revenue": "sum"
    }).reset_index()

    rfm.rename(columns={
        "purchase_date": "Recency",
        "purchase_frequency": "Frequency",
        "revenue": "Monetary"
    }, inplace=True)

    # Scores 1–4
    rfm["R_Score"] = pd.qcut(rfm["Recency"], 4, labels=[4, 3, 2, 1])
    rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 4, labels=[1, 2, 3, 4])
    rfm["M_Score"] = pd.qcut(rfm["Monetary"], 4, labels=[1, 2, 3, 4])
    rfm["RFM_Score"] = rfm["R_Score"].astype(str) + rfm["F_Score"].astype(str) + rfm["M_Score"].astype(str)

    def segment_customer(row):
        r = int(row["R_Score"])
        f = int(row["F_Score"])
        m = int(row["M_Score"])

        if r >= 4 and f >= 4 and m >= 4:
            return "Champions"
        elif r >= 3 and f >= 3:
            return "Loyal Customers"
        elif r >= 3 and m >= 3:
            return "Big Spenders"
        elif r >= 3 and f <= 2:
            return "Promising New"
        elif r <= 2 and f >= 3:
            return "At Risk"
        elif r <= 1 and f <= 2:
            return "Lost"
        else:
            return "Standard"

    rfm["Segment"] = rfm.apply(segment_customer, axis=1)

    return rfm


@st.cache_data
def prepare_model_data(df: pd.DataFrame):
    """
    Mirror the ML prep in your notebook:
    - Create High_Value_Customer
    - Encode gender
    - One-hot location/product_category/brand
    """
    df_model = df.copy()

    # Define high-value customers (top 30% by revenue)
    revenue_threshold = df_model["revenue"].quantile(0.70)
    df_model["High_Value_Customer"] = (df_model["revenue"] > revenue_threshold).astype(int)

    # Encode gender
    le = LabelEncoder()
    df_model["gender_encoded"] = le.fit_transform(df_model["gender"])

    # Base features
    feature_cols = [
        "age",
        "gender_encoded",
        "income",
        "purchase_frequency",
        "avg_order_value",
        "customer_lifespan",
    ]
    feature_cols = [c for c in feature_cols if c in df_model.columns]

    # One-hot encode
    ohe_cols = [c for c in ["location", "product_category", "brand"] if c in df_model.columns]
    df_encoded = pd.get_dummies(df_model, columns=ohe_cols, drop_first=True)

    one_hot_cols = [
        c for c in df_encoded.columns
        if c.startswith(("location_", "product_category_", "brand_"))
    ]

    final_features = feature_cols + one_hot_cols

    return df_model, df_encoded, final_features, le


@st.cache_resource
def train_models(df_encoded: pd.DataFrame, final_features: list):
    """
    Train RandomForest classifier and GradientBoosting regressor
    using the same structure as your notebook.
    """
    # --- Classification ---
    X_class = df_encoded[final_features]
    y_class = df_encoded["High_Value_Customer"]

    X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
        X_class, y_class, test_size=0.2, random_state=42
    )

    scaler_c = StandardScaler()
    X_train_c_scaled = scaler_c.fit_transform(X_train_c)
    X_test_c_scaled = scaler_c.transform(X_test_c)

    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train_c_scaled, y_train_c)

    y_pred_c = rf_classifier.predict(X_test_c_scaled)
    class_accuracy = accuracy_score(y_test_c, y_pred_c)

    # --- Regression ---
    X_reg = df_encoded[final_features]
    y_reg = df_encoded["revenue"]

    X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
        X_reg, y_reg, test_size=0.2, random_state=42
    )

    scaler_r = StandardScaler()
    X_train_r_scaled = scaler_r.fit_transform(X_train_r)
    X_test_r_scaled = scaler_r.transform(X_test_r)

    gb_regressor = GradientBoostingRegressor(
        n_estimators=100,
        learning_rate=0.1,
        random_state=42
    )
    gb_regressor.fit(X_train_r_scaled, y_train_r)

    y_pred_r = gb_regressor.predict(X_test_r_scaled)
    rmse = np.sqrt(mean_squared_error(y_test_r, y_pred_r))
    r2 = r2_score(y_test_r, y_pred_r)

    metrics = {
        "class_accuracy": class_accuracy,
        "reg_rmse": rmse,
        "reg_r2": r2,
    }

    return rf_classifier, gb_regressor, scaler_c, scaler_r, metrics


# -----------------------------
# LOAD DATA
# -----------------------------
df = load_data(DATA_PATH)
if df.empty:
    st.stop()

# RFM + model prep
rfm = compute_rfm(df)
df_model, df_encoded, final_features, le_model = prepare_model_data(df)

# Add weekday if not present
if "purchase_date" in df.columns and "purchase_weekday" not in df.columns:
    df["purchase_weekday"] = df["purchase_date"].dt.day_name()

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.title("Filters")

min_date = df["purchase_date"].min()
max_date = df["purchase_date"].max()

date_range = st.sidebar.date_input(
    "Purchase Date Range",
    value=(
        min_date.date() if pd.notna(min_date) else dt.date(2024, 1, 1),
        max_date.date() if pd.notna(max_date) else dt.date(2024, 12, 31),
    )
)

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date.date(), max_date.date()

mask_date = (df["purchase_date"].dt.date >= start_date) & (df["purchase_date"].dt.date <= end_date)

categories = sorted(df["product_category"].dropna().unique().tolist()) if "product_category" in df.columns else []
selected_cats = st.sidebar.multiselect("Product Categories", categories, default=categories)

if categories:
    mask_cat = df["product_category"].isin(selected_cats)
else:
    mask_cat = True

locations = sorted(df["location"].dropna().unique().tolist()) if "location" in df.columns else []
selected_locs = st.sidebar.multiselect("Locations", locations, default=locations)

if locations:
    mask_loc = df["location"].isin(selected_locs)
else:
    mask_loc = True

filtered_df = df[mask_date & mask_cat & mask_loc]

st.sidebar.markdown("---")
st.sidebar.write(f"Filtered records: **{len(filtered_df)}**")

# -----------------------------
# LAYOUT: TABS
# -----------------------------
st.title("Sales & Customer Insights Dashboard")

tab_overview, tab_segments, tab_models = st.tabs(
    ["📊 Overview", "👥 Customer Segments (RFM)", "🤖 Predictive Models"]
)

# -----------------------------
# TAB 1: OVERVIEW
# -----------------------------
with tab_overview:
    st.subheader("High-Level KPIs")

    total_revenue = filtered_df["revenue"].sum() if "revenue" in filtered_df.columns else 0
    num_orders = len(filtered_df)
    num_customers = filtered_df["customer_id"].nunique() if "customer_id" in filtered_df.columns else 0
    avg_order_value = total_revenue / num_orders if num_orders > 0 else 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue (Filtered)", f"${total_revenue:,.0f}")
    col2.metric("Number of Orders", f"{num_orders:,}")
    col3.metric("Unique Customers", f"{num_customers:,}")
    col4.metric("Average Order Value", f"${avg_order_value:,.2f}")

    st.markdown("---")
    st.subheader("Sales & Customer Distributions")

    col_a, col_b = st.columns(2)

    with col_a:
        if "age" in filtered_df.columns:
            st.write("**Customer Age Distribution**")
            fig, ax = plt.subplots()
            sns.histplot(filtered_df["age"].dropna(), bins=30, kde=True, ax=ax, color=PRIMARY_RED)
            ax.set_xlabel("Age")
            ax.set_ylabel("Count")
            st.pyplot(fig)

    with col_b:
        if "product_category" in filtered_df.columns and "revenue" in filtered_df.columns:
            st.write("**Revenue by Product Category**")
            cat_rev = (
                filtered_df.groupby("product_category")["revenue"]
                .sum()
                .sort_values(ascending=False)
            )
            fig, ax = plt.subplots()
            sns.barplot(x=cat_rev.values, y=cat_rev.index, ax=ax, color=PRIMARY_GREEN)
            ax.set_xlabel("Total Revenue")
            ax.set_ylabel("Product Category")
            st.pyplot(fig)

    st.markdown("---")

    if "purchase_date" in filtered_df.columns and "revenue" in filtered_df.columns:
        st.subheader("Monthly Revenue Trend")
        monthly = (
            filtered_df
            .dropna(subset=["purchase_date"])
            .groupby(filtered_df["purchase_date"].dt.to_period("M"))["revenue"]
            .sum()
            .sort_index()
        )
        if not monthly.empty:
            fig, ax = plt.subplots()
            ax.plot(monthly.index.to_timestamp(), monthly.values, marker="o", color=PRIMARY_RED)
            ax.set_xlabel("Month")
            ax.set_ylabel("Revenue")
            plt.xticks(rotation=45)
            st.pyplot(fig)

    if "purchase_weekday" in filtered_df.columns and "revenue" in filtered_df.columns:
        st.subheader("Revenue by Day of Week")
        order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        weekday_rev = (
            filtered_df.groupby("purchase_weekday")["revenue"]
            .sum()
            .reindex(order)
            .dropna()
        )
        if not weekday_rev.empty:
            fig, ax = plt.subplots()
            sns.barplot(x=weekday_rev.index, y=weekday_rev.values, ax=ax, color=PRIMARY_GRAY)
            ax.set_xlabel("Day of Week")
            ax.set_ylabel("Total Revenue")
            plt.xticks(rotation=45)
            st.pyplot(fig)

# -----------------------------
# TAB 2: CUSTOMER SEGMENTS (RFM)
# -----------------------------
with tab_segments:
    st.subheader("RFM Segmentation")

    if rfm.empty:
        st.info("RFM segmentation could not be computed (missing required columns).")
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Segment Distribution (Count)**")
            segment_counts = rfm["Segment"].value_counts().sort_values(ascending=False)
            fig, ax = plt.subplots()
            sns.barplot(x=segment_counts.index, y=segment_counts.values, ax=ax, palette="viridis")
            ax.set_ylabel("Number of Customers")
            ax.set_xlabel("Segment")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        with col2:
            st.write("**Monetary Value by Segment**")
            fig, ax = plt.subplots()
            sns.boxplot(x="Segment", y="Monetary", data=rfm, ax=ax)
            ax.set_xlabel("Segment")
            ax.set_ylabel("Monetary (Total Revenue)")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        st.markdown("---")

        st.write("**Recency vs Frequency by Segment**")
        fig, ax = plt.subplots()
        sns.scatterplot(
            x="Recency",
            y="Frequency",
            hue="Segment",
            data=rfm,
            alpha=0.7,
            ax=ax
        )
        ax.set_xlabel("Days Since Last Purchase (Recency)")
        ax.set_ylabel("Frequency (# of Orders)")
        st.pyplot(fig)

        st.markdown("---")

        avg_clv = rfm["Monetary"].mean()
        total_revenue_rfm = rfm["Monetary"].sum()
        champion_count = (rfm["Segment"] == "Champions").sum()
        at_risk_count = (rfm["Segment"] == "At Risk").sum()
        at_risk_pct = at_risk_count / len(rfm) * 100 if len(rfm) > 0 else 0

        st.subheader("Key Segment Metrics")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Revenue (RFM)", f"${total_revenue_rfm:,.0f}")
        c2.metric("Avg Customer Value", f"${avg_clv:,.2f}")
        c3.metric("Champions", f"{champion_count:,}")
        c4.metric("At Risk Customers", f"{at_risk_count:,} ({at_risk_pct:.1f}%)")

# -----------------------------
# TAB 3: PREDICTIVE MODELS
# -----------------------------
with tab_models:
    st.subheader("Predictive Models: Classification & Regression")

    if "High_Value_Customer" not in df_encoded.columns:
        st.warning("High_Value_Customer target not found in encoded data.")
    elif not final_features:
        st.warning("No feature columns available for modeling.")
    else:
        rf_classifier, gb_regressor, scaler_c, scaler_r, model_metrics = train_models(
            df_encoded, final_features
        )

        st.markdown("**Global Model Performance**")
        c1, c2 = st.columns(2)
        c1.metric("Classification Accuracy", f"{model_metrics['class_accuracy']:.2%}")
        c2.metric("Revenue Model R²", f"{model_metrics['reg_r2']:.3f}")
        st.caption(f"Revenue model RMSE: ${model_metrics['reg_rmse']:,.2f}")

        st.markdown("---")
        st.info("Select a customer to view model-based predictions and profile.")

        if "customer_id" not in filtered_df.columns:
            st.warning("customer_id column not available for individual predictions.")
        else:
            available_customers = filtered_df["customer_id"].dropna().unique().tolist()

            if not available_customers:
                st.warning("No customers available under current filters.")
            else:
                selected_customer = st.selectbox(
                    "Select a Customer ID",
                    sorted(available_customers)
                )

                cust_rows_encoded = df_encoded[df_encoded["customer_id"] == selected_customer]

                if cust_rows_encoded.empty:
                    st.warning("No encoded data available for this customer.")
                else:
                    row = cust_rows_encoded.iloc[0]
                    X = row[final_features].values.reshape(1, -1)

                    # Classification
                    X_c_scaled = scaler_c.transform(X)
                    y_class_pred = rf_classifier.predict(X_c_scaled)[0]
                    y_class_proba = rf_classifier.predict_proba(X_c_scaled)[0][1]

                    # Regression
                    X_r_scaled = scaler_r.transform(X)
                    y_reg_pred = gb_regressor.predict(X_r_scaled)[0]

                    actual_revenue = (
                        df[df["customer_id"] == selected_customer]["revenue"].sum()
                        if "revenue" in df.columns else np.nan
                    )

                    col_left, col_right = st.columns(2)

                    with col_left:
                        st.write("### High-Value Classification")
                        st.write(f"**Predicted High-Value?**  {'Yes' if y_class_pred == 1 else 'No'}")
                        st.write(f"**Probability of High-Value:**  {y_class_proba:.2%}")
                        st.caption("High-value = top 30% of customers by revenue in the training data.")

                    with col_right:
                        st.write("### Revenue Prediction")
                        st.write(f"**Predicted Revenue Pattern:**  ${y_reg_pred:,.2f}")
                        if not np.isnan(actual_revenue):
                            st.write(f"**Actual Historical Revenue:**  ${actual_revenue:,.2f}")

                    st.markdown("---")

                    st.write("### Customer Profile (Model Inputs)")
                    cols_to_show = [
                        "customer_id", "age", "gender", "income",
                        "purchase_frequency", "avg_order_value",
                        "customer_lifespan", "location", "product_category", "brand"
                    ]
                    cols_to_show = [c for c in cols_to_show if c in df.columns]

                    st.dataframe(
                        df[df["customer_id"] == selected_customer][cols_to_show]
                    )
                    st.caption("These are the attributes the model uses for the predictions above.")
