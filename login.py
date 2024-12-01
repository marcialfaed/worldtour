import streamlit as st

def login_page():
    st.title("Welcome to World Tour")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button('Login'):
        if username == 'user' and password == 'password':
            st.session_state.page = 'main'
        else:
            st.error('Invalid credentials!')
