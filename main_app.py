import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import pymysql

engine = create_engine("mysql+pymysql://data-student:u9AB6hWGsNkNcRDm@data.engeto.com:3306/data_academy_04_2022")
st.
st.title('Moje prvni appka')
st.write('...')

page = st.sidebar.radio('Select page', ['Mapa', 'Thomson'])
st.set_page_config(layout='wide')
query_morning = '''SELECT 
               start_station_latitude as lat,
               start_station_longitude as lon
           FROM edinburgh_bikes
           WHERE hour(started_at) BETWEEN 6 AND 9
           LIMIT 100000'''

df_morning = pd.read_sql(sql=query_morning, con = engine)

query_afternoon = '''SELECT 
               start_station_latitude as lat,
               start_station_longitude as lon
           FROM edinburgh_bikes
           WHERE hour(started_at) BETWEEN 15 AND 19
           LIMIT 100000'''

df_afternoon = pd.read_sql(sql=query_afternoon, con = engine)
                           
                        


if page == 'Mapa':
    st.header('Mapa sdilenych kol v Edinburghu')

    col1, col2 = st.columns(2)
    
    col1.write('Sdilena kola mezi 6 a 9 rano')
    col1.map(df_morning)

    col2.write('Sdilena kola mezi 15 a 19 vecer')
    col2.map(df_afternoon)
if page == 'Thomson':
    st.write('Thomson sampling')

