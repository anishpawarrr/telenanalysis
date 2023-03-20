import datetime

import gspread as gs
# t1 = datetime.datetime.now()
# t1 = t1.second
link = gs.service_account("datatele-366319-0d5fecc26b48.json")
sheet = link.open("Tele2")
file = sheet.get_worksheet(2)
import streamlit as st
t = st.text_input("enter text")
b = st.button("sub")
if b:
    t1 = datetime.datetime.now()
    file.update_cell(2, 1, t)
    t2 = datetime.datetime.now()
    # t2 = t2.second
    st.write(t1.second)
    st.write(t2.second)
    st.write(t2-t1)
    st.write(t2)
    st.write(type(t1))



