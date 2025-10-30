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

# Card com o texto original
st.markdown("""
<div style="
    background-color:#1E1E1E;
    padding:20px;
    border-radius:10px;
    margin-bottom:20px;
    box-shadow: 0 0 10px rgba(255, 165, 0, 0.2);">

<p>Foi identificado que o produto <strong>LB espuma</strong> estava sendo tributado na nota fiscal e indo para o razão, mas não na apuração fiscal.<br>
O departamento fiscal constatou que a apuração estava incorreta.</p>

<p>Foi identificado que a base de cálculo do imposto na emissão da nota não deduzia o ICMS destacado, como ocorre na apuração fiscal.<br>
Ficou alinhado inicialmente que seriam feitos lançamentos manuais para ajuste na contabilidade.</p>

<p>Na conciliação, verificou-se que itens da nota fiscal não estavam sendo tributados da mesma forma que nos itens da apuração fiscal.<br>
<strong>Status:</strong> Constatou-se que alguns produtos apresentavam erro de parâmetro no SAP, já corrigido pela Silmara.</p>

<p>A conciliação do COFINS foi realizada comparando os itens do razão (notas fiscais), analisando os XMLs e confrontando com a planilha de apuração fiscal.<br>
Estamos aguardando as correções do mês <strong>08</strong>.<br>
A conciliação do mês <strong>09</strong> deverá vir com as divergências reduzidas devido às correções efetuadas pela Silmara.<br>
Entretanto, uma nova conciliação deverá ser realizada, inclusive para verificar notas fiscais que não entraram no razão e suas possíveis ações e ajustes na contabilidade.</p>

</div>
""", unsafe_allow_html=True)
