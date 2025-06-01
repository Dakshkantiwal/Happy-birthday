import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Pink background CSS (keep from your previous code)
pink_bg_css = """
<style>
body {
    background-color: #ffb6c1;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
h1, h2, h3 {
    color: #800000;
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
    width: 200px;
    cursor: pointer;
}
div.stButton > button:hover {
    background-color: #ff1493;
}
</style>
"""
st.markdown(pink_bg_css, unsafe_allow_html=True)

# Function to load Lottie animation from URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load a cute envelope animation from lottiefiles.com
envelope_lottie = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")

if 'page' not in st.session_state or st.session_state.page is None:
    st.session_state.page = 'intro'

if 'letter_opened' not in st.session_state:
    st.session_state.letter_opened = False

def show_intro():
    st.markdown("<h1>🎉 Welcome to your Birthday Surprise! 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Tap the button below to open your special birthday message!</h3>", unsafe_allow_html=True)
    if st.button("🎈 Open Surprise"):
        st.session_state.page = 'surprise'
        st.session_state.letter_opened = False

def show_letter_intro():
    if envelope_lottie:
        st_lottie(envelope_lottie, height=300)
    else:
        st.markdown("<h2>📬 You have a special letter!</h2>", unsafe_allow_html=True)
    st.markdown("<h3>Click the button below to open your birthday letter!</h3>", unsafe_allow_html=True)
    if st.button("Open the Letter 🎉"):
        st.session_state.letter_opened = True

def show_letter_message():
    st.markdown("<h1>🎂 Happy Birthday Trapti! 🎈</h1>", unsafe_allow_html=True)
    st.markdown("💖 I may not be there in person, but my heart is with you.")
    st.markdown("🥰 Wishing you a day as beautiful and special as you are.")
    st.markdown("💌 Love you always!")
    st.balloons()
    if st.button("🔙 Back to Intro"):
        st.session_state.page = 'intro'
        st.session_state.letter_opened = False

def show_surprise():
    if not st.session_state.letter_opened:
        show_letter_intro()
    else:
        show_letter_message()

if st.session_state.page == 'intro':
    show_intro()
else:
    show_surprise()
