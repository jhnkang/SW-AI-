import streamlit as st

if st.button("호출"):
  if "text" in st.session_state:
    st.write(st.session_state.text)
  else:
    st.write("Error")

st.markdown("---")

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"])

st.write("You selected:", options)