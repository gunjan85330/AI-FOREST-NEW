import streamlit as st
import pydeck as pdk
from app.utils.model_loader import load_dataset, load_model

if "logged_in" not in st.session_state:
    st.switch_page("app/Login.py")

st.title(" Risk Heatmaps")

df = load_dataset()
model = load_model()

FEATURES = model.feature_names_in_

df["risk"] = model.predict_proba(df[FEATURES].fillna(0))[:,1]

st.subheader("Fire Risk Heatmap")

layer = pdk.Layer(
    "HeatmapLayer",
    df,
    get_position=["lon", "lat"],
    get_weight="risk",
    radiusPixels=40,
)

view = pdk.ViewState(
    latitude=df["lat"].mean(),
    longitude=df["lon"].mean(),
    zoom=7,
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view))

