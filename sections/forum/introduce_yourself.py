import streamlit as st
from streamlit_app import translate
from utils import title, comment_with_avatar

title(translate("introduce_yourself"))

comment_with_avatar("Lucas", "¡Este diseño se ve genial!", "2025-04-15", "https://picsum.photos/400/200")