import streamlit as st
from streamlit_app import translate
from utils import title, comment_with_avatar, parrafo, subtitle

title(translate("introduce_yourself.title"))

subtitle(translate("introduce_yourself.subtitle"))

comments = [
    "¡Qué alegría tenerte aquí!",
    "Este espacio ha sido creado por mujeres y para mujeres que comparten una pasión: el deporte en todas sus formas.",
    "Ya seas atleta profesional, amateur, entrenadora, estudiante o simplemente una amante del deporte en todas sus disciplinas, aquí encontrarás una comunidad que te apoya, te inspira y te entiende.",
    "El deporte no tiene género, pero la industria no tiene en cuenta todas nuestras necesidades, merecemos opciones de calzado deportivo diseñado para nosotras y nuestra anatomía, con la misma tecnología, innovación y variedad que se ofrece a nuestros compañeros masculinos.",
    "Comparte tus experiencias.",
    "Intercambia consejos y entrenamientos.",
    "Habla de nutrición, salud y bienestar.",
    "Conecta con otras mujeres como tú.",
    "Aquí celebramos tus logros, aprendemos de los desafíos y crecemos juntas.",
    "¡Gracias por ser parte de esta comunidad poderosa y auténtica!",
    "¡Bienvenida, este es tu espacio!",
]

for comment in comments:
    comment_with_avatar(
        user="",
        text=comment,
        date="",
        avatar_url="https://cdn-icons-png.flaticon.com/512/1077/1077012.png"
    )
