import pandas as pd
import pydeck as pdk
import streamlit as st
import matplotlib as plt
import folium
from streamlit_folium import st_folium
import folium

def plot_interactivemap(data):

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





def plot_3D_scatterplot(data):
    # Filter out rows with missing pollution data
    data = data.dropna(subset=['carbon_dioxide (ppm)', 'carbon_monoxide (ug/m3)', 'nitrogen_dioxide (ug/m3)'])

    # Select relevant columns for the map
    map_data = data[['latitude', 'longitude', 'carbon_dioxide (ppm)', 'carbon_monoxide (ug/m3)', 'nitrogen_dioxide (ug/m3)']]

    # Create a Pydeck scatter plot
    scatter_plot = pdk.Layer(
        "ScatterplotLayer",
        map_data,
        get_position=['longitude', 'latitude'],
        get_radius=100,
        auto_highlight=True,
        get_fill_color='[200, pollution_value, 0]',
        get_line_color=[0, 0, 0],
        pickable=True
    )

    # Set the initial viewpoint for the map
    view_state = pdk.ViewState(
        latitude=map_data['latitude'].mean(),
        longitude=map_data['longitude'].mean(),
        zoom=13,
        pitch=45
    )

    # Create the Pydeck deck
    deck = pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=view_state,
        layers=[scatter_plot]
    )

    # Render the map using Streamlit
    st.pydeck_chart(deck)

def heat_map(data):
    import pandas as pd
    import pydeck as pdk
    import streamlit as st

    # Load the data from the provided CSV


    # Filter out rows with missing pollution data
    data = data.dropna(subset=['carbon_dioxide (ppm)', 'carbon_monoxide (ug/m3)', 'nitrogen_dioxide (ug/m3)'])

    # Select relevant columns for the map
    map_data = data[['latitude', 'longitude', 'carbon_dioxide (ppm)', 'carbon_monoxide (ug/m3)', 'nitrogen_dioxide (ug/m3)']]

    # Create a Pydeck heatmap layer
    heatmap_layer = pdk.Layer(
        "HeatmapLayer",
        map_data,
        get_position=['longitude', 'latitude'],
        aggregation='"MEAN"',
        get_weight='carbon_dioxide (ppm)'
    )

    # Set the initial viewpoint for the map
    view_state = pdk.ViewState(
        latitude=map_data['latitude'].mean(),
        longitude=map_data['longitude'].mean(),
        zoom=13,
        pitch=45
    )

    # Create the Pydeck deck
    deck = pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=view_state,
        layers=[heatmap_layer]
    )

    # Render the map using Streamlit
    st.pydeck_chart(deck)


def bar_chart(data):
    ## BAR CHART 
    data = data.dropna(subset=['carbon_dioxide (ppm)', 'carbon_monoxide (ug/m3)', 'nitrogen_dioxide (ug/m3)'])

    # Select relevant columns
    pollution_data = data[['carbon_dioxide (ppm)', 'carbon_monoxide (ug/m3)', 'nitrogen_dioxide (ug/m3)']]

    # Calculate the mean pollution values
    mean_pollution = pollution_data.mean()

    # Create a bar graph
    plt.figure(figsize=(10, 6))
    mean_pollution.plot(kind='bar', color=['blue', 'green', 'red'])
    plt.title('Mean Pollution Levels')
    plt.xlabel('Pollutant')
    plt.ylabel('Mean Level')
    plt.xticks(rotation=0)
    st.pyplot(mean_pollution)


    # Load the data from the provided CSV
    # data = pd.read_csv('path/to/your/csv.csv')

    # Filter out rows with missing pollution data
    data = data.dropna(subset=['carbon_dioxide (ppm)', 'carbon_monoxide (ug/m3)', 'nitrogen_dioxide (ug/m3)'])

    # Select relevant columns
    pollution_data = data[['carbon_dioxide (ppm)', 'carbon_monoxide (ug/m3)', 'nitrogen_dioxide (ug/m3)']]

    # Calculate the mean pollution values
    mean_pollution = pollution_data.mean()

    # Display the bar graph using Streamlit
    st.bar_chart(mean_pollution)

    # Optionally, display the numerical values as well
    st.write('Mean Pollution Levels:')
    st.write(mean_pollution)