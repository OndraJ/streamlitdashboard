import streamlit as st

st.title('moje prvni appka')

st.write('Prvni radky aplikace, kterou delam')

page = st.sidebar.radio('Select page', ['Test', 'Thomson'])

if page == 'Test':
    st.write('Prvni radky aplikace, kterou delam')
if page == 'Thomson':
    st.write('Thomson sampling')

