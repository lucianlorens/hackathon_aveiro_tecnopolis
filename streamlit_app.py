import streamlit as st
from streamlit_folium import st_folium
import folium


st.title('Tecnopolis!')


# Sample data (latitude, longitude, pollution value)
pollution_data = [(40.64435, -8.64066, 50),
                  (40.64435, -8.64066, 70),
                  # Add more data as needed
                 ]

# Function to create a map using Folium
def create_map(data):
    map = folium.Map(location=[40.64435, -8.64066], zoom_start=12)
    
    for item in data:
        lat, lon, pollution_value = item
        folium.CircleMarker(
            location=(lat, lon),
            radius=pollution_value / 10,  # Adjust marker size based on pollution value
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.6
        ).add_to(map)
    
    return map

# Title and description of the application
st.title('Pollution Data Visualization')
st.write('This application displays pollution data on an interactive map.')

# Display the map
st.write('Pollution Map')
map = create_map(pollution_data)
# folium_static(map)  # Using folium_static to display Folium map in Streamlit
st_folium(map, width=800)

