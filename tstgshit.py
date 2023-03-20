import gspread as gs
import pandas as pd
import streamlit as st
import plotly_express as px

cred_file = "datatele-366319-0d5fecc26b48.json"
gc = gs.service_account(cred_file)
print(cred_file)
database = gc.open("Tele2")
# print(database)
#database.add_worksheet("tstws","100","20")
wsl = database.worksheets()

# l = []
# for i in range(len(wsl)):
#     s=wsl[i]
#     str=''
#     j=0
#     while j<len(s):
#         if s[j] == "'":
#             str+=s[j]
#             j+=1
#             while s[j] != "'":
#                 str+=s[j]
#                 j+=1
#             str+=s[j]
#             break
#     l.append(str)
#
# print(l)

# print(wsl)
# wsl = str(wsl)
# print(wsl)
# wsl+="0000"
# print(wsl)
# st.selectbox("WS",wsl)
# listsize = len(wsl)
# l=[]
# for i in range(listsize):
#     l.append(i)


wk = database.get_worksheet(1)
l = wk.get_all_records()
l=pd.DataFrame(l)
xa = st.selectbox("X",l.columns)
ya = st.multiselect("Y",l.columns)
l=px.line(l,x=xa,y=ya)
st.plotly_chart(l)
print(l)
# st.set_page_config("Telemetry")
st.title("Telemetry prototype")
st.header("Please dont share this link with anyone")
st.subheader("Time v/s Speed")
st.markdown("---")
xa=st.selectbox("Select X axis",options=l.columns)
ya=st.multiselect("Select y axis",options=l.columns)
pl=px.line(l,x=xa,y=ya)
st.plotly_chart(pl)

