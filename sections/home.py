import streamlit as st
from utils import parrafo, buttonLink, title
from streamlit_app import translate

title(translate("home.title"))

# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text,unsafe_allow_html=True)

    # Crear un enlace con apariencia de botón para el Corrreo
    
buttonLink(translate("about_us.contact_us"),"mailto:mapgirlsfortech@gmail.com")

# Centrar la cita, pero alineada a la izquierda
parrafo(
    f"""
    <div style="display: flex; justify-content: center; width: 80%;">
        <blockquote style="text-align: left; font-style: italic; font-size: 1em; border-left: 5px solid #ccc; padding-left: 10px;">
             {translate("home.testimony")}
        </blockquote>
    </div>
    """
)

parrafo(translate("home.introduction"))
# Crear una columna para centrar la imagen
col1, col2, col3 = st.columns([1, 3, 1])  # Tres columnas, el centro tiene el triple de peso
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/LOGO_Boots_1500x1500.png", use_container_width=True)