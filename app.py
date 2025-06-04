import streamlit as st
from PIL import Image
from datetime import datetime

# Page config
st.set_page_config(page_title="Happy Birthday Trapti!", page_icon="🎉")

# Apply custom CSS for background and styling
st.markdown("""
    <style>
        body {
            background-color: #ffe6f0;
        }
        .centered {
            text-align: center;
        }
        .letter-box {
            background-color: #fff0f5;
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
            box-shadow: 0 0 10px #ffb6c1;
        }
    </style>
""", unsafe_allow_html=True)

# Page state management
if "page" not in st.session_state:
    st.session_state.page = "intro"

# --- Intro Page ---
if st.session_state.page == "intro":
    st.markdown("<h1 class='centered' style='color: hotpink;'>Hi Trapti! 💕</h1>", unsafe_allow_html=True)
    st.markdown("<p class='centered'>Are you ready for your birthday surprise? 👀🎁</p>", unsafe_allow_html=True)
    if st.button("Yes, let's go! 🎉"):
        st.session_state.page = "main"
        st.experimental_rerun()

# --- Main Birthday Surprise Page ---
elif st.session_state.page == "main":
    # Optional image (replace with your own file name)
    try:
        image = Image.open("your_image_filename.png")  # Replace with your actual image file
        st.image(image, caption="Happy Birthday Trapti! 💖", use_container_width=True)
    except:
        st.warning("Image not found. Please add your image to the app folder.")

    # Countdown to June 5, 2025
    countdown_html = """
    <div style="text-align: center;">
      <h2 style="color: #ff4b4b;">🎉 Countdown to Your Birthday 🎉</h2>
      <div id="countdown" style="font-size: 30px; color: #ff66b2;"></div>
    </div>

    <script>
      const targetDate = new Date("2025-06-05T00:00:00").getTime();
      function updateCountdown() {
        const now = new Date().getTime();
        const distance = targetDate - now;

        if (distance < 0) {
          document.getElementById("countdown").innerHTML = "🎈 It's your birthday! 🎈";
          return;
        }

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById("countdown").innerHTML =
          days + "d " + hours + "h " + minutes + "m " + seconds + "s ";

        setTimeout(updateCountdown, 1000);
      }
      updateCountdown();
    </script>
    """
    st.markdown(countdown_html, unsafe_allow_html=True)

    # Main heading
    st.markdown("<h1 class='centered' style='color: pink;'>🎂 Happy Birthday Trapti! 🎈</h1>", unsafe_allow_html=True)

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

    # Letter (reveal on click)
    with st.expander("💌 Open Your Letter"):
        st.markdown("""
            <div class='letter-box'>
                <h3 style='text-align: center; color: deeppink;'>To Trapti,</h3>
                <p style='font-size: 18px; line-height: 1.6; text-align: center;'>
                Even though miles separate us, my heart celebrates you every single moment. 💖<br><br>
                On your special day, I wish you joy that lights up your world as brightly as you light up mine. 🌟<br><br>
                Thank you for being the most beautiful part of my life. This is just the beginning of many birthdays we'll share. 🎁<br><br>
                Love always,<br>
                <b>[Your Name]</b>
                </p>
            </div>
        """, unsafe_allow_html=True)

    # Birthday wishes
    st.markdown("### 💖 I may not be there in person, but my heart is with you.")
    st.markdown("### 🥰 Wishing you a day as beautiful and special as you are.")
    st.markdown("### 💌 Love you always!")

    # Balloons
    st.balloons()
