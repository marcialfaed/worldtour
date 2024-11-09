import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="World Tour", layout="wide")

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
            st.experimental_rerun()
        else:
            st.error('Invalid credentials!')
else:
    # Create columns for the header
    col1, col2, col3 = st.columns([3, 4, 1])  # Adjust the ratio to fit your needs

    # Title
    with col1:
        st.markdown("<h1 style='text-align: left; color: black;'>World Tour</h1>", unsafe_allow_html=True)

    # Search bar
    with col2:
        search_query = st.text_input("Search places", "")

    # Three-dot icon menu
    with col3:
        menu_icon = "⋮"  # Unicode for three dots
        with st.expander(menu_icon):
            st.write("1. About")
            st.write("2. Contact")
            st.write("3. Profile Settings")

    # Title and map will only be shown after login
    st.title("World Tour")

    # Create a simple map centered at a location (latitude, longitude)
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Centered on India

    # If a search query is entered, show a marker on the map
    if search_query:
        # For demonstration, let's just center the map to the location based on the search
        # In real-life applications, you would query a map API to get coordinates
        if search_query.lower() == "paris":
            folium.Marker([48.8566, 2.3522], popup="Paris").add_to(m)
        elif search_query.lower() == "new york":
            folium.Marker([40.7128, -74.0060], popup="New York").add_to(m)
        elif search_query.lower() == "tokyo":
            folium.Marker([35.6762, 139.6503], popup="Tokyo").add_to(m)
        else:
            st.warning("Location not found on the map. Try 'Paris', 'New York', or 'Tokyo'.")

    # Display the map in Streamlit
    st_folium(m, width=1000, height=1000)
