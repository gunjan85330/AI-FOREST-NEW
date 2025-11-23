import streamlit as st

if "logged_in" not in st.session_state:
    st.switch_page("app/Login.py")

st.title(" Project Overview")

st.markdown("""
## AI-Forest: Wildfire Prediction & Simulation System

### **Data Sources**
- **NASA VIIRS FIRMS Data** (2014–2023)
- **ERA5 Weather Reanalysis Data** (Temperature, Wind, Humidity, Rainfall, VPD)
- **Synthetic Data Generation using VAE/GAN**

### **Key Features**
- Fire risk prediction using machine learning  
- Spread simulation using nearest-neighbor propagation  
- Interactive web dashboard  
- Heatmap visualizations  
- Multi-page design with login  

### **ML Pipeline**
1. Data Cleaning  
2. Weather–Fire Merging  
3. Lag Feature Engineering  
4. Balancing and Synthetic Data  
5. Model Training (XGBoost)  
6. Deployment (Streamlit Cloud)  
""")

