import streamlit as st

with st.form("my_form"):
  user_input = st.text_input("Enter your E-Mail", "anyone@any.com")
  st.form_submit_button(label="Submit", icon="🔥")
