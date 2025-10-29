import streamlit as st
import re

# Configuração da página
st.set_page_config(page_title="ICMS", page_icon="🟣")

# Cabeçalho
st.image('teste.svg', width=300)
st.write("")

# Função para aplicar cor apenas aos números
def color_numbers(text):
    return re.sub(r'(\d[\d.,]*)', r'<span style="color:#FFA500">\1</span>', text)

# Título estilizado
st.markdown("<h2 style='color:#9B4DCC;'>ICMS a Recolher</h2>", unsafe_allow_html=True)
st.markdown("""**`2300391`**""")

# Texto com números destacados
texto_recolher = """
<ul>
<li>Separadas as notas de consumo próprio para lançamentos manuais pela contabilidade.</li>
<li>Foi identificada na Filial 019 a diferença de R$ 910,20 (pago a maior), devido à retificação tardia.<br>
DARE ICMS Próprio 06/2025: valor retificado de R$ 27.303,93 para R$ 26.393,73.<br>
Verificar status com fiscal.</li>
<li>Foi identificada que a Filial 003 na competência 06/2025 pagou R$ 1.038,31 a maior. Tinha saldo credor.<br>
Verificar status com fiscal.</li>
<li>Foram identificados valores no razão estavam em contas incorretas ou com valores registrados incorretos (ex.: provisões e autos de infração).<br>
<strong>Status:</strong> contabilidade já corrigiu grande parte.</li>
<li>Há outras diferenças de notas que constam no razão e não no fiscal, e vice-versa, incluindo divergências de valores.<br>
O relatório está salvo na pasta da rede. Diferenças relacionadas aos valores do DOOTAX grande parte foram ajustadas e resolvidas pela Patrícia.</li>
<li>Lançamentos referentes aos ajustes na apuração.<br>
A contabilidade precisa abrir as apurações fiscais para efetuar os lançamentos necessários.</li>
</ul>
"""
st.markdown(color_numbers(texto_recolher), unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Segundo bloco
st.markdown("""**`1280345`**""")
st.markdown(color_numbers("<p style='font-size:20px;'>1280345</p>"), unsafe_allow_html=True)

texto_recuperar = """
<ul>
<li>Foi identificado que os créditos tomados de ICMS sobre frete pelo fiscal não estão sendo registrados na contabilidade.<br>
<strong>Ação:</strong> lançamentos manuais estão sendo realizados pela contabilidade.</li>
<li>Entradas de transferências com crédito de ICMS apresentam diversas diferenças que precisam ser analisadas pelos departamentos.<br>
Entre 01/2025 e 08/2025, foram identificadas 559 notas com divergências entre razão e apuração fiscal.<br>
<strong>Status:</strong> pendente. Detalhes salvos na pasta da rede.</li>
<li>Diferença de valor na NF 880077<br>
<strong>Status:</strong> pendente de verificação pelos departamentos.</li>
</ul>
"""
st.markdown(color_numbers(texto_recuperar), unsafe_allow_html=True)

