import streamlit as st
from utils.auth import check_login

st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if check_login(username, password):
        st.success("Login successful!")
    else:
        st.error("Invalid username or password")


