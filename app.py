import streamlit as st

st.title("My First Streamlit Data App")

st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :smile:")
    st.balloons()