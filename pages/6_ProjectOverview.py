import streamlit as st

st.title("Project Overview")

st.write("""
## AI-Forest: Wildfire Prediction & Simulation System

### Data Used
- NASA VIIRS FIRMS Fire Data (10 years)
- ERA5 Weather Reanalysis Data
- Synthetic data (VAE/GAN in early phases)

### ML Pipeline
1. Data Cleaning  
2. Weather-Fire Merging  
3. Lag Feature Creation  
4. Balancing  
5. XGBoost model training  
6. Streamlit Deployment  

This system predicts wildfire risk and simulates spread using weather + fire history.
""")


