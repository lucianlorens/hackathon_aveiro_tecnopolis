import streamlit as st
from streamlit_folium import st_folium
import folium
import matplotlib.pyplot as plt
from datetime import *

import util.map_plotter as map_plotter

import pandas as pd

st.title('Tecnopolis')
st.subheader('Watch the city breathe.')

# Criar slider de data 
min_date_day = datetime.strptime('08/03/2023', "%d/%m/%Y")
max_date_day = datetime.strptime('17/09/2023', "%d/%m/%Y")
reading_date = st.slider(
    "Data da Leitura",
    min_value=min_date_day,
    max_value=max_date_day,
    value= datetime(2023, 6 ,6),
    step=timedelta(days=1),
    format="DD/MMMM/YYYY")

reading_date_formatted = reading_date.strftime("%d/%b/%Y")
st.write("Data selecionada:", reading_date_formatted)

# Criar slider de hora
min_datetime = datetime.strptime('00:00', '%H:%M')
max_datetime = datetime.strptime('23:45', '%H:%M')

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

df_gold = pd.read_csv('df_gold.csv')

def find_rows_by_timestamp(df, timestamp):
    filtered_df = df[df['timestamp'] == timestamp]
    
    return filtered_df

filtered_df = find_rows_by_timestamp(df_gold, selected_datetime)

# Function to create a map using Folium
data = filtered_df


map_plotter.plot_interactivemap(data)
map_plotter.plot_3D_scatterplot(data)
map_plotter.heat_map(data)
map_plotter.bar_chart(data)
