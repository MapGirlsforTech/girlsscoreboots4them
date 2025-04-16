import streamlit as st
from streamlit_app import translate
from utils import title, comment_with_avatar

# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text)

title(translate("introduce_yourself"))

st.header(translate("introduce_yourself"))

