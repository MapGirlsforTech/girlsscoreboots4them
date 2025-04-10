import streamlit as st
from utils import parrafo, buttonLink, t


parrafo(
    f"""
    <h2 style="text-align: center; color: #4CAF50;">
        {t["home"]["title"]}
    </h2>
    """
)

# Texto: Presentación del equipo

parrafo(t["home"]["presentation"])


buttonLink(t["home"]["linkToProgram"], "https://technovationchallenge.org/")

parrafo(t["home"]["introductionToTestimony"])

# Centrar la cita, pero alineada a la izquierda
parrafo(
    f"""
    <div style="display: flex; justify-content: center; width: 80%;">
        <blockquote style="text-align: left; font-style: italic; font-size: 1em; border-left: 5px solid #ccc; padding-left: 10px;">
             {t["home"]["testimony"]}
        </blockquote>
    </div>
    """
)

parrafo(t["home"]["projectFocus"])

