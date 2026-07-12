import streamlit as st
import pandas as pd
import os

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Neural Retail AI Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# Title
# -------------------------------
st.title("🛍️ Neural Retail AI Dashboard")
st.markdown("### AI Powered Retail Business Analytics")

st.write("---")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "Demand Forecasting",
        "Customer Analytics",
        "Inventory Optimization"
    ]
)

# -------------------------------
# HOME PAGE
# -------------------------------
if page == "Home":

    st.header("Welcome")

    st.success("Dashboard is running successfully.")

    st.markdown("""
## Platform Overview

The Neural Retail AI Dashboard is an integrated analytics solution designed to help retail businesses make data-driven decisions through artificial intelligence and interactive visualization.

### Key Features

- 📊 Interactive Business Dashboard
- 📈 AI-Based Demand Forecasting
- 👥 Customer Segmentation & Analytics
- 📦 Inventory Optimization
- ⚡ FastAPI Integration
- 🐳 Dockerized Deployment
""")
# -------------------------------
# DEMAND FORECAST PAGE
# -------------------------------
elif page == "Demand Forecasting":

    st.header("Demand Forecasting")

    file_path = "Data/Dashboard_Forecast.csv"

    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        st.success("Forecast Data Loaded Successfully")

        st.dataframe(df)

        st.subheader("Forecast Trend")

        st.line_chart(df["yhat"])

    else:

        st.error("Dashboard_Forecast.csv not found inside Data folder.")# -------------------------------
# CUSTOMER ANALYTICS PAGE
# -------------------------------
elif page == "Customer Analytics":

    st.header("👥 Customer Analytics")

    file_path = "Data/Customer_Analytics_Final.csv"

    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        st.success("Customer Analytics Data Loaded Successfully")

        st.subheader("Customer Analytics Dataset")
        st.dataframe(df)

        st.subheader("Dataset Shape")
        st.write(df.shape)

        st.subheader("Columns")
        st.write(df.columns.tolist())

        st.subheader("Statistics")
        st.dataframe(df.describe())

    else:

        st.error("Customer_Analytics_Final.csv not found.")# -------------------------------
# -------------------------------
# INVENTORY PAGE
# -------------------------------
elif page == "Inventory Optimization":

    st.header("📦 Inventory Optimization")

    st.success("Inventory module integrated successfully.")

    if os.path.exists("Data/online_retail_II_data.csv"):

        retail = pd.read_csv(
            "Data/online_retail_II_data.csv",
            encoding="latin1"
        )

        st.subheader("Retail Dataset")
        st.dataframe(retail.head(20))

        st.subheader("Basic Statistics")
        st.dataframe(retail.describe())

        st.subheader("Top 10 Selling Products")

        top_products = (
            retail.groupby("Description")["Quantity"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        st.bar_chart(top_products)

    else:

        st.warning("Retail dataset is not available in the deployed version.")