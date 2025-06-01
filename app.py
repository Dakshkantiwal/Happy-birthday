from PIL import Image
import streamlit as st
import time

st.set_page_config(page_title="Happy Birthday Trapti!", page_icon="🎉")

# Add the image here
image = Image.open("aef6e260-e320-43ae-881e-39803cce7cae.png")
st.image(image, caption="Happy Birthday Trapti! 💖", use_column_width=True)

st.markdown("<h1 style='text-align: center; color: pink;'>🎂 Happy Birthday Trapti! 🎈</h1>", unsafe_allow_html=True)
