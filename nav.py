import streamlit as st
from login import login_page
from worldtour import main_page

st.set_page_config(page_title="World Tour", layout="wide")

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# Handle navigation based on session state
if st.session_state.page == 'login':
    login_page()
elif st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'profile':
    from prof import profile
    profile()
elif st.session_state.page == 'about':
    from about import about
    about()
elif st.session_state.page == 'lang':
    from lang import lang
    lang()
elif st.session_state.page == 'notify':
    from notify import notify
    notify()
elif st.session_state.page == 'events':
    from events import events
    events()
