import streamlit as st
import streamlit.components.v1 as components

# Título do app
st.title("Dashboard de Faturamento Mensal")

# Embed do Power BI via iframe
components.html(
    """
    <iframe title="faturamento_mensal_" width="1140" height="541.25"
    src="https://app.powerbi.com/reportEmbed?reportId=41b18a5f-d294-4305-a56f-714a00efb81f&autoAuth=true&ctid=7c4d239e-9534-4e05-bb0b-ce4e8c32814a"
   
