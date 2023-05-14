import streamlit as st
import ard_data
import Linktoexcel

st.title("Please Fill all the details Carefully")
name = st.text_input(label="Name")
reg = st.text_input(label="Registration Number ")
sec = st.text_input(label="Section")
st.text("Scanning Will automatically upload your data")
if st.button("Scan Your Card"):
    st.text("Tap the card on rfid sensor")
    uid = str(ard_data.scanning_card())
    st.text(uid)
    result = Linktoexcel.writedata("Data/student_data.xlsx", name, sec, reg, uid)
    if result == "Success":
        st.markdown(f""" <span style='color:green'>Success</span>""",
                    unsafe_allow_html=True)
    if result == "Failure":
        st.markdown(f""" <span style='color:red'>Failure</span>""",
                    unsafe_allow_html=True)
