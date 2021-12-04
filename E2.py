# importar las librerias
from altair.vegalite.v4.api import value
from numpy.core.fromnumeric import shape
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style("darkgrid")

st.title("Comparador de casos COVID Activos vs Recuperados")

st.markdown("## Bienvenido al comparador ")
st.markdown("#### Está página fue diseñada con el fin de dar a conocer los casos activos y recuperados de COVID-19 en chile con sus respectivos graficos para una mayor comprensión ")

df = pd.read_csv(
    "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto46/activos_vs_recuperados.csv")


st.dataframe(df.head(10))
seleccion = st.radio("Selecione categoría", ('activos',
                     'recuperados', 'activos y recuperados'))
if(seleccion == 'activos'):
    st.success('Activos')
elif(seleccion == 'recuperados'):
    st.success('Recuperados')
elif(seleccion == 'activos y recuperados'):
    st.success('Activos y recuperados')


cantidad_columnas = len(df.index)

x, y = st.slider('Elegir rango de fechas a graficar:',
                 value=[1, cantidad_columnas])
filtro = pd.DataFrame(df.iloc[x:y+1])


if(seleccion == 'activos'):
    filtro.drop(['recuperados'], axis=1, inplace=True)
    fig, ax = plt.subplots()
    to_plot = filtro.iloc[:, 1:]
    ax.plot(to_plot)
    ax.set_title('Grafico de pacientes activos')
    ax.set_xlabel('Rango de fechas')
    ax.set_ylabel('Cantidad de pacientes recuperados')

    st.pyplot(fig)
    st.markdown(
        "## En este grafico podemos observar la cantidad de pacientes COVID-19 activos en el rango de fechas seleccionado")
    st.table(filtro.set_index('fecha_primeros_sintomas'))

elif((seleccion == 'recuperados')):
    filtro.drop(['activos'], axis=1, inplace=True)
    fig, ax = plt.subplots()
    to_plot = filtro.iloc[:, 1:]
    ax.plot(to_plot)
    ax.set_xlabel('Rango de Fechas')
    ax.set_ylabel('Cantidad de pacientes recuperados')
    st.pyplot(fig)
    st.markdown(
        "## En este grafico podemos observar la cantidad de pacientes COVID-19 recuperados en el rango de fechas seleccionado")


elif((seleccion == 'activos y recuperados')):
    to_plot1 = filtro.recuperados
    to_plot2 = filtro.activos

    fig, ax = plt.subplots()
    to_plot = filtro.iloc[:, 1:]
    ax.scatter(to_plot1, to_plot2)
    ax.set_title(
        'Grafico comparativo pacientes recuperados vs pacientes activos')
    ax.set_xlabel('Cantidad de pacientes activos')
    ax.set_ylabel('Cantidad de pacientes recuperados')

    st.pyplot(fig)
    st.markdown(
        "## En este grafico podemos observar la cantidad de pacientes COVID-19 activos vs los recuperados en el rango de fechas seleccionado")


st.table(filtro)
