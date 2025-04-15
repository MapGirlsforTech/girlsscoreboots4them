import streamlit as st

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
            <button style="background-color: #4CAF50; color: white; padding: 5px 20px; margin-bottom: 10px; font-size: 16px; border: none; cursor: pointer; border-radius: 5px;">
                {label}
            </button>
        </a>
        </div>
        """,
        unsafe_allow_html=True
    )

def title(text):
    st.markdown(f"""
    <h2 style="text-align: center; color: #4CAF50;">
        {text}
    </h2>
    """,
        unsafe_allow_html=True
    )

def subtitle(text):
        st.markdown(f"""
    <h4 style="text-align: center; color: #4CAF50;">
        {text}
    </h4>
    """,
        unsafe_allow_html=True
    )
