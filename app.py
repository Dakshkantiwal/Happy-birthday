import streamlit as st
from PIL import Image

st.set_page_config(page_title="Happy Birthday Trapti!", page_icon="🎉")

if 'page' not in st.session_state:
    st.session_state.page = 'intro'

def show_intro():
    st.markdown("<h1 style='text-align: center; color: pink;'>Welcome to your Birthday Surprise! 🎉</h1>", unsafe_allow_html=True)
    st.markdown("Click the button below to see your special birthday message and surprise!")
    if st.button('🎈 Open Surprise'):
        st.session_state.page = 'surprise'
        st.experimental_rerun()

def show_surprise():
    image = Image.open("aef6e260-e320-43ae-881e-39803cce7cae.png")
    st.image(image, caption="Happy Birthday Trapti! 💖", use_column_width=True)

    st.markdown("<h1 style='text-align: center; color: pink;'>🎂 Happy Birthday Trapti! 🎈</h1>", unsafe_allow_html=True)

    cake = """
               ,   ,   ,   ,   ,   ,
             {|||||||||||||||||||||}
             {~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~}
             {~ Happy Birthday!!! ~}
             {~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~}
             {|||||||||||||||||||||}
               \___|___|___|___|___/
                🎂  🎂  🎂  🎂  🎂
    """
    st.markdown(f"<pre style='text-align: center;'>{cake}</pre>", unsafe_allow_html=True)

    st.markdown("### 💖 I may not be there in person, but my heart is with you.")
    st.markdown("### 🥰 Wishing you a day as beautiful and special as you are.")
    st.markdown("### 💌 Love you always!")

    st.balloons()

    if st.button('🔙 Back to Intro'):
        st.session_state.page = 'intro'
        st.experimental_rerun()

if st.session_state.page == 'intro':
    show_intro()
elif st.session_state.page == 'surprise':
    show_surprise()
