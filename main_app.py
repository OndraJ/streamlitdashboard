import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import pymysql

engine = create_engine("mysql+pymysql://data-student:u9AB6hWGsNkNcRDm@data.engeto.com:3306/data_academy_04_2022")
st.set_page_config(layout='wide')
st.title('Moje prvni appka')
st.write('...')
page = st.sidebar.radio('Select page', ['Mapa', 'Thomson'])

if page == 'Mapa':
    st.header('Mapa sdilenych kol v Edinburghu')

    col1, col2 = st.columns(2)
    from_hour_morning = col1.slider('Rano od', min_value=5, max_value=12)
    to_hour_morning   = col1.slider('Rano do', min_value=5, max_value=12)
    col1.write('Pocatecni stanice mezi {} a {}'.format(from_hour_morning, to_hour_morning))
    query_morning = '''SELECT 
               start_station_latitude as lat,
               start_station_longitude as lon
           FROM edinburgh_bikes
           WHERE hour(started_at) BETWEEN {} AND {}
           LIMIT 100000'''.format(from_hour_morning, to_hour_morning)

    df_morning = pd.read_sql(sql=query_morning, con = engine)
    col1.map(df_morning)

    from_hour_afternoon = col1.slider('Vecer od', min_value=12, max_value=20)
    to_hour_afternoon   = col1.slider('Vecer do', min_value=12, max_value=20)
    col2.write('Pocatecni stanice mezi {} a {}'.format(from_hour_afternoon, to_hour_afternoon))
    query_afternoon = '''SELECT 
               start_station_latitude as lat,
               start_station_longitude as lon
           FROM edinburgh_bikes
           WHERE hour(started_at) BETWEEN {} AND {}
           LIMIT 100000'''.format(from_hour_morning, to_hour_morning)

    df_afternoon = pd.read_sql(sql=query_afternoon, con = engine)
    col2.map(df_afternoon)
if page == 'Thomson':
    st.write('Thomson sampling')

