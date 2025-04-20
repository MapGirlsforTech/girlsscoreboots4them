import streamlit as st
from streamlit_app import translate
from utils import title, parrafo

title(translate("rules.title"))

parrafo(translate("rules.first_rule"))
parrafo(translate("rules.second_rule"))
parrafo(translate("rules.third_rule"))
parrafo(translate("rules.fourth_rule"))
parrafo(translate("rules.fifth_rule"))
parrafo(translate("rules.sixth_rule"))
parrafo(translate("rules.seventh_rule"))
parrafo(translate("rules.eighth_rule"))
parrafo("")
parrafo("")
# Crear una columna para centrar la imagen
col1, col2, col3 = st.columns([1, 3, 1])  # Tres columnas, el centro tiene el triple de peso
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/LOGO_Boots_1500x1500.png", use_container_width=True)