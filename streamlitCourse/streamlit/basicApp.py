# Import required libraries
import streamlit as st

# 1) display title
st.title("Hello world!")

# 2) add interacvity
checkBox = st.checkbox("Display text")

# if checkbox
if checkBox:

    st.text("Checkbox on")


# 3) display sidebar
checkBoxSideBar = st.sidebar.checkbox("Display next text")

if checkBoxSideBar:

    st.text("Checkbox on from the sidebar")


    # 4) change text to info (different options to display data or text)
    st.info("Checkbox on from the sidebar")