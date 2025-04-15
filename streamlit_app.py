import streamlit as st
from translations import translations

# Helper para traducir los textos

def translate(key):
    # """Obtiene la traducción desde la estructura anidada."""
    keys = key.split(".")
    translation = translations.get(st.session_state.language, {})

    for k in keys:
        translation = translation.get(k, None)
        if translation is None:
            return f"Translation for '{key}' not found"

    return translation

languages_options = {"en": "English", "es": "Español"}
# Helper para obtener el label del idioma en base al indice
def format_func(option):
    return languages_options[option]

# Inicializar estado global si no existe
if "language" not in st.session_state:
    st.session_state.language = "es"  # Idioma por defecto

# Genera el selector de idiomas
with st.sidebar:
    selected_language = st.selectbox("language selector",list(languages_options.keys()), index=list(languages_options.keys()).index(st.session_state.language), label_visibility="collapsed",format_func=format_func)   
# Guarda el idioma seleccionado en el estado de sesión
if selected_language != st.session_state.language:
    st.session_state.language = selected_language

home = st.Page(f'sections/home.py',
                       title=translate("home_tab"), default=True)

documentation = st.Page(f'sections/documentation.py',
                       title=translate("documentation"))

questionnaire = st.Page(f'sections/questionnaire.py',
                       title=translate("questionnaire"))

ods = st.Page(f'sections/ods.py',
                       title=translate("ods.title"))

footprint = st.Page(f'sections/footprint.py',
                       title=translate("footprint"))

# # Secciones del foro
rules = st.Page(
    'sections/forum/rules.py', title=translate("rules")
)
clothing_complements = st.Page(
    'sections/forum/clothing_complements.py', title=translate("clothing_complements")
)
experiencies = st.Page(
    'sections/forum/experiencies.py', title=translate("experiencies")
)
footwear_shop = st.Page(
    'sections/forum/footwear_shop.py', title=translate("footwear_shop")
)
introduce_yourself = st.Page(
    'sections/forum/introduce_yourself.py', title=translate("introduce_yourself")
)

# # Funciona como router, desde aca se renderizan las paginas

# # Con esto configuro a mano las paginas pudiendo customizar el titulo e icono
pg = st.navigation(
    {
        "": [home,documentation, questionnaire, ods, footprint],
        translate("foro.title"): [rules,introduce_yourself,experiencies,footwear_shop,clothing_complements]
    }
)
if pg is not None:
    pg.run()
