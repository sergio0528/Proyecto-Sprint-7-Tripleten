import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("vehicles_us.csv")

st.header("Análisis de anuncios de venta de vehiculos")

hist_button = st.button("Construir histograma")
if hist_button:
    st.write("Histograma de la columna odómetro")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Construir gráfico de dispersión")
if scatter_button:
    st.write("Relación entre odómetro y precio")
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
