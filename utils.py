import streamlit as st

primaryColor = "#4CAF50"  # Color verde

# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text,unsafe_allow_html=True)

# Función para añadir un enlace
def enlace(enlace, titulo):
    st.page_link(enlace, label=titulo)

# Crear un enlace con apariencia de botón
def buttonLink(label, link):
    st.markdown(
       f"""
        <div style="display: flex; justify-content: center;">
        <a href="{link}" target="_blank">
            <button style="background-color: {primaryColor}; color: white; padding: 5px 20px; margin-bottom: 10px; font-size: 16px; border: none; cursor: pointer; border-radius: 5px;">
                {label}
            </button>
        </a>
        </div>
        """,
        unsafe_allow_html=True
    )

def title(text):
    st.markdown(f"""
    <h2 style="text-align: center; color: {primaryColor};">
        {text}
    </h2>
    """,
        unsafe_allow_html=True
    )

def subtitle(text):
        st.markdown(f"""
    <h4 style="text-align: center; color: {primaryColor};">
        {text}
    </h4>
    """,
        unsafe_allow_html=True
    )

def comment_with_avatar(user, text, date, avatar_url):
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; gap: 10px; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);background: rgb(38, 39, 48)">
            <img src="{avatar_url}" width="40px" height="40px" style="border-radius: 50%;" />
            <div style="display: flex; flex-direction: column;">
                <div style="display: flex; align-items: center; gap: 5px;">
                    <strong>{user}</strong> <small style="color: gray;">{date}</small>
                </div>
                <div>
                <p style="margin-top: 5px;">{text}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True
    )