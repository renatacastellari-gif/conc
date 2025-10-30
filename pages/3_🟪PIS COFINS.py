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
h4 {
    color: #FFA500;
    margin-bottom: 10px;
}
.card {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 20px;
    box-shadow: 0 0 8px rgba(255, 165, 0, 0.3);
}
p {
    font-size: 16px;
    line-height: 1.6;
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

# Bloco 1
st.markdown("""
<div class="card">
<p>Foi identificado que o produto <strong>LB espuma</strong> estava sendo tributado na nota fiscal e indo para o razão, mas não na apuração fiscal.<br>
O departamento fiscal constatou que a apuração estava incorreta.</p>
</div>
""", unsafe_allow_html=True)

# Bloco 2
st.markdown("""
<div class="card">
<p>Foi identificado que a base de cálculo do imposto na emissão da nota não deduzia o ICMS destacado, como ocorre na apuração fiscal.<br>
Ficou alinhado inicialmente que seriam feitos lançamentos manuais para ajuste na contabilidade.</p>
</div>
""", unsafe_allow_html=True)

# Bloco 3
st.markdown("""
<div class="card">
<p>Na conciliação, verificou-se que itens da nota fiscal não estavam sendo tributados da mesma forma que nos itens da apuração fiscal.<br>
<strong>Status:</strong> Constatou-se que alguns produtos apresentavam erro de parâmetro no SAP, já corrigido pela Silmara.</p>
</div>
""", unsafe_allow_html=True)

# Bloco 4
st.markdown("""
<div class="card">
<p>A conciliação do COFINS foi realizada comparando os itens do razão (notas fiscais), analisando os XMLs e confrontando com a planilha de apuração fiscal.<br>
Conciliação do mês <strong>08</strong> realizada.<br>
A conciliação do mês <strong>09</strong> ainda constam com divergências que precisam ser ajustadas pelo contábil na contabilidade. Como exemplo, notas fiscais que não entraram no razão e suas possíveis ações e ajustes na contabilidade<br>
Mês 10 testaremos os novos parametremos realizados pelo fiscal, uma nova conciliação deverá ser realizada.</p>
</div>
""", unsafe_allow_html=True)

