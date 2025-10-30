import streamlit as st
import re

# Configuração da página
st.set_page_config(page_title="ICMS", page_icon="🟣")

# CSS Global
st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: #EAEAEA;
    font-family: 'Montserrat', sans-serif;
}
h2 {
    font-family: 'Montserrat', sans-serif;
}
ul li {
    margin-bottom: 8px;
    font-size: 16px;
}
.card {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 20px;
    color: #FFFFFF;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}
.highlight {
    color: #FFA500;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Cabeçalho com logo
st.image('teste.svg', width=300)
st.write("")

# Função para aplicar cor apenas aos números
def color_numbers(text):
    return re.sub(r'(\d[\d.,]*)', r'<span class="highlight">\1</span>', text)

# ================= BLOCO 1: ICMS a Recolher =================
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
ICMS a Recolher
</h2>
""", unsafe_allow_html=True)

st.markdown("""**`Conta: 2300391`**""")

texto_recolher = """
<ul>
<li>Separadas as notas de consumo próprio para lançamentos manuais pela contabilidade.</li>
<li>Valores no razão estavam em contas incorretas ou com valores registrados incorretos (ex.: provisões e autos de infração).<br>
<strong>Status:</strong> contabilidade já corrigiu grande parte.</li>
<li>Diferenças entre razão e fiscal, incluindo divergências de valores.<br>
O relatório está salvo na pasta da rede. Diferenças relacionadas aos valores do DOOTAX grande parte foram ajustadas e resolvidas pela Patrícia.</li>
<li>Lançamentos referentes aos ajustes na apuração.<br>
Contabilidade precisa abrir as apurações fiscais para efetuar os lançamentos necessários.</li>
</ul>
"""
st.markdown(f"<div class='card'>{color_numbers(texto_recolher)}</div>", unsafe_allow_html=True)

# ================= BLOCO EXTRA: Diferenças por Filial =================
st.markdown("""
<h5 style="
    color:#FFA500;
    font-weight:700;
    border-bottom:2px solid #9B4DCC;
    padding-bottom:5px;
    margin-bottom:15px;">
Diferenças de Pagamentos
</h5>
""", unsafe_allow_html=True)

st.markdown("<div style='font-weight:bold; margin-bottom:8px;'>ICMS Próprio 06/2025:</div>", unsafe_allow_html=True)

texto_diferencas = """



<ul>
<li>⚠️ Filial 019: pagou R$ 910,20 a maior, devido à retificação tardia.<br>
DARE ICMS Próprio: Valor retificado de R$ 27.303,93 para R$ 26.393,73.<br>
Verificar status com fiscal.</li>
<li>⚠️ Filial 003: pagou R$ 1.038,31 a maior. Tinha saldo credor.<br>
Verificar status com fiscal.</li>
</ul>
"""
st.markdown(f"<div class='card'>{color_numbers(texto_diferencas)}</div>", unsafe_allow_html=True)

# Separador
st.markdown("<hr>", unsafe_allow_html=True)

# ================= BLOCO 2: ICMS a Recuperar =================
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
ICMS a Recuperar
</h2>
""", unsafe_allow_html=True)

st.markdown("""**`Conta: 1280345`**""")

texto_recuperar = """
<ul>
<li>⚠️ Créditos tomados de ICMS sobre frete pelo fiscal não estão sendo registrados na contabilidade.<br>
<strong>Ação:</strong> lançamentos manuais estão sendo realizados pela contabilidade.</li>
<li>⚠️ Entradas de transferências com crédito de ICMS apresentam diversas diferenças.<br>
Entre 01/2025 e 08/2025, foram identificadas 559 notas com divergências entre razão e apuração fiscal.<br>
<strong>Status:</strong> pendente. Detalhes salvos na pasta da rede.</li>
<li>⚠️ Diferença de valor (Stile) na NF 880077.<br>
<strong>Status:</strong> pendente de verificação pelos departamentos.</li>
</ul>
"""
st.markdown(f"<div class='card'>{color_numbers(texto_recuperar)}</div>", unsafe_allow_html=True)











