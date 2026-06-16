import streamlit as st
import pandas as pd
from pathlib import Path

@st.cache_data
def load_data():
    data_file = Path(__file__).parent / "TESLA.csv"
    df = pd.read_csv(data_file)

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    df["Daily Return"] = df["Adj Close"].pct_change()
    df["MA20"] = df["Adj Close"].rolling(window=20).mean()
    df["MA50"] = df["Adj Close"].rolling(window=50).mean()

    return df

df = load_data()
