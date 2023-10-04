import streamlit as st
from streamlit_folium import st_folium
import folium
# from datetime import datetime, timedelta
from datetime import *
# from datetime import time as dt_time
import pandas as pd

st.title('Tecnopolis!')
st.write('This application displays pollution data on an interactive map.')
st.write('Watch the city breathe.')

min_datetime = datetime.strptime('00:00', '%H:%M')
max_datetime = datetime.strptime('23:45', '%H:%M')

min_date_day = datetime.strptime('08/03/2023', "%d/%m/%Y")
max_date_day = datetime.strptime('17/09/2023', "%d/%m/%Y")

# Criar slider de data 
reading_date = st.slider(
    "Data da Leitura",
    min_value=min_date_day,
    max_value=max_date_day,
    value= datetime(2023, 6 ,6),
    format="DD/MMMM/YYYY")

reading_date_formatted = reading_date.strftime("%d/%b/%Y")
st.write("Data selecionada:", reading_date_formatted)

min_datetime = datetime.strptime('00:00', '%H:%M')
max_datetime = datetime.strptime('23:45', '%H:%M')


# Criar slider de hora
reading_time = st.slider(
    "Horário da Leitura:",
    min_value=min_datetime,
    max_value=max_datetime,
    # value=dt_time(9, 30),
    value = datetime.strptime('16:20', '%H:%M'),
    # value = datetime.time('16:20', '%H:%M'),
    # value=(min_datetime, max_datetime),
    step=timedelta(minutes=15),
    format="HH:MM"
    )
reading_time_formatted = reading_time.strftime("%H:%M")
st.write("Hora selecionada:", reading_time_formatted )

st.write("data hora selecionada: ",reading_date_formatted,reading_time_formatted) 

# Sample data (latitude, longitude, pollution value)
pollution_data = [(40.64435, -8.64066, 50),
                  (40.64435, -8.64066, 70),
                  # Add more data as needed
                 ]

df = pd.read_csv('air_biblioteca_municipal.csv')

selected_datetime = reading_time + reading_date

time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())


filtered_df = df[(df['timestamp'] == selected_datetime)]

# Display the filtered DataFrame
st.write('### Filtered Data Based on Selected Time Range:')
st.write(filtered_df)

# Function to create a map using Folium



def create_map(data):
    map = folium.Map(location=[40.64435, -8.64066], zoom_start=12)
    
    # query the data from date

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



# Display the map
st.write('Pollution Map')
map = create_map(pollution_data)
# folium_static(map)  # Using folium_static to display Folium map in Streamlit
st_folium(map, width=800)


# criar checkbox de quais dados vão ser processados ? 