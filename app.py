from cProfile import label
import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd

st.set_page_config(layout="wide")

#load and prepare the data.
sheet_url = "https://docs.google.com/spreadsheets/d/1xaMnBFk-N6BxVX9kv_t2LMrezkMFizMQIjsJFRGS7SY/edit#gid=1341667998"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
#csvpath = r'dataBase.csv'
df = pd.read_csv(url_1)
df = df[['Latitude','Longitude','City','Desc','Image','Icon']]
df['Desc'] = df['Desc'].fillna('')

st.header ("Produtores do Maranhão")
        
farmers_markets = folium.Map(location=[-4.803743785485214, -45.16014604033804],
tiles = 'OpenStreetMap',
zoom_start=6)
for index, row in df.iterrows():
        
        text = f"""
        <h4><b> {row.City} </b></h4> 
        <p style="text-align:center;">
        <img src="{row.Image}" alt="Farmer's Market Photo" style = "width:200px;height:200px;"> 
        
        <br>
        <p style="text-align:center;color:black">
        {row.Desc}<br>
        </p>
            """
        folium.Marker(
            [row['Latitude'],row['Longitude']],
            icon = folium.features.CustomIcon(row['Icon'],icon_size=(40, 40)),
            popup = folium.Popup(text, max_width = 260, height= 260),
            tooltip = row['City']).add_to(farmers_markets)
        

folium_static(farmers_markets, width=1400, height= 700)


### fonte

photo, info = st.columns([0.2, 1])

with photo:
    image = 'imgs/bottons.png'
    st.image(image, width=200,)

with info:
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.write('powered by TECAAP')
    st.write('Laboratório de Tecnologia Aplicada a Aquicultura e Pesca.')
    st.write('Instagram : [TECAAP](https://www.instagram.com/lab.tecaap/)')
