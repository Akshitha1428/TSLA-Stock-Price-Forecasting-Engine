# ============================================================
# TESLA STOCK ANALYSIS DASHBOARD
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Tesla Stock Analysis Dashboard",
    page_icon="📈",
    layout="wide"
)

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    df = pd.read_csv("TSLA.csv")

    # Convert Date Column
    df["Date"] = pd.to_datetime(df["Date"])

    # Sort Values
    df = df.sort_values("Date")

    # Create Features
    df["Daily Return"] = df["Adj Close"].pct_change()
    df["MA20"] = df["Adj Close"].rolling(window=20).mean()
    df["MA50"] = df["Adj Close"].rolling(window=50).mean()

    return df

df = load_data()

# ============================================================
# TITLE
# ============================================================

st.title("📈 Tesla Stock Market Analysis Dashboard")
st.markdown("### Exploratory Data Analysis of Tesla (TSLA) Stock")

# ============================================================
# SIDEBAR FILTER
# ============================================================

st.sidebar.header("Filter Data")

start_date = st.sidebar.date_input(
    "Start Date",
    value=df["Date"].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    value=df["Date"].max()
)

filtered_df = df[
    (df["Date"] >= pd.to_datetime(start_date)) &
    (df["Date"] <= pd.to_datetime(end_date))
]

# ============================================================
# DATASET OVERVIEW
# ============================================================

st.subheader("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Rows", filtered_df.shape[0])
col2.metric("Total Columns", filtered_df.shape[1])
col3.metric(
    "Latest Price ($)",
    round(filtered_df["Adj Close"].iloc[-1], 2)
)

# ============================================================
# DATA PREVIEW
# ============================================================

st.subheader("📋 Dataset Preview")
st.dataframe(filtered_df.head())

# ============================================================
# STOCK PRICE TREND
# ============================================================

st.subheader("📈 Tesla Stock Price Trend")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    filtered_df["Date"],
    filtered_df["Adj Close"]
)

ax.set_title("Tesla Adjusted Closing Price")
ax.set_xlabel("Date")
ax.set_ylabel("Price ($)")

st.pyplot(fig)

# ============================================================
# MOVING AVERAGES
# ============================================================

st.subheader("📉 Moving Average Analysis")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    filtered_df["Date"],
    filtered_df["Adj Close"],
    label="Adj Close"
)

ax.plot(
    filtered_df["Date"],
    filtered_df["MA20"],
    label="20-Day Moving Average"
)

ax.plot(
    filtered_df["Date"],
    filtered_df["MA50"],
    label="50-Day Moving Average"
)

ax.set_title("Tesla Stock Price with Moving Averages")
ax.set_xlabel("Date")
ax.set_ylabel("Price ($)")
ax.legend()

st.pyplot(fig)

# ============================================================
# VOLUME ANALYSIS
# ============================================================

st.subheader("📊 Trading Volume Analysis")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    filtered_df["Date"],
    filtered_df["Volume"]
)

ax.set_title("Tesla Trading Volume")
ax.set_xlabel("Date")
ax.set_ylabel("Volume")

st.pyplot(fig)

# ============================================================
# DAILY RETURNS DISTRIBUTION
# ============================================================

st.subheader("📈 Daily Return Distribution")

fig, ax = plt.subplots(figsize=(10, 5))

ax.hist(
    filtered_df["Daily Return"].dropna(),
    bins=50
)

ax.set_title("Distribution of Daily Returns")
ax.set_xlabel("Daily Return")
ax.set_ylabel("Frequency")

st.pyplot(fig)

# ============================================================
# SUMMARY STATISTICS
# ============================================================

st.subheader("📋 Statistical Summary")

summary = filtered_df[
    ["Adj Close", "Volume", "Daily Return"]
].describe()

st.dataframe(summary)

# ============================================================
# KEY INSIGHTS
# ============================================================

st.subheader("🔍 Key Insights")

st.success(
    """
    • Tesla stock shows strong long-term growth.

    • Trading volume spikes during major market events.

    • Daily returns are centered around zero with high volatility.

    • Moving averages indicate bullish long-term trends.

    • Tesla remains a high-growth and high-risk stock.
    """
)

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.write("Created using Streamlit, Pandas and Matplotlib")
