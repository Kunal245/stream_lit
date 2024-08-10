import streamlit as st
from geopy.distance import geodesic
import random

def generate_random_coordinates(lat, lon, radius):
  """Generates random coordinates within a given radius."""

  # Convert radius from kilometers to degrees
  radius_in_degrees = radius / 111000.0

  # Generate random angles
  u = random.uniform(0, 1)
  v = random.uniform(0, 1)

  # Convert to polar coordinates
  w = radius_in_degrees * math.sqrt(u)
  t = 2 * math.pi * v

  # Convert to Cartesian coordinates
  x = w * math.cos(t)
  y = w * math.sin(t)

  # Adjust for the shrinking of the earth at the poles
  x = x / math.cos(lat)

  # Calculate new latitude and longitude
  new_lat = lat + y
  new_lon = lon + x

  return new_lat, new_lon

def main():
  st.title("Random Place Generator")

  # Get user's location (replace with actual location retrieval)
  user_lat = 37.7749
  user_lon = -122.4194

  # Get radius from user
  radius = st.number_input("Radius (kilometers)", min_value=0.1, value=1.0)

  if st.button("Generate Random Place"):
    random_lat, random_lon = generate_random_coordinates(user_lat, user_lon, radius)
    st.write(f"Random Coordinates: ({random_lat}, {random_lon})")

if __name__ == "__main__":
  main()
