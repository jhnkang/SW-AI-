import streamlit as st
from datetime import time

text = st.text_input("입력")
if st.button("Save") :
    st.session_state.text=text

st.markdown("---")

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

values = st.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)


appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

age = st.slider("How old are u")
st.write("i'm", age, "years old")
a = 3 # 선언 
st.write(a)
st.session_state.a = 3
st.write(st.session_state.a)
