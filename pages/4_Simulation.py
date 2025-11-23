import streamlit as st
from utils.model_loader import load_dataset, load_model
from utils.simulation import run_simulation

st.title("Wildfire Spread Simulation")

df = load_dataset()
model = load_model()

lat = st.number_input("Ignition Latitude", value=29.7)
lon = st.number_input("Ignition Longitude", value=80.3)
steps = st.slider("Steps", 1, 30, 10)
threshold = st.slider("Spread Threshold", 0.0, 1.0, 0.05)

if st.button("Run Simulation"):
    history, total = run_simulation(df, model, lat, lon, steps, threshold)

    st.success(f"Simulation complete – Burned cells: {total}")

    for i, cells in enumerate(history):
        st.write(f"Step {i}: {len(cells)} burning cells")


