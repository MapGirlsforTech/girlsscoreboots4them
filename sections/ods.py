import streamlit as st
from streamlit_app import translate

# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text)

st.header(translate("ods"))

st.markdown("17 objetivos para transformar nuestro mundo")