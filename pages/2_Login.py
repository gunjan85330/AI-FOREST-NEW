import streamlit as st
from app.utils.auth import check_login

st.title(" Login to AI-Forest Dashboard")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if check_login(username, password):
        st.session_state["logged_in"] = True
        st.success("Login successful!")
        st.switch_page("app/Home.py")
    else:
        st.error("Invalid username or password")

