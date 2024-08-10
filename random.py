import streamlit as st
from geopy.distance import distance
from geopy.point import Point
import random

def random_coordinate_within_radius(lat, lon, radius):
    # Generate a random distance within the radius
    random_distance = random.uniform(0, radius)
    
    # Generate a random bearing (angle in degrees)
    random_bearing = random.uniform(0, 360)
    
    # Calculate the destination point
    origin = Point(lat, lon)
    destination = distance(kilometers=random_distance).destination(origin, random_bearing)
    
    return destination.latitude, destination.longitude

# Streamlit UI
st.title('Random Places Suggestion')

# Input user location (latitude and longitude)
user_lat = st.number_input('Enter your latitude', value=37.7749)
user_lon = st.number_input('Enter your longitude', value=-122.4194)

# Input radius
radius = st.slider('Select radius (km)', min_value=1, max_value=100, value=10)

if st.button('Generate Random Place'):
    random_lat, random_lon = random_coordinate_within_radius(user_lat, user_lon, radius)
    st.write(f'Random place coordinates: Latitude: {random_lat}, Longitude: {random_lon}')
    
    # Provide a link to Google Maps with the coordinates
    google_maps_url = f"https://www.google.com/maps/search/?api=1&query={random_lat},{random_lon}"
    st.markdown(f"[View on Google Maps]({google_maps_url})")
