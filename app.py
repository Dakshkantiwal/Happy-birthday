from PIL import Image
import streamlit as st
import time



# Set up the page
st.set_page_config(page_title="Happy Birthday Trapti!", page_icon="🎉")
audio_file = open('birthday_song.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')


# Display the image
image = Image.open("aef6e260-e320-43ae-881e-39803cce7cae.png")
st.image(image, caption="Happy Birthday Trapti! 💖", use_column_width=True)

# Main header
st.markdown("<h1 style='text-align: center; color: pink;'>🎂 Happy Birthday Trapti! 🎈</h1>", unsafe_allow_html=True)

# ASCII cake
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

# Birthday messages
st.markdown("### 💖 I may not be there in person, but my heart is with you.")
st.markdown("### 🥰 Wishing you a day as beautiful and special as you are.")
st.markdown("### 💌 Love you always!")

# Balloons animation
st.balloons()
