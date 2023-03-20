import streamlit as st
from streamlit_option_menu import option_menu
import  pandas as pd
import plotly_express as px
import gspread as gs

def turnana():
    st.sidebar.title("Turning Analysis")
    selectlist = str(turnshitlist)
    # l=[]
    # i=0
    # while i<len(selectlist):
    #     stri = ""
    #     if selectlist[i] == "'":
    #         i += 1
    #         while selectlist[i] != "'":
    #             stri += selectlist[i]
    #             i += 1
    #         i+=1
    #         l.append(stri)
    #
    # s = st.sidebar.selectbox("Select sheet",l)
    # db = gshitturn.worksheet(s)
    # db = db.get_all_records()
    # db = pd.DataFrame(db)

    tlistsize = len(turnshitlist)
    turnl=[]
    for i in range(tlistsize):
        turnl.append(i)
    sh = st.sidebar.selectbox("Select sheet",turnl)
    shitdata = gshitturn.get_worksheet(sh)
    shitdata=shitdata.get_all_records()
    shitdata = pd.DataFrame(shitdata)
    ya = st.multiselect("Select laps",shitdata.columns)
    pl = px.line(shitdata,x="Turn",y=ya)
    st.plotly_chart(pl)


#json api
jsonfile = "datatele-366319-0d5fecc26b48.json"
#storing collected key in variable
gc = gs.service_account(jsonfile)
gshitlap = gc.open("Telemetry")
gshitturn = gc.open("Tele2")
lapshitlist = gshitlap.worksheets()
turnshitlist = gshitturn.worksheets()
st.set_page_config("Telemetry")
st.title("Computing Speed")
st.caption("Ignore title I had noting to write there")
opt = option_menu("Analysis", options=["Lap analysis","Turn analysis"])
if opt == "Turn analysis":
    turnana()