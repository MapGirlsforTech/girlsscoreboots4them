import streamlit as st
from translations import translate
from utils import parrafo, title, subtitle, buttonLink

title(translate("documentation.title"))

parrafo(translate("documentation.subtitle"))
parrafo(translate("documentation.bullet_1"))
parrafo(translate("documentation.bullet_2"))
parrafo(translate("documentation.bullet_3"))
parrafo(translate("documentation.bullet_4"))
parrafo(translate("documentation.bullet_5"))
parrafo(translate("documentation.bullet_6"))
parrafo(translate("documentation.bullet_7"))
parrafo("")
parrafo("")
# Crear una columna para centrar la imagen
col1, col2, col3 = st.columns([1, 3, 1])  # Tres columnas, el centro tiene el triple de peso
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/LOGO_Boots_1500x1500.png", use_container_width=True)
