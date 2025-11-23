import streamlit as st

if "logged_in" not in st.session_state:
    st.switch_page("app/Login.py")

st.title(" AI FOREST — Wildfire Intelligence Dashboard")

st.markdown("""
### Welcome to the AI-Forest System  
Your all-in-one wildfire prediction, simulation, and analysis platform.
""")

col1, col2 = st.columns(2)

with col1:
    st.page_link("app/Prediction.py", label=" Fire Risk Prediction", icon="🔥")
    st.page_link("app/Simulation.py", label=" Wildfire Spread Simulator", icon="🔥")

with col2:
    st.page_link("app/Visualizations.py", label=" Risk Heatmaps", icon="🌍")
    st.page_link("app/ProjectOverview.py", label=" Project Overview", icon="📘")

st.divider()

st.page_link("app/Contributors.py", label=" Contributors", icon="👥")
st.page_link("app/Contact.py", label=" Contact", icon="📬")

