import streamlit as st

def notify():
    st.title('Notifications')
    st.write("Stay updated with the latest alerts and updates.")
    # Add code to display notifications
    
    if st.button('Back to Main', key="back_to_main_about"):
        st.session_state.page = 'main'

if __name__ == "__main__":
    notify()
