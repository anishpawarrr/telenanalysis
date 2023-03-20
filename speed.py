import streamlit as st
import requests
import time

# Replace YOUR_API_KEY with your actual API key
api_key = "f851b05056bb8f7d47a8ca6a72823e7e"

# Look up the current location
response = requests.get(
    "https://api.openweathermap.org/geo/1.0/direct",
    params={
        "lat": "",
        "lon": "",
        "limit": 1,
        "appid": api_key
    }
)
location = response.json()["data"][0]

# Save the current location and time
previous_location = (location["lat"], location["lon"])
previous_time = time.time()

# Wait for a short period of time
time.sleep(10)

# Look up the current location again
response = requests.get(
    "https://api.openweathermap.org/geo/1.0/direct",
    params={
        "lat": "",
        "lon": "",
        "limit": 1,
        "appid": api_key
    }
)
location = response.json()["data"][0]

# Calculate the distance and time difference
current_location = (location["lat"], location["lon"])
distance = geodesic(previous_location, current_location).kilometers
time_difference = time.time() - previous_time

# Calculate the speed in kilometers per hour
speed_kph = distance / (time_difference / 3600)

print(f"Current speed: {speed_kph} km/h")