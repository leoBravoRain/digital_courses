import streamlit as st

# title
st.title("Hello world!")

# add a checkbox (user interaction)
checkBox = st.checkbox("Display text")

if checkBox:

    st.text("Checkbox on!")


# add side checbox
checkboxSideBar = st.sidebar.checkbox("Display another text")

if checkboxSideBar:

    st.text("Checkbox ON from the sidebar")

    st.info(" This is the sidebar")