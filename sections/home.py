import streamlit as st
from utils import parrafo, buttonLink, title
from streamlit_app import translate

title(translate("home.title"))
# Texto: Presentación del equipo

parrafo(translate("home.presentation"))

buttonLink(translate("home.linkToProgram"), "https://technovationchallenge.org/")

parrafo(translate("home.introductionToTestimony"))

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

parrafo(translate("home.projectFocus"))




#Home Definitiva

# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text,unsafe_allow_html=True)

    # Crear un enlace con apariencia de botón para el Corrreo
st.markdown(
    """
    <div style="display: flex; justify-content: right;">
    <a href="mailto:mapgirlsfortech@gmail.com" target="_blank">
        <button style="background-color: #4CAF50; color: white; padding: 5px 20px; font-size: 16px; border: none; cursor: pointer; border-radius: 5px;">
            Contáctanos
        </button>
    </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(" ")

#Titulo de la Home: Boots for Her, Girls Score!!!

# Centrar la cita, pero alineada a la izquierda
st.markdown(
    """
    <div style="display: flex; justify-content: center; width: 80%;">
        <blockquote style="text-align: left; font-style: italic; font-size: 1em; border-left: 5px solid #ccc; padding-left: 10px;">
            "He jugado al fútbol desde los 5 años y me encantan los deportes, pero nunca he encontrado botas diseñadas especificamente para chicas. He sufrido de varias lesiones en los tobillos, pero mi última lesión ha sido la más grave de todas, concretamente en la rodilla y he tenido que estar 4 meses en reposo total."
        </blockquote>
    </div>
    """,
    unsafe_allow_html=True
)

parrafo(" ")
st.markdown("El anterior testimonio es de nuestra compañera Pilar, que ha sufrido la lesión más grave de su trayectoria deportiva.")
st.markdown("Nos reunimos aquí porque compartimos una necesidad que no puede seguir siendo ignorada: la ausencia de calzado deportivo femenino para todas las disciplinas. El calzado deportivo disponible en el mercado, hecho en su mayoría para la anatomía masculina, no se adapta adecuadamente a la morfología del pie femenino. No es solo una cuestión de diseño y salud, es una cuestión de equidad, de representación y de respeto por nuestras necesidades como atletas, como mujeres y como personas.")
st.markdown("Aquí, compartiremos experiencias, conocimientos y estrategias para exigir a las marcas, diseñadores e instituciones deportivas que reconozcan y atiendan esta necesidad.")
st.markdown(" ")
st.markdown("**Este foro es nuestro punto de partida para el cambio.**")
st.markdown(" ")
st.markdown(" ")
# Crear una columna para centrar la imagen
col1, col2, col3 = st.columns([1, 3, 1])  # Tres columnas, el centro tiene el triple de peso
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/LOGO_Boots_1500x1500.png", use_container_width=True)