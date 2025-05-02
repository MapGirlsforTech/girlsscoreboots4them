import streamlit as st
from streamlit_app import translate
from utils import title, comment_with_avatar, parrafo, subtitle

title(translate("introduce_yourself.title"))
subtitle(translate("introduce_yourself.subtitle"))
parrafo(translate("introduce_yourself.welcome_message"))

comments = [
    {
        "text": """
            Hola, soy Ana.<br>
            Práctico gimnasia rítmica y natación.<br>  
            Me encanta pasear con mi perro y jugar con él.<br>
            También me gusta mucho todo lo relacionado con la tecnología."<br>
        """,
        "user": "Ana"
    },
    {
        "text": '''
            Hola, soy Maite.<br>
            Practico Kárate.<br>
            Me gusta mucho leer y tocar el piano.<br>
        ''',
        "user": "Maite"
    },
    {
        "text": '''
          Hola, soy Pilar.<br>
            Práctico fútbol y tenis.<br>
            Me fascina viajar y acampar con los scouts.<br>  
        ''',
        "user": "Pilar"
    },
]

for comment in comments:
    comment_with_avatar(
        user=comment["user"],
        text=comment["text"],
        date="",
        avatar_url="https://cdn-icons-png.flaticon.com/512/1077/1077012.png"
    )
