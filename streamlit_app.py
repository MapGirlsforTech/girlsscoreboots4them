import streamlit as st

# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text)

# Función para añadir un enlace
def enlace(enlace, titulo):
    st.page_link(enlace, label=titulo)

# Define el código CSS para el fondo de color

background_css = """
<style>
body {
    background-color: #f0f2f6;
}
</style>
"""

# Inserta el código CSS en la aplicación
st.markdown(background_css, unsafe_allow_html=True)

# st.header("MAP Girls for Tech")

st.markdown("<h2 style='text-align: center;'>MAP Girls for Tech</h2>", unsafe_allow_html=True)

# Texto: Presentación del equipo

st.markdown(
    "Hola, somos **Maite**, **Ana** y **Pilar** y juntas formamos el equipo MAP Girls for Tech. Participamos por tercer año consecutivo en el proyecto Technovation Girls, cuyo objetivo es acercar la tecnología a las chicas y jóvenes de 8 a 18 años, la idea es aumentar con esta iniciativa la presencia de mujeres en las carreras STEM."
)
parrafo("Debemos buscar un problema en nuestra comunidad que cumpla uno o varios de los Objetivos  de Desarrollo Sostenible 2030 de la ONU. Durante 12 semanas debemos trabajar para darle una solución a dicho problema y crear una App móvil o una Web App con dicha solución. ")

parrafo("En este programa participan y compiten equipos de chicas de todo el mundo divididas en tres categorías, Beginner, Junior y Senior. ")

parrafo("Las chicas aprendemos entre otras muchas cosas a programar, entrenar modelos de IA y a exponer nuestra idea y trabajo en público.")

parrafo("Podéis conocer más sobre este programa a través del siguiente enlace:")
# technovationchallenge.org

enlace("https://technovationchallenge.org/", "Programa Technovation Girls")
# st.markdown('[Programa Technovation](https://technovationchallenge.org/)')

parrafo("Un problema que nos ha llamado la atención es que no hay calzado deportivo femenino para las jugadoras de fútbol. Es crucial utilizar un calzado adecuado al practicar deporte, ya que el uso de zapatos no aptos para el pie puede causar graves lesiones. Este es el caso de nuestra compañera Pilar, así como de otras muchas mujeres, que debido a la falta de calzado adaptado a su pie sufre lesiones, en ocasiones importantes, ya que se ven  obligadas a recurrir al calzado masculino. Este es el testimonio de Pilar:")

st.caption("“He jugado al fútbol desde los 5 años y me encantan los deportes, pero nunca he encontrado botas específicamente para chicas. He sufrido de varias lesiones en los tobillos, pero mi última lesión, ha sido la más grave de todas concretamente en la rodilla, he tenido que estar 4 meses en reposo total.”")

parrafo("Ante esta problemática, la falta de calzado deportivo adecuado al pie de la mujer en muchos deportes femeninos, es hacia donde vamos a enfocar nuestro proyecto esta temporada.")

parrafo("Hemos desarrollado un cuestionario con una serie de preguntas que nos ayudarán a darle forma  al proyecto y tratar de buscar una solución a este problema: ")

parrafo("#### **¡¡¡NECESITAMOS VUESTRA AYUDA!!!**")

parrafo("¿Podrías contestar nuestro cuestionario?")

enlace("https://technovationchallenge.org/", "Enlace al cuestionario")

parrafo("__Muchas Gracias.__")
st.image("./images/Logo-Circular-WEB_OK.png", width=400)