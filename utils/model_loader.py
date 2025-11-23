import joblib
import pandas as pd
import gdown
import os
import streamlit as st

PARQUET_URL = "https://drive.google.com/uc?id=1W2NwAwKVtz-jQcAZaKUAT4aDpUj-GNlv"
PARQUET_PATH = "master_with_lags.parquet"

NUMERIC_COLS = [
    'temp_c','rain_mm','wind_u','wind_v','pressure','wind','humidity','vpd',
    'fire_today_lag_1','fire_today_lag_3','fire_today_lag_7',
    'temp_c_lag_1','temp_c_lag_3','temp_c_lag_7',
    'rain_mm_lag_1','rain_mm_lag_3','rain_mm_lag_7',
    'humidity_lag_1','humidity_lag_3','humidity_lag_7',
    'vpd_lag_1','vpd_lag_3','vpd_lag_7',
    'wind_lag_1','wind_lag_3','wind_lag_7',
    'wind_u_lag_1','wind_u_lag_3','wind_u_lag_7',
    'wind_v_lag_1','wind_v_lag_3','wind_v_lag_7',
    'pressure_lag_1','pressure_lag_3','pressure_lag_7'
]

@st.cache_resource
def load_dataset():
    # Download file if needed
    if not os.path.exists(PARQUET_PATH):
        gdown.download(PARQUET_URL, PARQUET_PATH, quiet=False)

    df = pd.read_parquet(PARQUET_PATH)

    # Convert to numeric
    for col in NUMERIC_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.fillna(0)  # XGBoost safe
    return df

@st.cache_resource
def load_model():
    return joblib.load("models/baseline_risk_model_improved.pkl")



