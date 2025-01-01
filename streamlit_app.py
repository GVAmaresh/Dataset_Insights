import streamlit as st
from app import home_page, data_exploration_page
from chat import chat_page

st.set_page_config(page_title="Data Explorer", page_icon="📊", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'home'
if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'data_exploration':
    data_exploration_page()
elif st.session_state.page == 'chat':
    chat_page()
