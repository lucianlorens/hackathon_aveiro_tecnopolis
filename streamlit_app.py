import streamlit as st
from streamlit_folium import st_folium
import folium
from datetime import datetime, timedelta
from datetime import time as dt_time

st.title('Tecnopolis!')



# Criar slider de data 
reading_date = st.slider(
    "Data da Leitura",
    #min date
    #max date
    value=datetime(2020, 1, 1),
    format="DD/MMMM/YYYY")
st.write("Data selecionada:", reading_date)

min_datetime = datetime.strptime('00:00', '%H:%M')
max_datetime = datetime.strptime('23:45', '%H:%M')


# Criar slider de hora
reading_time = st.slider(
    "Horário da Leitura:",
    min_value=min_datetime,
    max_value=max_datetime,
    value=dt_time(9, 30),
    # value=(min_datetime, max_datetime),
    step=timedelta(minutes=15),
    format="hh:mm"
    )
st.write("Hora selecionada:", reading_time)

# Sample data (latitude, longitude, pollution value)
pollution_data = [(40.64435, -8.64066, 50),
                  (40.64435, -8.64066, 70),
                  # Add more data as needed
                 ]

# Function to create a map using Folium
def create_map(data):
    map = folium.Map(location=[40.64435, -8.64066], zoom_start=12)
    
    # add points according to filters. 

    for item in data:
        lat, lon, pollution_value = item
        folium.CircleMarker(
            location=(lat, lon),
            radius=pollution_value / 10,  # Adjust marker size based on pollution value
            color='red',
            fill=True,
            # vermelho para Monóxido de Carbono, Azul para Dióxido de Carbono,
            # verde para nitrogênio
            # pontilhado para poeira

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


# criar checkbox de quais dados vão ser processados ? 