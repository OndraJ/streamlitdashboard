import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import pymysql



st.title('Moje prvni appka')
st.write('...')

page = st.sidebar.radio('Select page', ['Mapa', 'Thomson'])

query = '''SELECT 
               start_station_latitude as lat,
               start_station_longitude as lon
           FROM edinburgh_bikes
           LIMIT 20000'''
engine = create_engine("mysql+pymysql://data-student:u9AB6hWGsNkNcRDm@data.engeto.com:3306/data_academy_04_2022")

df = pd.read_sql(sql=query, con = engine)
                           
                        


if page == 'Mapa':
    st.write('Mapa sdilenych kol v Edinburghu')
    st.map(df)
if page == 'Thomson':
    st.write('Thomson sampling')

