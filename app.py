import streamlit as st
from PIL import Image
import requests
import time
from streamlit_lottie import st_lottie

# --- Page Config ---
st.set_page_config(page_title="Happy Birthday Trapti!", page_icon="🎉", layout="centered")

# --- Background Styling ---
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

# --- Lottie Loader ---
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Typing Animation ---
def type_writer(message):
    typed_text = ""
    placeholder = st.empty()
    for char in message:
        typed_text += char
        placeholder.markdown(f"<p style='font-size:22px; color:#d6336c;'>{typed_text}</p>", unsafe_allow_html=True)
        time.sleep(0.05)

# --- Pages ---
def show_intro():
    st.markdown("<h1 style='text-align: center; color: #e75480;'>💝 Happy Birthday Trapti!</h1>", unsafe_allow_html=True)
    st.markdown("### 👋 A little surprise awaits you...")
    if st.button("💌 Tap to Open Your Letter"):
        st.session_state.page = "letter"

def show_letter_page():
    st.markdown("<h2 style='text-align: center; color: #ff4081;'>💖 A Letter for You 💖</h2>", unsafe_allow_html=True)

    # Optional image
    try:
        image = Image.open("trapti-smile.jpg")  # Replace with your image filename
        st.image(image, caption="A Special Memory 💕", use_container_width=True)
    except:
        st.warning("Image not found. Please check the filename.")

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

 

    # Typing message
    if st.button("📜 Reveal Birthday Message"):
        type_writer("I may not be there in person, but my heart is with you 💖\nWishing you a day as beautiful and special as you are.\nLove you always!")


    # Memory timeline
    st.markdown("---")
    st.markdown("### 🕰️ Our Little Timeline")
    st.markdown("✅ **7 june** – The spark started 📞")
    st.markdown("✅ **5 june 2023** – Still favorite day")
    st.markdown("✅ **Countless late-night chats** – Never enough 💬")
    st.markdown("✅ **5 june 2025: Your birthday!** – A perfect day to celebrate you 🎉")

    st.markdown("---")

    # Secret button to unlock hidden page
    if st.button("🤫 Psst... Don't click this!"):
        st.session_state.page = "secret"

def show_secret_page():
    st.markdown("<h2 style='text-align: center; color: #a020f0;'>🌟 Your Secret Surprise Page 🌟</h2>", unsafe_allow_html=True)
    st.success("Here's a little secret... You mean the world to me 🥺❤️")
    st.info("I can't wait to celebrate this day *in person* one day soon.")
    st.balloons()
    st.markdown("#### 🥰 Bonus Quote:")
    st.markdown("> *“You are my today and all of my tomorrows.”* — Leo Christopher")
    st.markdown("⬅️ Click the **back button** in your browser if you want to read the letter again!")

# --- Navigation ---
if "page" not in st.session_state:
    st.session_state.page = "intro"

if st.session_state.page == "intro":
    show_intro()
elif st.session_state.page == "letter":
    show_letter_page()
elif st.session_state.page == "secret":
    show_secret_page()
