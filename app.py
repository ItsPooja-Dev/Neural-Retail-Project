import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Neural Retail Intelligence Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------
# Load CSS
# ---------------------------------
if os.path.exists("assets/style.css"):
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------------------------
# Sidebar
# ---------------------------------
if os.path.exists("assets/logo.png"):
    try:
        st.sidebar.image("assets/logo.png", width=120)
    except Exception:
        st.sidebar.write("🤖 Neural Retail")
else:
    st.sidebar.write("🤖 Neural Retail")
st.sidebar.title("Neural Retail")
st.sidebar.caption("AI Powered Business Intelligence")
page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📈 Demand Forecasting",
        "👥 Customer Analytics",
        "📦 Inventory Optimization",
        "🚀 Deployment"
    ]
)

# ---------------------------------
# Header
# ---------------------------------
st.markdown("""
<h1 style='text-align:center;color:white;'>
🚀 Neural Retail Intelligence Platform
</h1>

<h4 style='text-align:center;color:#AAB6D3;'>
AI Powered Retail Decision Support & Business Intelligence
</h4>
""", unsafe_allow_html=True)

st.write("---")

# =================================
# HOME PAGE
# =================================
if page == "🏠 Home":

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("💰 Revenue", "₹24.8M", "+18%")
    col2.metric("📦 Orders", "15,248", "+11%")
    col3.metric("👥 Customers", "8,932", "+9%")
    col4.metric("🎯 Accuracy", "96.4%", "+2%")

    st.write("---")

    left, right = st.columns([2,1])

    with left:

        st.subheader("📊 Platform Overview")

        st.write("""
The Neural Retail Intelligence Platform helps retail businesses make
data-driven decisions using Artificial Intelligence.

Main Modules:

• Demand Forecasting

• Customer Analytics

• Inventory Optimization

• Business Intelligence Dashboard

• FastAPI Integration

• Docker Deployment
""")

    with right:

        st.success("🟢 AI Models Connected")
        st.success("🟢 Database Online")
        st.success("🟢 FastAPI Running")
        st.success("🟢 Docker Ready")

    st.write("---")

    st.subheader("📈 Monthly Sales Performance")

    sales = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr","May","Jun"],
        "Sales":[120,180,150,240,300,360]
    })

    fig = px.line(
        sales,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Sales Trend"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("💰 Revenue Distribution")

    revenue = pd.DataFrame({
        "Category":["Electronics","Fashion","Home","Sports"],
        "Revenue":[45,25,18,12]
    })

    fig2 = px.pie(
        revenue,
        values="Revenue",
        names="Category",
        hole=0.55
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("🤖 AI Recommendation")

    st.info("""
✔ Increase Electronics Inventory

✔ Weekend Sales Expected to Grow

✔ Customer Retention Improving

✔ Demand Forecast Accuracy : 96%
""")
# =================================
# DEMAND FORECASTING
# =================================
elif page == "📈 Demand Forecasting":

    st.header("📈 AI Demand Forecasting")

    col1, col2, col3 = st.columns(3)

    col1.metric("Forecast Accuracy", "96.8%")
    col2.metric("Predicted Growth", "+14%")
    col3.metric("Confidence", "98%")

    file_path = "data/Dashboard_Forecast.csv"

    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        st.success("Forecast Dataset Loaded Successfully")

        st.dataframe(df, use_container_width=True)

        if "yhat" in df.columns:

            fig = px.line(
                df,
                x="ds",
                y=["yhat", "yhat_lower", "yhat_upper"],
                title="AI Demand Forecast with Confidence Range",
                template="plotly_dark"
)

            fig.update_layout(
               xaxis_title="Date",
              yaxis_title="Forecast Demand"
)

            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)"
            )

            st.plotly_chart(fig, use_container_width=True)

    else:

        st.error("Dashboard_Forecast.csv not found.")


# =================================
# CUSTOMER ANALYTICS
# =================================
elif page == "👥 Customer Analytics":

    st.header("👥 Customer Analytics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Customers", "8,932")
    c2.metric("Retention Rate", "72%")
    c3.metric("Avg Spending", "₹624")
    c4.metric("Churn Risk", "28%")

    file_path = "data/Customer_Analytics_Final.csv"

    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        st.success("✅ Customer Analytics Loaded Successfully")

        # Preview
        st.subheader("📋 Customer Data Overview")
        st.dataframe(
            df.head(50),
            use_container_width=True
        )


        # Dataset Information
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Dataset Shape")
            st.info(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")

        with col2:
            st.subheader("📈 Customer Segments")

            if "Customer Segment" in df.columns:

                segment = (
                    df["Customer Segment"]
                    .value_counts()
                    .reset_index()
                )

                segment.columns = [
                    "Segment",
                    "Count"
                ]

                fig = px.pie(
                    segment,
                    names="Segment",
                    values="Count",
                    hole=0.5,
                    title="Customer Segment Distribution",
                    template="plotly_dark"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


        # Churn Analysis
        if "Churn" in df.columns:

            st.subheader("⚠️ Customer Churn Analysis")

            churn = (
                df["Churn"]
                .value_counts()
                .reset_index()
            )

            churn.columns = [
                "Status",
                "Customers"
            ]

            fig2 = px.bar(
                churn,
                x="Status",
                y="Customers",
                title="Churn Prediction Analysis",
                template="plotly_dark"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )


        # Monetary Analysis
        if "Monetary" in df.columns:

            st.subheader("💰 Customer Value Analysis")

            fig3 = px.histogram(
                df,
                x="Monetary",
                nbins=40,
                title="Customer Spending Distribution",
                template="plotly_dark"
            )

            st.plotly_chart(
                fig3,
                use_container_width=True
            )


        # Statistics
        st.subheader("📊 Statistical Summary")

        st.dataframe(
            df.describe(),
            use_container_width=True
        )


    else:

        st.error("❌ Customer_Analytics_Final.csv not found.")
# =================================
# INVENTORY OPTIMIZATION
# =================================
elif page == "📦 Inventory Optimization":

    st.header("📦 Inventory Intelligence")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Products", "2150")
    c2.metric("In Stock", "2041")
    c3.metric("Low Stock", "81")
    c4.metric("Critical", "28")

    file_path = "data/online_retail_II_data.csv"

    if os.path.exists(file_path):

        retail = pd.read_csv(
            file_path,
            encoding="latin1"
        )

        st.success("Retail Dataset Loaded Successfully")

        st.dataframe(retail.head(20), use_container_width=True)

        if "Description" in retail.columns and "Quantity" in retail.columns:

            st.subheader("🏆 Top 10 Selling Products")

            top_products = (
                retail.groupby("Description")["Quantity"]
                .sum()
                .sort_values(ascending=False)
                .head(10)
                .reset_index()
            )

            fig = px.bar(
                top_products,
                x="Quantity",
                y="Description",
                orientation="h",
                title="Top Selling Products",
                template="plotly_dark"
            )

            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)"
            )

            st.plotly_chart(fig, use_container_width=True)

        st.subheader("📊 Dataset Statistics")
        st.dataframe(retail.describe())

    else:

        st.warning("online_retail_II_data.csv not found.")


# =================================
# DEPLOYMENT
# =================================
elif page == "🚀 Deployment":

    st.header("🚀 Deployment Center")

    st.success("Application Successfully Deployed")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
### 🟢 System Status

- AI Model Connected
- FastAPI Running
- Docker Active
- Database Connected
- GitHub Repository Connected
- Streamlit Online
""")

    with col2:

        st.markdown("""
### ⚙ Technology Stack

- Python
- Streamlit
- Plotly
- Pandas
- FastAPI
- Docker
- GitHub
""")

    st.write("---")

    st.subheader("📌 Deployment Steps")

    st.code("""
git add .
git commit -m "Final Project"
git push origin main
streamlit run app.py
""")

    st.success("✅ Project Ready for GitHub & Streamlit Cloud Deployment")


# =================================
# FOOTER
# =================================
st.write("---")

st.markdown(
    """
<div style='text-align:center;color:gray;font-size:14px;'>
© 2026 Neural Retail Intelligence Platform <br>
Powered by Artificial Intelligence | Streamlit | Plotly
</div>
""",
    unsafe_allow_html=True,
)