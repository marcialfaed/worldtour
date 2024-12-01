import streamlit as st

def events():
    st.title('Events')
    st.write("Check out events happening in different locations.")

    event_categories = ['Music', 'Art', 'Technology', 'Sports', 'Education']
    selected_category = st.selectbox('Select Event Category', event_categories)
    st.write(f"Selected Category: {selected_category}")

    locations = ['New York', 'London', 'Tokyo', 'Sydney', 'Baguio']
    selected_location = st.selectbox('Select Location', locations)
    st.write(f"Selected Location: {selected_location}")

    st.subheader("Upcoming Events")
    st.write("""
    - **Music Festival** - March 20, 2024
    - **Art Expo** - April 15, 2024
    - **Tech Conference** - May 10, 2024
    """)

    if st.button('Back to Main', key="back_to_main_events"):
        st.session_state.page = 'main'

if __name__ == "__main__":
    events()
