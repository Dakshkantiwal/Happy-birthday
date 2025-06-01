from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Set up the page
st.set_page_config(page_title="Happy Birthday Trapti!", page_icon="🎉")

# Background styling
st.markdown("""
    <style>
    body {
        background-color: #ffe6f0;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    h1, h2, h3 {
        color: #c71585;
        text-align: center;
        text-shadow: 1px 1px 2px #fff;
    }
    div.stButton > button {
        background-color: #ff69b4;
        color: white;
        font-size: 20px;
        border-radius: 10px;
        padding: 10px 24px;
        margin: 0 auto;
        display: block;
        width: 220px;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background-color: #ff1493;
    }
    </style>
""", unsafe_allow_html=True)

# Load Lottie animation
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

envelope_lottie = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")  # Cute envelope

# Session state
if 'page' not in st.session_state:
    st.session_state.page = 'intro'
if 'letter_opened' not in st.session_state:
    st.session_state.letter_opened = False

# Intro page
def show_intro():
    st.markdown("<h1>🎉 Welcome to Your Birthday Surprise, Trapti! 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Click below to open your special message 💌</h3>", unsafe_allow_html=True)
    if st.button("✨ Open Surprise ✨"):
        st.session_state.page = 'letter'

# Letter page
def show_letter_page():
    st.markdown("<h2>📬 You've got a letter!</h2>", unsafe_allow_html=True)

    if envelope_lottie:
        st_lottie(envelope_lottie, height=300)
    else:
        envelope = Image.open("your_envelope_image.png")
        st.image(envelope, caption="Tap to open your birthday letter 💌", use_container_width=True)

    if not st.session_state.letter_opened:
        if st.button("💌 Open the Letter"):
            st.session_state.letter_opened = True

    if st.session_state.letter_opened:
        st.markdown("<h1>🎂 Happy Birthday Trapti! 🎈</h1>", unsafe_allow_html=True)
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
        st.markdown("💖 I may not be there in person, but my heart is with you.")
        st.markdown("🥰 Wishing you a day as beautiful and special as you are.")
        st.markdown("💌 Love you always!")
        st.balloons()

        if st.button("🔙 Back to Home"):
            st.session_state.page = 'intro'
            st.session_state.letter_opened = False

# Page routing
if st.session_state.page == 'intro':
    show_intro()
elif st.session_state.page == 'letter':
    show_letter_page()
