#here you can test streamlit

import streamlit as st

# Title and text
st.title("Hello from Streamlit!")
st.write("This is a simple Streamlit app.")

# Input widget
name = st.text_input("Enter your name:")

# Display result
if name:
    st.write(f"Hello, {name}!")

# Button
if st.button("Click Me!"):
    st.write("Button clicked!")
