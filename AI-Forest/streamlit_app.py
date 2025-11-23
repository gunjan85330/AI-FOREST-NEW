import streamlit as st
import sys, os

# Ensure utils is importable
sys.path.append(os.path.abspath("./utils"))

st.set_page_config(
    page_title="AI Forest – Wildfire Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("AI FOREST – Wildfire Prediction & Simulation Dashboard")

st.sidebar.write("Use the sidebar to navigate through the pages.")


