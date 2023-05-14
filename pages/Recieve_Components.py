import streamlit as st
import Linktoexcel
import ard_data

st.title("Welcome To Recieving Section")
st.header("Please Follow Along")
data=st.text_area(label="Scan Your Items",key="item")
stock_data=data.split("\n")
stock_data=stock_data[:-1]
if(st.button("Scan Card")):
    scan_card=ard_data.scanning_card()
    result=Linktoexcel.getcomponents(scan_card)
    result.sort()
    stock_data.sort()
    if(stock_data==result):
        Linktoexcel.delete(scan_card)
        st.markdown(f""" <span style='color:green'>Success</span>""",
                    unsafe_allow_html=True)




