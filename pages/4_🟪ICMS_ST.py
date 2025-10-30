import streamlit as st

# Configuração da página
st.set_page_config(page_title="ICMS-ST", page_icon="🟣")  # Sem wide

# CSS Global
st.markdown("""
<style>
body {
    font-family: 'Roboto', sans-serif;
    color: #EAEAEA;
}
ul li {
    margin-bottom: 10px;
    font-size: 17px;
    line-height: 1.6;
}
h3 {
    color: #9B4DCC;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# Cabeçalho com logo
st.image('teste.svg', width=200)
st.write("")

# Título principal
st.markdown("""
<h2 style="
    color:#9B4DCC;
    font-family:'Montserrat',sans-serif;
    font-weight:700;
    text-align:center;
    border-bottom:2px solid #FFA500;
    padding-bottom:8px;
    margin-bottom:20px;">
ICMS-ST
</h2>
""", unsafe_allow_html=True)

# Bloco de informações
st.markdown("""
<div style="
    background-color:#1E1E1E;
    padding:15px;
    border-radius:8px;
    margin-bottom:20px;">
<ul style="list-style-type:none; padding-left:0;">
<li>⚠️Não foi identificado o pagamento do ICMS ST mensal <strong>08/2025</strong> no valor de <span style="color:#FFA500;">R$ 55.394,97</span>, referente à filial <strong>15</strong>, com vencimento em <strong>12/09</strong>.</li>
<li><strong>Status:</strong> Guia recalculada e enviada para pagamento. 🎟️Multa e Juros: <span style="color:#FFA500;">R$ 6.892,22</span>.</li>
<li>Identificada <strong>notas de devolução sem direito a crédito</strong>.</li>
</ul>
</div>
""", unsafe_allow_html=True)

