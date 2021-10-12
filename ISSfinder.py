import urllib3
from urllib.request import urlopen
import json
from datetime import datetime
from geopy.geocoders import Nominatim

iss_data = urlopen("http://api.open-notify.org/iss-now.json") #Get data from API

iss_processed_data = json.loads(iss_data.read()) #Load data

geolocator = Nominatim(user_agent="Adam Khan's ISS Locator") #Variable for calling Reverse Geocoding API
latAndLong = iss_processed_data['iss_position']['latitude'] + ", " + iss_processed_data['iss_position']['longitude'] #Get Latitude and Longitude values for printing
latAndLong_no_space = iss_processed_data['iss_position']['latitude'] + "," + iss_processed_data['iss_position']['longitude'] #Latitude and Longitude for Google Maps link

maps_link = "https://www.google.com/maps/search/?api=1&query=" + latAndLong_no_space #Google Maps Link
try: #Try block works if there is an address (when ISS is over land)
    location = geolocator.reverse(latAndLong)
    print (location.address)
    print ("Latitude: ", iss_processed_data['iss_position']['latitude'])
    print ("Longitude: ", iss_processed_data['iss_position']['longitude'])
    print ("Check out the current location on Google Maps: ",  maps_link)
except: #Except block is called when address can not be found
    print ("The International Space Station is currently over the ocean")
    print ("Latitude: ", iss_processed_data['iss_position']['latitude'])
    print ("Longitude: ", iss_processed_data['iss_position']['longitude'])
    print ("Check out the current location on Google Maps: ",  maps_link)