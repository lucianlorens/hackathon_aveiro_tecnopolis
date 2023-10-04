import pandas as pd
import pydeck as pdk
import streamlit as st

# Load the data from the provided CSV

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
