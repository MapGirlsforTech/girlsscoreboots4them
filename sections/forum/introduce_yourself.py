import streamlit as st
from streamlit_app import translate
from utils import title, comment_with_avatar, parrafo, subtitle

title(translate("introduce_yourself.title"))
subtitle(translate("introduce_yourself.subtitle"))
parrafo(translate("introduce_yourself.welcome_message"))

# comments = [
#     "¡Qué alegría tenerte aquí!",
# ]

# for comment in comments:
#     comment_with_avatar(
#         user="",
#         text=comment,
#         date="",
#         avatar_url="https://cdn-icons-png.flaticon.com/512/1077/1077012.png"
#     )
