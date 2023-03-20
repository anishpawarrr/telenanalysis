import requests
import socket

def get_location(ip_address):
  # Make a request to the geolocation service with the IP address
  response = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey=eca3fc42a0c34ee8b745ebc67042795a&ip={ip_address}')

  # Check if the request was successful
  if response.status_code == 200:
    # Get the location data from the response
    location_data = response.json()

    # Extract the location information from the data
    country = location_data.get('country_name')
    city = location_data.get('city')
    latitude = location_data.get('latitude')
    longitude = location_data.get('longitude')

    # Return the location information
    return (country, city, latitude, longitude)
  else:
    # Return None if the request was not successful
    return None
import subprocess

def get_ipconfig():
  # Run the ipconfig command and get the output
  output = subprocess.run(['ipconfig'], stdout=subprocess.PIPE).stdout.decode()
  return output

# Test the function
output = get_ipconfig()
print(output)
# Test the function with a sample IP address
ip_address = socket.gethostbyname('localhost')
print(ip_address)
location = get_location('2402:8100:303b:a424:3ff1:3b2c:9ad5:230e')
print(location)

l = "dfaf,rfref,refeaf"