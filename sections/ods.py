import streamlit as st
from streamlit_app import translate
from utils import title, subtitle, parrafo
from translations import translations

title(translate("ods.title"))

st.markdown(
    f"<h4 style='text-align: center;'>{translate("ods.objectives_to_change_the_world.title")}</h3>",
    unsafe_allow_html=True
)

parrafo("")
parrafo(translate("ods.objectives_to_change_the_world.first_text"))
parrafo(translate("ods.objectives_to_change_the_world.second_text"))
parrafo("")
#Imagen todas las ODS

st.image("./images/Poster ODS_Spanish.png")
parrafo("")
subtitle(translate("ods.how_we_apply.title"))
parrafo("")
#Imagen 4 ODS

# Crear una columna para centrar la imagen
# Tres columnas, el centro tiene el triple de peso
col1, col2, col3 = st.columns([1, 3, 1])
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/ODS_Proyecto.png", use_container_width=True)

subtitle(translate("ods.how_we_apply.third_ods.title"))
parrafo(translate("ods.how_we_apply.third_ods.text"))
subtitle(translate("ods.how_we_apply.fifth_ods.title"))
parrafo(translate("ods.how_we_apply.fifth_ods.text"))
subtitle(translate("ods.how_we_apply.nineth_ods.title"))
parrafo(translate("ods.how_we_apply.nineth_ods.text"))
subtitle(translate("ods.how_we_apply.tenth_ods.title"))
parrafo(translate("ods.how_we_apply.tenth_ods.text"))
