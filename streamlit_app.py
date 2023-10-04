import streamlit as st
from streamlit_folium import st_folium
import folium

from datetime import *

import pandas as pd

st.title('Tecnopolis!')
st.write('Watch the city breathe.')

min_date_day = datetime.strptime('08/03/2023', "%d/%m/%Y")
max_date_day = datetime.strptime('17/09/2023', "%d/%m/%Y")

min_datetime = datetime.strptime('00:00', '%H:%M')
max_datetime = datetime.strptime('23:45', '%H:%M')

# Criar slider de data 
reading_date = st.slider(
    "Data da Leitura",
    min_value=min_date_day,
    max_value=max_date_day,
    value= datetime(2023, 6 ,6),
    step=timedelta(days=1),
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
    value = datetime.strptime('15:15', '%H:%M'),
    step=timedelta(minutes=15),
    format="HH:MM"
    )
reading_time_formatted = reading_time.strftime("%H:%M")
st.write("Hora selecionada:", reading_time_formatted )

# st.write("data hora selecionada: ", reading_date_formatted,reading_time_formatted) 
string_date = str(reading_date_formatted + " " +reading_time_formatted)
parsed_date = datetime.strptime(string_date, "%d/%b/%Y %H:%M")
selected_datetime = parsed_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")


# Sample data (latitude, longitude, pollution value)
pollution_data = [(40.640869210794435, -8.654079269311524, 50),
                  (40.638073976301875, -8.643864619150884, 70),
                  # Add more data as needed
                 ]

df_gold = pd.read_csv('df_gold.csv')
# filtered_df = df_gold[ (df_gold['timestamp'] == selected_datetime) ]

def find_rows_by_timestamp(df, timestamp):
    """
    Find all rows in the DataFrame that match the given timestamp.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to search.
        timestamp (str): The timestamp to search for (in the format 'YYYY-MM-DDTHH:MM:SS').
    
    Returns:
        pd.DataFrame: DataFrame containing rows that match the timestamp.
    """
    # Convert timestamp to datetime object
    # timestamp = pd.to_datetime(timestamp)
    
    # Filter the DataFrame based on the timestamp
    filtered_df = df[df['timestamp'] == timestamp]
    
    return filtered_df

filtered_df = find_rows_by_timestamp(df_gold, selected_datetime)



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
            radius = pollution_value / 10,  # Adjust marker size based on pollution value
            color = 'red',
            fill = True,
            # vermelho para Monóxido de Carbono, Azul para Dióxido de Carbono,
            # verde para nitrogênio
            # pontilhado para poeira

            fill_color='red', 
            fill_opacity=0.3

        ).add_to(map)
    
    # if mono_carb check
    # if diox_carb check
    # if diox_nitro check

    return map



### create 3D map

# Display the map
st.write('Pollution Map')
map = create_map(pollution_data)
# folium_static(map)  # Using folium_static to display Folium map in Streamlit
st_folium(map, width=800)


import pandas as pd
import pydeck as pdk
import streamlit as st

# Load the data from the provided CSV
data = pd.read_csv('df_gold.csv')

# Filter out rows with missing latitude or longitude
data = data.dropna(subset=['latitude', 'longitude'])

# Create a Pydeck heatmap layer
heatmap_layer = pdk.Layer(
    "HeatmapLayer",
    data,
    get_position=['longitude', 'latitude'],
    aggregation='"MEAN"',
    get_weight='carbon_dioxide (ppm)'
)

# Set the initial viewpoint for the map
view_state = pdk.ViewState(
    latitude=data['latitude'].mean(),
    longitude=data['longitude'].mean(),
    zoom=11,
    pitch=0
)

# Create the Pydeck deck
deck = pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=view_state,
    layers=[heatmap_layer]
)

# Render the map using Streamlit
st.pydeck_chart(deck)
