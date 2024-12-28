import streamlit as st
import time

st.set_page_config(page_title="Infinite Balloons", layout="wide")

st.title("Infinite Balloon Flow 🎈")

# Loop for infinite balloons
if "run" not in st.session_state:
    st.session_state.run = True

def stop_balloons():
    st.session_state.run = False

start_button = st.button("Start Balloons")
stop_button = st.button("Stop Balloons", on_click=stop_balloons)

if start_button:
    st.session_state.run = True

placeholder = st.empty()

while st.session_state.run:
    with placeholder:
        st.balloons()
    time.sleep(0.5)  # Adjust the delay for the flow speed

st.write("Click 'Start Balloons' to see infinite balloons, and 'Stop Balloons' to stop the flow.")
