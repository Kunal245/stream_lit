import streamlit as st
from geopy.distance import geodesic
from geopy.point import Point
import random

def random_coordinate_within_radius(lat, lon, radius):
    # Convert radius from kilometers to meters
    radius_m = radius * 1000
    
    # Generate a random distance within the radius
    distance = random.uniform(0, radius_m)
    
    # Generate a random bearing (angle)
    bearing = random.uniform(0, 360)
    
    # Generate the new random point
    origin = Point(lat, lon)
    destination = geodesic(meters=distance).destination(origin, bearing)
    
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

