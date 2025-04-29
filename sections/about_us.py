import streamlit as st
from streamlit_app import translate
from utils import title, buttonLink

# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text,unsafe_allow_html=True)


title(translate("about_us.title"))

# Crear un enlace con apariencia de botón para el Corrreo
buttonLink(translate("about_us.contact_us"), "mailto:mapgirlsfortech@gmail.com" )

title("MAP Girls for Tech")

# Texto: Presentación del equipo

parrafo(translate("about_us.presentation"))

# Crear una columna para centrar la imagen
# Tres columnas, el centro tiene el triple de peso
col1, col2, col3 = st.columns([1, 3, 1])
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/MAP_WEB.png", use_container_width=True)

parrafo(translate("about_us.information"))

# Crear un enlace con apariencia de botón para ir a Technovation
buttonLink(translate("about_us.program_link"), "https://technovationchallenge.org/" )

parrafo(" ")
parrafo(" ")

parrafo(translate("about_us.problematic"))

# Centrar la cita, pero alineada a la izquierda
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; width: 80%;">
        <blockquote style="text-align: left; font-style: italic; font-size: 1em; border-left: 5px solid #ccc; padding-left: 10px;">
        {translate("about_us.quote")}
        </blockquote>
    </div>
    """,
    unsafe_allow_html=True
)

parrafo(" ")

parrafo(translate("about_us.summary"))

parrafo(translate("home.questionnaire"))

parrafo(f"<h4 style='text-align: center;'>{translate('home.needYourHelp')}</h4>")

parrafo(f"<h5 style='text-align: center;'>{translate('home.questionnaireRequest')}</h5>")

parrafo(f"<h5 style='text-align: center;'>{translate('home.thankYou')}</h5>")

# Crear un enlace con apariencia de botón
buttonLink(translate("home.questionnaireLink"), "https://forms.gle/ti3ky6UAXbHjB2a87")

parrafo(" ")

# Crear una columna para centrar la imagen
# Tres columnas, el centro tiene el triple de peso
col1, col2, col3 = st.columns([1, 3, 1])
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/Logo-Circular-WEB_OK.png", use_container_width=True)
