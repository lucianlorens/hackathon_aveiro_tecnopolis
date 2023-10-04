import streamlit as st
from streamlit_folium import st_folium
import folium
import matplotlib.pyplot as plt
from datetime import *

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

m = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()], zoom_start=15)

# Function to assign marker color based on pollution level
def get_marker_color(pollution_value):
    if pollution_value <= 50:
        return 'green'
    elif pollution_value <= 100:
        return 'yellow'
    elif pollution_value <= 150:
        return 'orange'
    else:
        return 'red'

for index, row in data.iterrows():

    #add carbon dioxide
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5 * row['carbon_dioxide (ppm)'] / 100,  # Adjust marker size based on CO2 level
        # color=get_marker_color(row['carbon_dioxide (ppm)']),  # Color based on CO2 level
        color= 'blue ',  # Color based on CO2 level
        fill=True,
        # fill_color=get_marker_color(row['carbon_dioxide (ppm)']),
        fill_color='blue',
        fill_opacity=0.2
    ).add_to(m)

    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5 * row['carbon_monoxide (ug/m3)'] / 100,  # Adjust marker size based on CO2 level
        # color=get_marker_color(row['carbon_dioxide (ppm)']),  # Color based on CO2 level
        color= 'red ',  # Color based on CO2 level
        fill=True,
        # fill_color=get_marker_color(row['carbon_dioxide (ppm)']),
        fill_color='red',
        fill_opacity=0.2
    ).add_to(m)


    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5 * row['nitrogen_dioxide (ug/m3)'] / 100,  # Adjust marker size based on CO2 level
        # color=get_marker_color(row['carbon_dioxide (ppm)']),  # Color based on CO2 level
        color= 'green ',  # Color based on CO2 level
        fill=True,
        # fill_color=get_marker_color(row['carbon_dioxide (ppm)']),
        fill_color='green',
        fill_opacity=0.2
    ).add_to(m)

st_folium(m, width=800)


### BAR CHART 
# data = data.dropna(subset=['carbon_dioxide (ppm)', 'carbon_monoxide (ug/m3)', 'nitrogen_dioxide (ug/m3)'])

# # Select relevant columns
# pollution_data = data[['carbon_dioxide (ppm)', 'carbon_monoxide (ug/m3)', 'nitrogen_dioxide (ug/m3)']]

# # Calculate the mean pollution values
# mean_pollution = pollution_data.mean()

# # Create a bar graph
# plt.figure(figsize=(10, 6))
# mean_pollution.plot(kind='bar', color=['blue', 'green', 'red'])
# plt.title('Mean Pollution Levels')
# plt.xlabel('Pollutant')
# plt.ylabel('Mean Level')
# plt.xticks(rotation=0)
# # st.pyplot(mean_pollution)

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the data from the provided CSV
# # data = pd.read_csv('path/to/your/csv.csv')

# # Filter out rows with missing pollution data
# data = data.dropna(subset=['carbon_dioxide (ppm)', 'carbon_monoxide (ug/m3)', 'nitrogen_dioxide (ug/m3)'])

# # Select relevant columns
# pollution_data = data[['carbon_dioxide (ppm)', 'carbon_monoxide (ug/m3)', 'nitrogen_dioxide (ug/m3)']]

# # Calculate the mean pollution values
# mean_pollution = pollution_data.mean()

# # Display the bar graph using Streamlit
# st.bar_chart(mean_pollution)

# # Optionally, display the numerical values as well
# st.write('Mean Pollution Levels:')
# st.write(mean_pollution)

### create 3D map

# =====

import util.map_plotter as map_plotter
map_plotter.plot_3D_scatterplot(data)
map_plotter.heat_map(data)