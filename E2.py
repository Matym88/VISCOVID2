# importar las librerias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
sns.set_style("darkgrid")

st.title("Comparador de casos COVID Activos vs Recuperados")

st.markdown("## Bienvenido al comparador ")
st.markdown("#### Está página fue diseñada con el fin de dar a conocer los casos activos y recuperados de COVID-19 en chile con sus respectivos graficos para una mayor comprensión ")

df = pd.read_csv(
    "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto46/activos_vs_recuperados.csv")

df.set_index('fecha_primeros_sintomas', inplace=True)
covid = df.T


st.dataframe(covid.head(10))

seleccion = st.radio("Selecione categoría", ('activos',
                     'recuperados', 'activos y recuperados'))
if(seleccion == 'activos'):
    st.success('Activos')
elif(seleccion == 'recuperados'):
    st.success('Recuperados')
elif(seleccion == 'activos y recuperados'):
    st.success('Activos y recuperados')


primerafecha = datetime.strptime(covid.columns[15], '%Y-%m-%d')


ultimafecha = datetime.strptime(covid.columns[-1], '%Y-%m-%d')


start_time = st.slider("Seleccione las fechas: ", value=[
                       primerafecha, ultimafecha], format="YYYY-MM-DD")


index_of_primera_fecha = covid.columns.get_loc(
    start_time[0].strftime('%Y-%m-%d'))


index_of_ultima_fecha = covid.columns.get_loc(
    start_time[1].strftime('%Y-%m-%d'))


to_plot = covid.iloc[:,
                     index_of_primera_fecha:index_of_ultima_fecha+1]
if(seleccion == 'activos'):
    covid.drop(['recuperados'], inplace=True)
    to_plot1 = covid.iloc[:,
                          index_of_primera_fecha:index_of_ultima_fecha+1]
    st.markdown(
        "## En este grafico podemos observar la cantidad de pacientes COVID-19 activos en el rango de fechas seleccionado")
    fig, ax = plt.subplots()
    ax.plot(to_plot1.T)
    ax.set_title('Grafico de pacientes activos')
    ax.set_xlabel('fechas')
    ax.set_ylabel('Cantidad de pacientes activos')
    xs = np.arange(0, index_of_ultima_fecha-index_of_primera_fecha+1, 15)
    plt.xticks(xs, rotation=90)
    st.pyplot(fig)

    # st.table(fechas)

elif((seleccion == 'recuperados')):
    covid.drop(['activos'], inplace=True)
    to_plot2 = covid.iloc[:,
                          index_of_primera_fecha:index_of_ultima_fecha+1]

    st.markdown(
        "## En este grafico podemos observar la cantidad de pacientes COVID-19 recuperados en el rango de fechas seleccionado")
    fig, ax = plt.subplots()
    ax.plot(to_plot2.T)
    ax.set_title('Grafico de pacientes recuperados')
    ax.set_xlabel('fechas')
    ax.set_ylabel('Cantidad de pacientes recuperados')
    xs = np.arange(0, index_of_ultima_fecha-index_of_primera_fecha+1, 15)
    plt.xticks(xs, rotation=90)
    st.pyplot(fig)
    # st.table(fechas)

elif((seleccion == 'activos y recuperados')):
    covid.iloc[:,
               index_of_primera_fecha:index_of_ultima_fecha+1]
    st.markdown(
        "## En este grafico podemos observar la cantidad de pacientes COVID-19 activos vs los recuperados en el rango de fechas seleccionado")
    fig, ax = plt.subplots()
    ax.plot(to_plot.T)
    ax.set_title('Grafico de pacientes activos vs recuperados')
    ax.set_xlabel('fechas')
    ax.set_ylabel('Cantidad de pacientes recuperados')
    xs = np.arange(0, index_of_ultima_fecha-index_of_primera_fecha+1, 15)
    plt.xticks(xs, rotation=90)
    st.pyplot(fig)

    # st.table(fechas)

# st.table(filtro)
