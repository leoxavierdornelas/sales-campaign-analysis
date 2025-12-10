import streamlit as st
import pandas as pd

df = pd.read_csv("outputs/summary.csv")

st.title("Painel Interativo – Campanha de Vendas")
st.dataframe(df)

st.subheader("Filtrar por canal")
canal = st.selectbox("Selecione", df["canal"].unique())
st.write(df[df["canal"] == canal])

st.subheader("Métricas gerais")
st.metric("ROI Médio", round(df["roi"].mean(), 2))
st.metric("Taxa de Conversão Média", f"{round(df['taxa_conversao_pct'].mean(), 2)}%")
