import streamlit as st

if "logged_in" not in st.session_state:
    st.switch_page("app/Login.py")

st.title(" Contact Us")

st.markdown("""
For project queries or collaboration, you can reach us at:

**gunjan.singh_bsc.math23@gla.ac.in**
""")

