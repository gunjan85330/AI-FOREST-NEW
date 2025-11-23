import joblib
import pandas as pd
import gdown
import os
import streamlit as st

PARQUET_URL = "https://drive.google.com/uc?id=1W2NwAwKVtz-jQcAZaKUAT4aDpUj-GNlv"
PARQUET_PATH = "master_with_lags.parquet"

@st.cache_resource
def load_dataset():
    if not os.path.exists(PARQUET_PATH):
        gdown.download(PARQUET_URL, PARQUET_PATH, quiet=False)
    return pd.read_parquet(PARQUET_PATH)

@st.cache_resource
def load_model():
    return joblib.load("models/baseline_risk_model_improved.pkl")


