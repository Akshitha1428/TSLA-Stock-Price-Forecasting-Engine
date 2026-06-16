import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
page_title="Tesla Stock Analysis Dashboard",
page_icon="📈",
layout="wide"
)

st.title("📈 Tesla Stock Analysis Dashboard")

@st.cache_data
def load_data():
file_path = Path(**file**).parent / "TESLA.csv"
df = pd.read_csv(file_path)
return df

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Column Names")
st.write(df.columns.tolist())

st.subheader("Dataset Shape")
st.write(f"Rows: {df.shape[0]}")
st.write(f"Columns: {df.shape[1]}")

st.subheader("Statistical Summary")
st.dataframe(df.describe())

st.success("Dataset loaded successfully!")

