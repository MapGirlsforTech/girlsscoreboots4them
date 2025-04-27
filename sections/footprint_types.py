import streamlit as st
from streamlit_app import translate
from utils import title

# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text,unsafe_allow_html=True)


title(translate("footprint_types.title"))

st.markdown("Existen tres tipos de pisadas:")
St.markdown(" ")
St.markdown("**Pronadora:** Es aquella en la que el pie apoya por la zona interna. Es la pisada que secorresponde con los pies planos y en la que toda la carga del cuerpo recae hacia la zona interna del pie. En el estudio de la pisada observamos una huella muy ensanchada y un aplanamiento del pie.")
St.markdown(" ")
St.markdown("**Supinadora:** Es la pisada en la que el pie apoya por la zona externa. Se corresponde con los pies cavos, en los que se suele observar un arco interno muy elevado y un apoyo muy grande por el borde externo. Suelen presentar sobrecargas en la zona de talón y antepié.")
St.markdown(" ")
St.markdown("**Neutra:** Es la pisada en la que el apoyo se distribuye de manera homogénea. El talón apoya centrado y el peso se distribuye de manera correcta durante el paso.")
St.markdown(" ")

# Crear una columna para centrar la imagen
# Tres columnas, el centro tiene el triple de peso
col1, col2, col3 = st.columns([1, 3, 1])
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/Tipos-Pisadas_WEB.png", use_container_width=True)

St.markdown(" ")
St.markdown("Los pies de las mujeres no solo tienen una forma diferente, sino que también son más livianos que los de los hombres y su forma de correr y moverse, es diferente.")
St.markdown("El hecho de que no existan calzado deportivo específicamente diseñado para mujeres en todas las modalidades deportivas, puede contribuir a una serie de lesiones debido a las diferencias anatómicas entre hombres y mujeres.")
St.markdown("El calzado deportivo diseñado para hombres no siempre se ajusta bien a la morfología del pie femenino, lo que puede aumentar el riesgo de lesiones.")
St.markdown(" ")

# Crear una columna para centrar la imagen
# Tres columnas, el centro tiene el triple de peso
col1, col2, col3 = st.columns([1, 3, 1])
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/Diferencias Pie Hombre-mujer_WEB.png", use_container_width=True)

St.markdown(" ")
St.markdown("Razones por las que esto puede ocurrir:")
St.markdown(" ")
St.markdown("**1. Diferencias en la forma del pie:**")
St.markdown("Los pies de las mujeres tienden a ser más estrechos en el talón y más anchos en la zona de los dedos en comparación con los pies de los hombres. Si el calzado no está diseñado para ajustarse a esta forma, puede haber un ajuste incómodo o inadecuado, lo que aumenta el riesgo de:")
St.markdown("Ampollas y rozaduras: Un mal ajuste puede generar fricción en áreas específicas, lo que resulta en lesiones cutáneas como ampollas.")
St.markdown("Dolores en los pies y las articulaciones: Un ajuste inadecuado puede causar dolor en el pie o en la pierna, ya que no distribuye de manera adecuada las fuerzas durante el movimiento.")
St.markdown(" ")
St.markdown("**2. Tamaño y distribución del pie:**")
St.markdown("Las mujeres, en promedio, tienen pies más pequeños y ligeros que los hombres. Esto puede afectar el soporte y la estabilidad al usar calzado deportivo diseñado para hombres, que generalmente están hechas con una distribución del peso y un diseño que no toma en cuenta estas diferencias. Esto puede llevar a:")
St.markdown("Falta de soporte en el arco: Las botas diseñadas para hombres pueden no proporcionar un soporte adecuado en el arco del pie femenino, lo que puede contribuir a lesiones en los ligamentos y tendones.")
St.markdown("Estrés en las rodillas y caderas: El desajuste en las botas puede alterar la biomecánica del movimiento al correr o cambiar de dirección, lo que puede aumentar la presión en las rodillas y las caderas, favoreciendo lesiones como esguinces o tendinitis.")
St.markdown(" ")
St.markdown("**3. Lesiones en el tobillo:**")
St.markdown("Las mujeres tienden a tener una mayor flexibilidad en las articulaciones, especialmente en los tobillos. Si el calzado no ofrece un soporte adecuado, esto puede hacer que los tobillos sean más propensos a lesiones como:")
St.markdown("Esguinces de tobillo: Un calzado que no se ajusta correctamente o que no tiene suficiente soporte lateral puede aumentar el riesgo de esguinces, que son comunes en el fútbol debido a los cambios rápidos de dirección y la exigencia física.")
St.markdown(" ")
St.markdown("**4. Impacto en el rendimiento:**")
st.markdown("El calzado deportivo mal ajustado puede afectar el rendimiento al no proporcionar el nivel adecuado de comodidad y soporte. Esto puede hacer que la deportista cambie su postura o forma de correr para adaptarse al calzado, lo que aumenta el riesgo de sobrecargar ciertas partes del cuerpo (por ejemplo, las rodillas, la espalda o las caderas), lo que puede derivar en lesiones crónicas.")
st.markdown(" ")
st.markdown("**5. Lesiones por falta de amortiguación:**")
st.markdown("Las mujeres tienden a ser más propensas a sufrir lesiones relacionadas con el impacto debido a la diferencia en la distribución del peso corporal. Si el calzado no tiene suficiente amortiguación o si están diseñadas con una estructura menos adecuada para las mujeres, pueden surgir problemas como:")
st.markdown("Lesiones por estrés en los huesos (fracturas por sobrecarga): La falta de absorción adecuada de impactos puede aumentar el riesgo de fracturas por sobrecarga, especialmente en los pies y las piernas.")
st.markdown("Dolores articulares: La falta de una buena amortiguación puede generar molestias en las rodillas o la espalda debido a los golpes repetitivos durante la practica deportiva.")
st.markdown(" ")
st.markdown("**En resumen:**")
st.markdown("El uso de calzado deportivo no diseñado para la anatomía femenina puede aumentar el riesgo de lesiones, ya que no brindan el soporte, el ajuste o la comodidad adecuados para las deportistas.")
st.markdown("Las diferencias en la forma y tamaño de los pies, la flexibilidad articular, y la distribución del peso corporal entre hombres y mujeres son factores que pueden contribuir a estos riesgos.")
st.markdown("Por esta razón, es fundamental que el calzado deportivo femenino se diseñe teniendo en cuenta las necesidades específicas de las mujeres para reducir el riesgo de lesiones y mejorar el rendimiento.")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
