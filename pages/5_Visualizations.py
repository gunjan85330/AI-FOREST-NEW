import streamlit as st
import pydeck as pdk
from utils.model_loader import load_dataset, load_model

st.title("Fire Risk Heatmap")

df = load_dataset()
model = load_model()

FEATURES = model.feature_names_in_
df["risk"] = model.predict_proba(df[FEATURES].fillna(0))[:,1]

layer = pdk.Layer(
    "HeatmapLayer",
    df,
    get_position=["lon", "lat"],
    get_weight="risk",
    radiusPixels=40,
)

view_state = pdk.ViewState(
    longitude=df["lon"].mean(),
    latitude=df["lat"].mean(),
    zoom=7,
)

st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state
))
