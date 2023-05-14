import streamlit as st
import Linktoexcel



st.title("Welcome to this Section")

st.header("Here You are able to see your data")
st.header("Reload the page for getting data")
st.subheader("Click on this button to know Number of student registered")
reg = Linktoexcel.readregno()
name = Linktoexcel.readstudname()
sec = Linktoexcel.readsec()
uid=Linktoexcel.readcardno()
if(st.button("Get Registered Students")):
    for i in range(len(reg)):
        str=f"""Name -- {name[i]} , Registration No -- {reg[i]} , Section {sec[i]} """
        st.text(str)
st.subheader("Click To know the Issued Components")
if(st.button("Get Issued Components")):
    for i in range(len(uid)):
        comp=Linktoexcel.getcomponents(uid[i])
        if(len(comp)==1):
            continue
        else:
            comps=""
            for j in comp:
                comps=comps+str(j)+"\n"
            res=f"""The Name --> {name[i]}
Registration Number --> {reg[i]}
Issued Components --> 
{comps}"""
            st.text(res)