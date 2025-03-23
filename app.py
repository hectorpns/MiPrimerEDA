import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

st.header("Análisis Exploratorio de Datos de Vehículos")

# Botón para generar el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Si el botón es presionado
    st.write('Creación de un histograma para la columna odómetro')

    # Crear el histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)

# Botón para generar el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # Si el botón es presionado
    st.write('Creación de un gráfico de dispersión para odómetro vs precio')

    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")

    # Mostrar el gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)

# Casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')
if build_scatter:
    st.write('Construir un gráfico de dispersión para odómetro vs precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
