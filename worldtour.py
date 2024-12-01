import streamlit as st
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components
import requests

def main_page():
    def show_header():
        col1, col2, col3, col4 = st.columns([8, 1, 7, 3])
        with col1:
            st.markdown("<h1 style='text-align: left; margin: 0; color: #004d40;'>🌍World Tour</h1>", unsafe_allow_html=True)
        with col3:
            search_query = st.text_input("🔍 Search places", "")
        with col4:
            settings_icon = "⚙️"
            with st.expander(settings_icon):
                if st.button('🏠 Home'):
                    st.session_state.page = 'main'
                if st.button('👤 Profile'):
                    st.session_state.page = 'profile'
                if st.button('🔔 Notifications'):
                    st.session_state.page = 'notify'
                if st.button('🗣️ Language'):
                    st.session_state.page = 'lang'
                if st.button('🎉 Events'):
                    st.session_state.page = 'events'
                if st.button('ℹ️ About'):
                    st.session_state.page = 'about'
        return search_query

    st.markdown(
        """
        <style>
        body { background-color: #e0f7fa; }
        .stTextInput > div > div { display: flex; align-items: center; }
        .stTextInput > div > div > input { margin-bottom: 0; padding: 10px; border: none; border-bottom: 2px solid #4CAF50; border-radius: 4px; }
        .stTextInput > div > div > input:focus { border-bottom-color: #4CAF50; outline: none; box-shadow: 0 0 10px #4CAF50; }
        h1 { margin: 0 !important; color: #004d40; }
        .header { display: flex; flex-direction: column; width: 100%; margin: 0; padding: 0; }
        .map-container { height: calc(100vh - 130px); width: 100%; margin: 0; padding: 0; }
        .map { height: 100%; width: 100%; border: none; }
        .stMarkdown { margin: 0 !important; }
        .stButton { margin: 0 !important; }
        .st-expander-content { margin: 0 !important; padding: 0 !important; }
        </style>
        """,
        unsafe_allow_html=True
    )

    def get_marker_icon(category):
        icons = {
            'restaurant': 'cutlery',
            'park': 'tree',
            'museum': 'university',
            'default': 'map-marker'
        }
        return icons.get(category, 'default')

    def recommend_locations(preferences, locations):
        return [loc for loc in locations if loc['category'] in preferences]

    search_query = show_header()

    js_code = """
    <script>
    document.addEventListener('DOMContentLoaded', (event) => {
        document.querySelector('iframe').addEventListener('click', () => {
            alert('Map clicked!');
        });
    });
    </script>
    """
    components.html(js_code, height=0, width=0)

    # Define maximum zoom level to see all continents
    max_zoom_level = 1  # Adjust this value as needed

    # Initialize the map with the defined maximum zoom level
    map_object = folium.Map(location=[20.5937, 30.9629], zoom_start=max_zoom_level)

    if search_query:
        response = requests.get(f'http://127.0.0.1:5000/locations')
        if response.status_code == 200:
            locations = response.json()
            for loc in locations:
                if search_query.lower() in loc['name'].lower():
                    folium.Marker(
                        [loc['latitude'], loc['longitude']],
                        popup=loc['name'],
                        icon=folium.Icon(icon='info-sign')
                    ).add_to(map_object)
        else:
            st.error("Error fetching locations")

    # 1stWcity: Best cities with red icons
    top_places_1stWcity = [
        {"name": "Bangkok", "lat": 13.7563, "lon": 100.5018, "images": ["https://bigtourkrabi.com/include_designs/photoalbum/bangkok/muang_boran/bt_mb_001-6.jpg", "https://th.bing.com/th/id/OIP.80T5hZ5hh_Plgx9wbOa51AHaEK?rs=1&pid=ImgDetMain", "https://cdn.thecrazytourist.com/wp-content/uploads/2018/07/ccimage-shutterstock_193572950.jpg"]}
    ]

    for place in top_places_1stWcity:
        popup_html = f"""
        <h4>{place['name']}</h4>
        <img src="{place['images'][0]}" width="100%">
        <img src="{place['images'][1]}" width="100%">
        <img src="{place['images'][2]}" width="100%">
        """
        folium.Marker(
            [place['lat'], place['lon']],
            popup=folium.Popup(popup_html, max_width=300),
            icon=folium.Icon(icon='info-sign', color='red')
        ).add_to(map_object)

    # 2ndWcity: Additional cities with blue icons
    top_places_2ndWcity = [
        {"name": "Berlin", "lat": 52.5200, "lon": 13.4050},
        {"name": "Madrid", "lat": 40.4168, "lon": -3.7038},
        {"name": "Rome", "lat": 41.9028, "lon": 12.4964},
        {"name": "Beijing", "lat": 39.9042, "lon": 116.4074},
        {"name": "Moscow", "lat": 55.7558, "lon": 37.6173},
        {"name": "Buenos Aires", "lat": -34.6037, "lon": -58.3816},
        {"name": "Lagos", "lat": 6.5244, "lon": 3.3792},
        {"name": "Cape Town", "lat": -33.9249, "lon": 18.4241},
        {"name": "Sydney", "lat": -33.8688, "lon": 151.2093},
        {"name": "Los Angeles", "lat": 34.0522, "lon": -118.2437}
    ]

    for place in top_places_2ndWcity:
        folium.Marker(
            [place['lat'], place['lon']],
            popup=place['name'],
            icon=folium.Icon(icon='info-sign', color='blue', icon_size=(20, 33))  # Smaller size for blue icons
        ).add_to(map_object)

    st_folium(map_object, width=1500, height=1000)

if __name__ == "__main__":
    main_page()
