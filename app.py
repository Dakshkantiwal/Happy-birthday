import streamlit as st
from PIL import Image

st.set_page_config(page_title="Happy Birthday Trapti!", page_icon="🎉")

# Background style
st.markdown("""
<style>
body {
  background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
  font-family: 'Brush Script MT', cursive;
}
h1, h2, h3 {
  color: #fff;
  text-shadow: 2px 2px 4px #000000;
}
</style>
""", unsafe_allow_html=True)

# Page content
col1, col2 = st.columns([1, 1])

with col1:
    image = Image.open("aef6e260-e320-43ae-881e-39803cce7cae.png")
    st.image(image, caption="Happy Birthday Trapti! 💖", use_container_width=True)


with col2:
    st.markdown("<h1>🎂 Happy Birthday Trapti! 🎈</h1>", unsafe_allow_html=True)
    st.markdown("""
    <h3>💖 Though miles apart, my heart is with you.</h3>
    <h3>🥰 Wishing you joy, love, and laughter today and always.</h3>
    <h3>💌 Love you endlessly!</h3>
    """, unsafe_allow_html=True)

st.balloons()
