import streamlit as st
from streamlit_app import translate
from utils import parrafo, buttonLink, title, subtitle
import pandas as pd
import plotly.express as px
data = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRpR6XlR7T_AdqCxVp83HRw85zMzFhrs18ehRsswsPHETFtB4wBljHB-Fdrc9RBDuv4hKrPU6U_Lt8F/pub?gid=160785226&single=true&output=csv')

title(translate("questionnaire.title"))

parrafo(translate("home.questionnaire"))

parrafo(translate("questionnaire.thanks_message"))

buttonLink(translate("home.questionnaireLink"), "https://forms.gle/ti3ky6UAXbHjB2a87")

title(translate("questionnaire.charts_title"))

df = pd.DataFrame(data)

df.rename(columns={
    'Marca Temporal': 'Fecha', 
    '01.  ¿Conocías que no existen botas / zapatillas diseñadas específicamente para el pie femenino en el fútbol y otros deportes?\n': translate("questionnaire.charts.femaleSportsShoesAvailability"),
    '02.  Indica cual es principal deporte que practicas:': translate("questionnaire.charts.sportPracticed"),
    ' 04. ¿Existen zapatillas / botas adaptadas al pie femenino para el deporte que practicas?': translate("questionnaire.charts.femaleShoesExistence"),
    '05.  ¿Las zapatillas / botas que utilizas en tu deporte te resultan cómodas?': translate("questionnaire.charts.shoeComfort"),
    " 07. ¿Has tenido alguna lesión debida a las zapatillas / botas que utilizas?":translate("questionnaire.charts.injuriesDueToShoes"),
    "08.  ¿Utilizas algún tipo de plantilla o accesorio para mejorar el ajuste y/o la comodidad del calzado que utilizas?": translate("questionnaire.charts.comfortEnhancementMethods"),
    "11. ¿Te gustaría que existiese calzado adecuado al pie femenino para todas las modalidades deportivas?\n": translate("questionnaire.charts.wishForFemaleSportsShoes"),
    "15. ¿Conoces tu tipo de pisada?": translate("questionnaire.charts.knowledgeOfFootType"),
    "17. ¿Te gustaría que existiera una App para móvil o Web App que diera visibilidad al problema del calzado deportivo femenino y ayude a solucionarlo?": translate("questionnaire.charts.appToAddressFemaleSportsShoesIssue"),
    "24. ¿En qué tipo de superficie lo prácticas?": translate("questionnaire.charts.sportsSurfaceType")
    }, inplace=True)

# Descomentar para ver la tabla
# st.dataframe(df)

def chart(title):
    subtitle(title, "left")
    st.plotly_chart(
        key=title,
        figure_or_data=px.pie(
            names=list(df[title].value_counts().index), 
            values=list(df[title].value_counts().values)
        )
    )
    
charts_values = list(translate("questionnaire.charts").keys())

for value in charts_values:
    chart(translate("questionnaire.charts")[value])
