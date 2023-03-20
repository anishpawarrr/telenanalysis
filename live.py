import time

import streamlit as st

x=20
# st.<elem>("rfa")
s = st.title("Live info")
container1 = st.empty()
container2 = st.empty()
container3 = st.empty()
container4 = st.empty()
for i in range(x):
    time.sleep(0.3)
    container1.subheader(f"Speed -> {i} km/h")
    container2.subheader(f"RPM -> {i*143}")
    container3.subheader(f"Acceleration -> {i/7} G")
    container4.subheader(f"Brake -> False")














# import requests
# import smtplib
#
# apifile = open("api-key.txt", "r")
# apikey = apifile.read()
# apifile.close()
#
# home = input("home")
# work = input("work")
#
# url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imerial&"
#
# r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + apikey)
#
#
