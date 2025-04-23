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

