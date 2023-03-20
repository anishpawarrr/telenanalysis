import pandas as pd
import streamlit as st
import plotly_express as px

#datatele-366319-0d5fecc26b48.json
#pvtkey
#teletest@datatele-366319.iam.gserviceaccount.com
#email

x=[[1,2,3],[1,75,33],[1,2,3]]
y = pd.DataFrame(x)
st.write(y)
o=pd.read_csv("Records.csv")
st.write(o)
st.line_chart(o[["Speed","Time"]])
st.header("plo")
xv=st.selectbox("X axis", options = o.columns)
yv=st.multiselect("y axis", options = o.columns)
pl = px.line(o,y=yv,x=xv)
st.plotly_chart(pl)

# f=px.bar(y)
# st.write(f)