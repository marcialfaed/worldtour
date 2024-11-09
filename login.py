import streamlit as st

st.set_page_config(page_title="Login", layout="centered")

# Simple Login page
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Welcome to World Tour")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button('Login'):
        if username == 'user' and password == 'password':  # Simple mock login
            st.session_state.logged_in = True
            st.success('Logged in successfully!')
            # Redirect to main page using an anchor (a session state variable)
            st.session_state.page = 'main'
            st.experimental_set_query_params(page="main")
            st.experimental_rerun()
        else:
            st.error('Invalid credentials!')

# Check if we need to redirect to the main page
if st.session_state.logged_in and st.session_state.get("page") == 'main':
    st.stop()
