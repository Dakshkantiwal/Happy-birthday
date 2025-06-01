--------------# Save this as app.py
import streamlit as st
import time

st.set_page_config(page_title="Happy Birthday Trapti!", page_icon="🎉")

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
-------------------------------------------------
