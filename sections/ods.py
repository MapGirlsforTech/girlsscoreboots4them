import streamlit as st
from streamlit_app import translate

# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text)

st.header(translate("ods"))

parrafo("**17 objetivos para transformar nuestro mundo**")
parrafo("En 2015, la ONU aprobó la Agenda 2030 sobre el Desarrollo Sostenible, una oportunidad para que los países y sus sociedades emprendieran un nuevo camino con el que mejorar la vida de todas las personas, sin dejar a nadie atrás.")
parrafo("La Agenda cuenta con 17 Objetivos de Desarrollo Sostenible, que establecen que la erradicación de la pobreza debe ir de la mano de estrategias que fomenten el crecimiento económico y abordan una serie de necesidades sociales como la educación, la sanidad, la protección social y las perspectivas de empleo, al tiempo que se combate el cambio climático y se protege el medio ambiente.")
