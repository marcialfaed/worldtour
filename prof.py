import streamlit as st

def profile():
    st.markdown(
        """
        <style>
        body {
            background-color: #e0f7fa;
        }
        .stTextInput > div > div {
            display: flex;
            align-items: center;
        }
        .stTextInput > div > div > input {
            margin-bottom: 0;
            padding: 10px;
            border: none;
            border-bottom: 2px solid #4CAF50;
            border-radius: 4px;
        }
        .stTextInput > div > div > input:focus {
            border-bottom-color: #4CAF50;
            outline: none;
            box-shadow: 0 0 10px #4CAF50;
        }
        .stImage > div {
            display: flex;
            justify-content: center;
        }
        h1 {
            color: #004d40;
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

    st.title("Profile Page")

    st.write("## Sign Up")
    with st.form("signup_form_unique_1"):
        col1, col2 = st.columns([1, 3])
        with col1:
            profile_picture = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
        with col2:
            new_username = st.text_input("New Username")
            new_password = st.text_input("New Password", type='password')
            new_email = st.text_input("Email")
            preferences = st.multiselect(
                "Preferences (Select categories you are interested in)",
                ["Restaurants", "Parks", "Museums", "Historical Sites", "Shopping Centers"]
            )
        if st.form_submit_button("Sign Up"):
            # Add code to handle sign up (e.g., save to database)
            st.success("Signed up successfully!")

    st.write("## Log In")
    col1, col2 = st.columns(2)
    with col1:
        username = st.text_input("Username", key="login_username")
    with col2:
        password = st.text_input("Password", type='password', key="login_password")
    if st.button("Log In", key="login_button"):
        # Add code to handle log in (e.g., check credentials)
        if username == "user" and password == "password":
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials!")

    if st.button('Back to Main', key="back_to_main_profile"):
        st.session_state.page = 'main'

if __name__ == "__main__":
    profile()
