import streamlit as st

def about():
    st.markdown(
        """
        <style>
        body {
            background-color: #e0f7fa;
        }
        .stImage > div {
            display: flex;
            justify-content: center;
        }
        h1 {
            color: #004d40;  /* Contrast color for the title */
        }
        .stButton button {
            background-color: #00796b;
            color: white;
            border-radius: 4px;
            padding: 10px 24px;
            font-size: 16px;
            transition-duration: 0.4s;
        }
        .stButton button:hover {
            background-color: #004d40;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write("# Welcome to World Tour")

    st.write("""
    ## Our Vision
    World Tour is your ultimate companion for discovering the best locations and establishments across the globe. Whether you're a traveler seeking new destinations or someone looking to explore hidden gems in your hometown, our app is designed to provide you with all the information you need. Our mission is to make exploration and discovery accessible to everyone, bringing the world closer to you.

    From popular tourist spots to lesser-known attractions, World Tour aims to cover it all with detailed descriptions, user reviews, and interactive maps. Join our community of explorers and embark on your next adventure with us!

    Your feedback is invaluable to us, and we continuously strive to improve our app based on your suggestions.
    """)

    st.image("https://via.placeholder.com/400x200", caption="Exploring the World", use_column_width=True)

    if st.button('Back to Main', key="back_to_main_about"):
        st.session_state.page = 'main'

if __name__ == "__main__":
    about()
