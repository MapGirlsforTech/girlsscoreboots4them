import streamlit as st
from streamlit_app import translate
from utils import title, subtitle, image_center

# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text,unsafe_allow_html=True)


title(translate("footprint_types.title"))

subtitle(translate("footprint_types.types_title"), "left")
parrafo(translate("footprint_types.types"))

image_center("./images/Tipos-Pisadas_WEB.png")

parrafo(translate("footprint_types.second_text"))

image_center("./images/Diferencias_Pie_Hombre_mujer_WEB.png")

subtitle(translate("footprint_types.reasons_title"), "left")
parrafo(translate("footprint_types.reason_1"))
parrafo(translate("footprint_types.reason_2"))
parrafo(translate("footprint_types.reason_3"))
parrafo(translate("footprint_types.reason_4"))
parrafo(translate("footprint_types.reason_5"))
parrafo(translate("footprint_types.reason_summary"))

# Crear una columna para centrar la imagen
col1, col2, col3 = st.columns([1, 3, 1])  # Tres columnas, el centro tiene el triple de peso
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/LOGO_Boots_1500x1500.png", use_container_width=True)