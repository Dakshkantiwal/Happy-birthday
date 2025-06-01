import streamlit as st
from PIL import Image

st.set_page_config(page_title="Happy Birthday Trapti!", page_icon="🎉")

# Pink background CSS
pink_bg_css = """
<style>
body {
    background-color: #ffb6c1;  /* light pink */
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
h1, h2, h3 {
    color: #800000;  /* dark red/maroon */
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

# Initialize session state
if 'page' not in st.session_state or st.session_state.page is None:
    st.session_state.page = 'intro'

if 'letter_opened' not in st.session_state:
    st.session_state.letter_opened = False

st.write("Current page:", st.session_state.page)  # debug

def show_intro():
    st.markdown("<h1>🎉 Welcome to your Birthday Surprise! 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Tap the button below to open your special birthday message!</h3>", unsafe_allow_html=True)
    if st.button("🎈 Open Surprise"):
        st.session_state.page = 'surprise'
        st.session_state.letter_opened = False  # reset letter state on new surprise open

def show_letter_intro():
    try:
        # Use your envelope image here; replace with your actual filename
        st.image("envelope.png", caption="A special letter for you 📬", use_container_width=True)
    except Exception:
        # Fallback if no image found
        st.markdown("<h2>📬 You have a special letter!</h2>", unsafe_allow_html=True)
    st.markdown("<h3>Click the button below to open your birthday letter!</h3>", unsafe_allow_html=True)
    if st.button("Open the Letter 🎉"):
        st.session_state.letter_opened = True

def show_letter_message():
    try:
        image = Image.open("aef6e260-e320-43ae-881e-39803cce7cae.png")
        st.image(image, caption="Happy Birthday Trapti! 💖", use_container_width=True)
    except Exception as e:
        st.error(f"Error loading image: {e}")

    st.markdown("<h1>🎂 Happy Birthday Trapti! 🎈</h1>", unsafe_allow_html=True)

    cake = '''
               ,   ,   ,   ,   ,   ,
             {|||||||||||||||||||||}
             {~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~}
             {~ Happy Birthday!!! ~}
             {~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~}
             {|||||||||||||||||||||}
               \\___|___|___|___|___/
                🎂  🎂  🎂  🎂  🎂
    '''
    st.markdown(f"<pre style='text-align: center; color: #800000;'>{cake}</pre>", unsafe_allow_html=True)

    st.markdown("<h3>💖 I may not be there in person, but my heart is with you.</h3>", unsafe_allow_html=True)
    st.markdown("<h3>🥰 Wishing you a day as beautiful and special as you are.</h3>", unsafe_allow_html=True)
    st.markdown("<h3>💌 Love you always!</h3>", unsafe_allow_html=True)

    st.balloons()

    if st.button("🔙 Back to Intro"):
        st.session_state.page = 'intro'
        st.session_state.letter_opened = False

def show_surprise():
    if not st.session_state.letter_opened:
        show_letter_intro()
    else:
        show_letter_message()

# Page router
if st.session_state.page == 'intro':
    show_intro()
else:
    show_surprise()
