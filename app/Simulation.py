import streamlit as st
from app.utils.model_loader import load_dataset, load_model
from app.utils.simulation import run_simulation

if "logged_in" not in st.session_state:
    st.switch_page("app/Login.py")

st.title("🌋 Wildfire Spread Simulation")

df = load_dataset()
model = load_model()

lat = st.number_input("Ignition Latitude", value=29.7)
lon = st.number_input("Ignition Longitude", value=80.3)
steps = st.slider("Steps", 1, 30, 10)
threshold = st.slider("Base Spread Threshold", 0.0, 1.0, 0.05)

if st.button("Run Simulation"):

    history, total = run_simulation(df, model, lat, lon, steps, threshold)

    st.success(f"Simulation complete — Total burned cells: {total}")

    for i, cells in enumerate(history):
        st.write(f"Step {i}: {len(cells)} cells burning")

