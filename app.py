# Set up the page
st.set_page_config(page_title="Happy Birthday Trapti!", page_icon="🎉")

# Display the image
image = Image.open("aef6e260-e320-43ae-881e-39803cce7cae.png")  # Replace with your image filename
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
from PIL import Image
import streamlit as st
import time
