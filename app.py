import streamlit as st
from PIL import Image
import requests
import time
from streamlit_lottie import st_lottie

# Set page config
st.set_page_config(page_title="Happy Birthday Trapti!", page_icon="🎉", layout="centered")

# Set pink background
st.markdown("""
    <style>
    body {
        background-color: #ffe6f0;
    }
    .center {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Load Lottie animation
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

floating_hearts = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_ydo1amjm.json")

# Typing animation function
def type_writer(message):
    typed_text = ""
    placeholder = st.empty()
    for char in message:
        typed_text += char
        placeholder.markdown(f"<p style='font-size:22px; color:#d6336c;'>{typed_text}</p>", unsafe_allow_html=True)
        time.sleep(0.05)

# Intro page
def show_intro():
    st.markdown("<h1 style='text-align: center; color: #e75480;'>💝 Happy Birthday Trapti!</h1>", unsafe_allow_html=True)
    st.markdown("### 👋 A little surprise awaits you...")
    if st.button("💌 Tap to Open Your Letter"):
        st.session_state.page = "letter"

# Letter page
def show_letter_page():
    st.markdown("<h2 style='text-align: center; color: #ff4081;'>💖 A Letter for You 💖</h2>", unsafe_allow_html=True)

    # Image (optional)
    try:
        image = Image.open("your_image.png")  # Replace with your image filename
        st.image(image, caption="A Special Memory 💕", use_container_width=True)
    except:
        st.warning("Couldn't load image — make sure the filename is correct!")

    # Cake
    cake = """
           ,   ,   ,   ,   ,   ,
         {|||||||||||||||||||||}
         {~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~}
         {~ Happy Birthday!!! ~}
         {~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~}
         {|||||||||||||||||||||}
           \\___|___|___|___|___/
            🎂  🎂  🎂  🎂  🎂
    """
    st.markdown(f"<pre style='text-align: center;'>{cake}</pre>", unsafe_allow_html=True)

    # Lottie animation (hearts)
    if floating_hearts:
        st_lottie(floating_hearts, height=200)

    # Typing message
    if st.button("📜 Reveal Birthday Message"):
        type_writer("I may not be there in person, but my heart is with you 💖\nWishing you a day as beautiful and special as you are.\nLove you always!")

    # Balloons
    st.balloons()

# Session state to manage pages
if "page" not in st.session_state:
    st.session_state.page = "intro"

if st.session_state.page == "intro":
    show_intro()
elif st.session_state.page == "letter":
    show_letter_page()
