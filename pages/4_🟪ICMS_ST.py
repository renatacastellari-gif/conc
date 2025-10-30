import streamlit as st

# Configuração da página
st.set_page_config(page_title="ICMS-ST", page_icon="🟣")

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

# Card 1 - Fundo creme
st.markdown("""
<div style="
    background-color:#F5F5DC; /* tom creme */
    color:#333333;
    padding:15px;
    border-radius:8px;
    margin-bottom:20px;">
<ul style="list-style-type:none; padding-left:0;">
<li>⚠️ Não foi identificado o pagamento do ICMS ST mensal <strong>08/2025</strong> no valor de <span style="color:#9B4DCC;">R$ 55.394,97</span>, referente à filial <strong>15</strong>, com vencimento em <strong>12/09</strong>.</li>
<li><strong>Status:</strong> Guia recalculada e enviada para pagamento. 🎟️ Multa e Juros: <span style="color:#9B4DCC;">R$ 6.892,22</span>.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Card 2 - Igual ao primeiro (fundo creme)
st.markdown("""
<div style="
    background-color:#F5F5DC; /* tom creme */
    color:#333333;
    padding:15px;
    border-radius:8px;
    margin-bottom:20px;">
<h5 style="color:#9B4DCC;">Notas de devolução sem direito a crédito:</h5>
<p>
Nas operações de venda com CFOP <strong>6.403</strong>, o ICMS-ST é recolhido antecipadamente. No entanto, quando há devolução dessas mercadorias por meio do CFOP <strong>2.411</strong>, e a empresa — como é o caso da Omnifile — não possui inscrição estadual no estado remetente, ela não pode se creditar do ICMS-ST destacado na nota original.
</p>
<p>
<strong>Status:</strong> Aguardando confirmação do departamento fiscal se há intenção de solicitar a restituição desses valores junto ao estado de origem ou se devemos considerar esses valores como perda definitiva para fins de contabilização.
</p>
</div>
""", unsafe_allow_html=True)
