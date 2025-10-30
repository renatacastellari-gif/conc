import streamlit as st

# Configuração da página
st.set_page_config(page_title="PIS e COFINS", page_icon="🟣")

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
PIS e COFINS a Recolher
</h2>
""", unsafe_allow_html=True)

# Card com conteúdo organizado
st.markdown("""
<div style="
    background-color:#1E1E1E;
    padding:20px;
    border-radius:10px;
    margin-bottom:20px;
    box-shadow: 0 0 10px rgba(255, 165, 0, 0.2);">

<h4 style="color:#FFA500;">Conciliação Fiscal</h4>
<ul style="list-style-type:none; padding-left:0;">
<li>Produto <strong>LB espuma</strong> estava sendo tributado na nota fiscal e indo para o razão, mas não na apuração fiscal.</li>
<li>Base de cálculo do imposto na nota não deduzia o ICMS destacado, diferente da apuração fiscal.</li>
<li>Itens da nota fiscal estavam com tributação diferente da apuração. <strong>Status:</strong> Erro de parâmetro no SAP corrigido pela Silmara.</li>
</ul>

<h4 style="color:#FFA500;">Situação Atual</h4>
<ul style="list-style-type:none; padding-left:0;">
<li>Conciliação do COFINS foi feita comparando razão, XMLs e planilha de apuração.</li>
<li>Aguardando correções do mês <strong>08</strong>.</li>
<li>Conciliação do mês <strong>09</strong> deve vir com menos divergências.</li>
<li>Nova conciliação será feita para verificar notas que não entraram no razão e possíveis ajustes contábeis.</li>
</ul>

</div>
""", unsafe_allow_html=True)
