import pandas as pd
import numpy as np
import streamlit as st
import pydeck as pdk

city = st.text_input('区を教えてください')

df = pd.read_excel('UberEats加盟_20210405.xlsx')

df = df[df['市区郡名'] == city]

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=35.71,
        longitude=139.71,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=50,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=False,
            extruded=False,
         ),
    ],
))
