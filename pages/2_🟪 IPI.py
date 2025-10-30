import streamlit as st

# Configuração da página
st.set_page_config(page_title="IPI", page_icon="🟣")  # Sem wide

# CSS Global para fonte e espaçamento
st.markdown("""
<style>
body {
    font-family: 'Montserrat', sans-serif;
    color: #EAEAEA;
}
ul li {
    margin-bottom: 10px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# Cabeçalho com logo
st.image('teste.svg', width=200)
st.write("")  # Espaço

# Título estilizado
st.markdown("""
<h2 style="
    color:#9B4DCC;
    font-family:'Montserrat',sans-serif;
    font-weight:700;
    text-align:center;
    border-bottom:2px solid #FFA500;
    padding-bottom:8px;
    margin-bottom:20px;">
IPI a Recolher
</h2>
""", unsafe_allow_html=True)

# Conta com destaque visual
st.markdown("""**`Conta: 2300390`**""")

# Bloco com lista estilizada
st.markdown("""
<div style="
    background-color:#1E1E1E;
    padding:15px;
    border-radius:8px;
    color:#FFFFFF;
    font-size:16px;">
<ul style="list-style-type:none; padding-left:0;">
<li> -- Competência <strong>06/2025</strong> (pagamento em 07/2025).</li>
<li>⚠️ Filial <strong>008</strong>: Identificado pagamento de <span style="color:#FFA500;">R$ 14.174,76 a maior</span>.</li>
<li>⚠️ Filial <strong>019</strong>: Identificado pagamento de <span style="color:#FFA500;">R$ 6.463,23 a maior</span>. <br><strong>Status:</strong> Fiscal ciente, verificar compensação.</li>
<li>💡 Sugestão: Automatizar o processo que envia esses valores para DCTFWeb para evitar digitação manual.</li>
<li>⚠️ Competência <strong>04/2025</strong>: diferença de <span style="color:#FFA500;">R$ 10,00</span> na Filial 002 e <span style="color:#FFA500;">R$ 13,16</span> na Filial 006.</li>
<li>⚠️ Filial <strong>015 (03/2025)</strong>: pagou <span style="color:#FFA500;">R$ 5.000,00 a menor</span>.</li>
<li>⚠️Diferença de valor na NF <strong>880077</strong>. <br><strong>Status:</strong> Fiscal ciente.</li>
</ul>
</div>
""", unsafe_allow_html=True)


