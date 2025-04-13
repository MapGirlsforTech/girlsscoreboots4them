import streamlit as st
from streamlit_app import translate

# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text)

st.header(translate("ods"))

parrafo("**17 objetivos para transformar nuestro mundo**")
parrafo("En 2015, la ONU aprobó la Agenda 2030 sobre el Desarrollo Sostenible, una oportunidad para que los países y sus sociedades emprendieran un nuevo camino con el que mejorar la vida de todas las personas, sin dejar a nadie atrás.")
parrafo("La Agenda cuenta con 17 Objetivos de Desarrollo Sostenible, que establecen que la erradicación de la pobreza debe ir de la mano de estrategias que fomenten el crecimiento económico y abordan una serie de necesidades sociales como la educación, la sanidad, la protección social y las perspectivas de empleo, al tiempo que se combate el cambio climático y se protege el medio ambiente.")

#Imagen todas las ODS

# Crear una columna para centrar la imagen
# Tres columnas, el centro tiene el triple de peso
col1, col2, col3 = st.columns([1, 3, 1])
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/Poster ODS_Spanish.png", use_container_width=True)

parrafo("Nuestra App aplica con los siguientes ODS:")

#Imagen 4 ODS

# Crear una columna para centrar la imagen
# Tres columnas, el centro tiene el triple de peso
col1, col2, col3 = st.columns([1, 3, 1])
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/ODS_Proyecto.png", use_container_width=True)

parrafo("ODS número 3: Salud y Bienestar")
parrafo("Nuestro proyecto toca el tema del deporte, tratando de concienciar a los usuarios sobre unos de los problemas que están cobrando mayor importancia en este ámbito. Por tanto, nuestra web App pretende mejorar la experiencia al practicar deporte y por tanto, el bienestar y la salud de las mujeres deportistas")
parrafo("ODS número 5: Igualdad de género")
parrafo("A día de hoy, es mucho más fácil encontrar un calzado adaptado al pie masculino que al femenino. Esto afecta directamente al rendimiento de las deportistas femeninas porque se lesionan con más facilidad y siendo graves  en algunas ocasiones estas lesiones.")
parrafo("ODS número 9: Industria,innovación e infraestructura")
parrafo("El desarrollo de este proyecto es completamente innovador. Después de realizar un exhaustivo estudio, no hemos encontrado calzado deportivo femenino para un gran número de deportes. Hacer ver a la industria este problema supondrá una innovación en la industria deportiva femenina.")
parrafo("ODS número 10: Reducción de las desigualdades")
parrafo("Nuestro proyecto cumple este ODS porque igual que hay calzado deportivo para hombres en todas las modalidades que lo requieren, también tendría que haber calzado deportivo femenino en las mismas condiciones. Esto hace que las mujeres estén infravaloradas.")
