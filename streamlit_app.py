# from matplotlib import container
import folium
import streamlit as st
import pandas as pd

import util as util

st.title('Tecnopolis!')


# Dados de exemplo (latitude, longitude, valor de poluição)
dados_poluição = [(37.7749, -122.4194, 50),
                  (37.7749, -122.4194, 70),
                  # Adicione mais dados conforme necessário
                 ]

# Função para criar um mapa usando Folium
def criar_mapa(dados):
    mapa = folium.Map(location=[37.7749, -122.4194], zoom_start=12)
    
    for dado in dados:
        lat, lon, valor_poluição = dado
        folium.CircleMarker(
            location=(lat, lon),
            radius=valor_poluição / 10,  # Ajuste o tamanho do marcador com base no valor da poluição
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.6
        ).add_to(mapa)
    
    return mapa

# Título e descrição da aplicação
st.title('Visualização de Dados de Poluição')
st.write('Este aplicativo exibe dados de poluição em um mapa interativo.')

# Exibir o mapa
st.write('Mapa de Poluição')
mapa = criar_mapa(dados_poluição)

folium_static(mapa)  # Usando folium_static para exibir o mapa Folium no Streamlit
