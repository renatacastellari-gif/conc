import streamlit as st

# Configuração da página
st.set_page_config(page_title="IPI", page_icon="🟣")  # Sem wide

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
IPI a Recolher
</h2>
""", unsafe_allow_html=True)

# Conta destacada
st.markdown("""**`Conta: 2300390`**""")

# Bloco 1 - Competência 06/2025
st.markdown("""
<div style="
    background-color:#1E1E1E;
    padding:15px;
    border-radius:8px;
    margin-bottom:20px;">
<h5>Competência 06/2025:</h5>
<ul style="list-style-type:none; padding-left:0;">
<li>Filial <strong>008</strong>: Identificado pagamento de <span style="color:#FFA500;">R$ 14.174,76 a maior</span>.</li>
<li>Filial <strong>019</strong>: Identificado pagamento de <span style="color:#FFA500;">R$ 6.463,23 a maior</span>.</li>
<li><strong>Status:</strong> Fiscal ciente, verificar compensação.</li>
<li><strong>Sugestão:</strong> Automatizar o processo que envia esses valores para DCTFWeb para evitar digitação manual.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Bloco 2 - Competência 04/2025
st.markdown("""
<div style="
    background-color:#1E1E1E;
    padding:15px;
    border-radius:8px;
    margin-bottom:20px;">
<h5>Competência 04/2025:</h5>
<ul style="list-style-type:none; padding-left:0;">


<li>Filial 002: Diferença de <span style="color:#FFA500;">R$ 10,00</span> (Valor pago: <span style="color:#FFA500;">R$ 34.146,04</span>. Apuração: <span style="color:#FFA500;">R$ 34.136,04</span>).</li>
<li>Filial 006: Diferença <span style="color:#FFA500;">R$ 13,16 </span>.</li>
</ul>
""", unsafe_allow_html=True)


# Bloco 3 - Filial 015 (03/2025)
st.markdown("""
<div style="
    background-color:#1E1E1E;
    padding:15px;
    border-radius:8px;
    margin-bottom:20px;">
<h5> Competência 03/2025:</h5>
<ul style="list-style-type:none; padding-left:0;">
<li> Filial 015: Pagou <span style="color:#FFA500;">R$ 5.000,00 a menor</span>.</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<h2 style="
    color:#9B4DCC;
    font-family:'Montserrat',sans-serif;
    font-weight:700;
    text-align:center;
    border-bottom:2px solid #FFA500;
    padding-bottom:8px;
    margin-bottom:20px;">
IPI a Recuperar
</h2>
""", unsafe_allow_html=True)
st.markdown("""**`Conta: 1280342`**""")

# Bloco 4 - Diferença NF 880077
st.markdown("""
<div style="
    background-color:#1E1E1E;
    padding:15px;
    border-radius:8px;">
<h5> Competência: 05/2025.:</h5>
<li>Diferença de valor (Stile) na NF 880077</li>
<ul style="list-style-type:none; padding-left:0;">
<li><strong>Status:</strong> Fiscal ciente.</li>
</ul>
</div>
""", unsafe_allow_html=True)










