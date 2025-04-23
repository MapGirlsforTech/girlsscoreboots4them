import streamlit as st
from translations import translate

# Helper para traducir los textos
languages_options = {"en": "English", "es": "Español"}
# Helper para obtener el label del idioma en base al indice
def format_func(option):
    return languages_options[option]

def set_language(lang):
    st.session_state["language"] = lang

# # Inicializar estado global si no existe
if "language" not in st.session_state:
    set_language("es")  # Idioma por defecto
# Genera el selector de idiomas
st.sidebar.selectbox("language selector",list(languages_options.keys()),index=list(languages_options.keys()).index(st.session_state.language), label_visibility="collapsed",format_func=format_func,on_change=set_language)   

pagePath = "sections"

navigation = st.navigation(
    pages={
        "": [
            st.Page(f'{pagePath}/home.py', title=translate("home_tab"), default=True),
            st.Page(f'{pagePath}/documentation.py', title=translate("documentation.title")), 
            st.Page(f'{pagePath}/questionnaire.py', title=translate("questionnaire")), 
            st.Page(f'{pagePath}/ods.py', title=translate("ods.title")), 
            st.Page(f'{pagePath}/footprint.py', title=translate("footprint"))
        ],
        translate("foro.title"): [
            st.Page(f'{pagePath}/forum/rules.py', title=translate("rules.title")),
            st.Page(f'{pagePath}/forum/introduce_yourself.py', title=translate("introduce_yourself.title")),
            st.Page(f'{pagePath}/forum/experiencies.py', title=translate("experiencies")),
            st.Page(f'{pagePath}/forum/footwear_shop.py', title=translate("footwear_shop")),
            st.Page(f'{pagePath}/forum/clothing_complements.py', title=translate("clothing_complements")),
            st.Page(f'{pagePath}/forum/merchandising.py', title=translate("merchandising"))
        ]
    }
)

navigation.run()
