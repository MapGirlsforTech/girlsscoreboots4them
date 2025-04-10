import streamlit as st
from streamlit_app import translate
from utils import parrafo, buttonLink, t
import pandas as pd
import plotly.express as px
data = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRpR6XlR7T_AdqCxVp83HRw85zMzFhrs18ehRsswsPHETFtB4wBljHB-Fdrc9RBDuv4hKrPU6U_Lt8F/pub?gid=160785226&single=true&output=csv')

st.header(translate("questionnaire"))

parrafo(t["home"]["questionnaire"])

parrafo(f"<h4 style='text-align: center;'>{t['home']['needYourHelp']}</h4>")

parrafo(f"<h5 style='text-align: center;'>{t['home']['questionnaireRequest']}</h5>")

parrafo(f"<h5 style='text-align: center;'>{t['home']['thankYou']}</h5>")

buttonLink(t["home"]["questionnaireLink"], "https://technovationchallenge.org/")

# Crear una columna para centrar la imagen
col1, col2, col3 = st.columns([1, 3, 1])  # Tres columnas, el centro tiene el triple de peso
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/Logo-Circular-WEB_OK.png", use_container_width=True)

df = pd.DataFrame(data)

df.rename(columns={
    'Marca Temporal': 'Fecha', 
    '01.  ¿Conocías que no existen botas / zapatillas diseñadas específicamente para el pie femenino en el fútbol y otros deportes?\n': "Conocimiento de existencia de botas para pie femenino",
    '02.  Indica cual es principal deporte que practicas:': "Deporte principal",
    ' 04. ¿Existen zapatillas / botas adaptadas al pie femenino para el deporte que practicas?': "Existe calzado femenino para el deporte que practicas?",
    '05.  ¿Las zapatillas / botas que utilizas en tu deporte te resultan cómodas?': "Tu calzado te resulta comodo?"
    }, inplace=True)

# Descomentar para ver la tabla
#st.dataframe(df)

st.header("Conocimiento de existencia de botas para pie femenino")
st.plotly_chart(
    px.pie(
        names=list(df["Conocimiento de existencia de botas para pie femenino"].value_counts().index), 
        values=list(df["Conocimiento de existencia de botas para pie femenino"].value_counts().values)
    )
)

st.header("Deporte principal")

st.plotly_chart(
    px.pie(
        names=list(df["Deporte principal"].value_counts().index), 
        values=list(df["Deporte principal"].value_counts().values)
    )
)

st.header("Existe calzado femenino para el deporte que practicas?")

st.plotly_chart(
    px.pie(
        names=list(df["Existe calzado femenino para el deporte que practicas?"].value_counts().index), 
        values=list(df["Existe calzado femenino para el deporte que practicas?"].value_counts().values)
    )
)

st.header("Tu calzado te resulta comodo?")

st.plotly_chart(
    px.pie(
        names=list(df["Tu calzado te resulta comodo?"].value_counts().index), 
        values=list(df["Tu calzado te resulta comodo?"].value_counts().values)
    )
)