import streamlit as st
import Linktoexcel
import ard_data

st.title("Welcome to Issuing Section")
st.header('Please Follow Along')
data=st.text_area(label="Scan Your Items",key="item")
stock_data=data.split("\n")
if st.button("Scan Your Card"):

    scan_card = ard_data.scanning_card()  # ard_data.scanning_card()
    uid = Linktoexcel.readcardno()
    reg = Linktoexcel.readregno()
    name = Linktoexcel.readstudname()
    sec = Linktoexcel.readsec()
    if scan_card != "Failure":
        st.markdown(f""" <span style='color:green'>Success</span>""",
                    unsafe_allow_html=True)
        idx = uid.index(scan_card)
        st.text(f"""Name -- {name[idx]}""")
        st.text(f"""Registration Number -- {reg[idx]}""")
        st.text(f"""Section -- {sec[idx]}""")
    else:
        st.markdown(f""" <span style='color:red'>Failure</span>""",
                    unsafe_allow_html=True)
    result = Linktoexcel.writecomponent(scan_card, stock_data)
    if(result=="Success"):
        st.markdown(f""" <span style='color:green'>Success</span>""",
                    unsafe_allow_html=True)
    else:
        st.markdown(f""" <span style='color:red'>Failure</span>""",
                    unsafe_allow_html=True)

