import streamlit as st
import pandas as pd
from utils.model_loader import load_dataset, load_model

st.title("Fire Risk Prediction")

df = load_dataset()
model = load_model()

lat = st.number_input("Latitude", value=29.7)
lon = st.number_input("Longitude", value=80.3)

if st.button("Predict Fire Risk"):

    dist = (df["lat"] - lat).abs() + (df["lon"] - lon).abs()
    idx = dist.idxmin()

    FEATURES = model.feature_names_in_
    sample = df.loc[idx, FEATURES].to_frame().T.fillna(0)

    prob = model.predict_proba(sample)[0][1]

    st.metric("Predicted Fire Risk", f"{prob:.4f}")


