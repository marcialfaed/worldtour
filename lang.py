import streamlit as st

def lang():
    st.title('Language')
    st.write("Access language guides or translation tools for different regions.")

    language_options = ['English', 'Spanish', 'French', 'Chinese', 'Japanese']
    selected_language = st.selectbox('Select a Language', language_options)
    st.write(f"Selected Language: {selected_language}")

    translation_input = st.text_area("Enter text to translate")
    if st.button('Translate'):
        st.write("Translation feature is under development.")  # Placeholder for translation logic

    st.subheader("Language Guides")
    st.write("""
    - [English Guide](#)
    - [Spanish Guide](#)
    - [French Guide](#)
    - [Chinese Guide](#)
    - [Japanese Guide](#)
    """)

    if st.button('Back to Main', key="back_to_main_lang"):
        st.session_state.page = 'main'

if __name__ == "__main__":
    lang()
