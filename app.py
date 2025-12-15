import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Análisis de anuncios de vehículos")

df = pd.read_csv("vehicles_us.csv")

st.write("Vista previa del conjunto de datos:")
st.write(df.head())

# Casillas de verificación
show_hist = st.checkbox("Mostrar histograma de precios")
show_scatter = st.checkbox("Mostrar gráfico de dispersión (Precio vs Año)")

if show_hist:
    fig_hist = px.histogram(
        df,
        x="price",
        nbins=50,
        title="Distribución de precios de los vehículos"
    )
    st.plotly_chart(fig_hist)

if show_scatter:
    fig_scatter = px.scatter(
        df,
        x="model_year",
        y="price",
        title="Precio vs Año del modelo",
        opacity=0.5
    )
    st.plotly_chart(fig_scatter)
