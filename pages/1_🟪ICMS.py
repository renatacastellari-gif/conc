import streamlit as st

# Configuração da página
st.set_page_config(page_title="ICMS", page_icon="🟣")

# Cabeçalho
st.image('teste.svg', width=300)
st.write("")

# CSS para colorir números automaticamente
st.markdown(
    """
    <style>
    /* Cor padrão para texto */
    p, li {
        font-size: 18px;
        color: #333;
    }
    /* Cor para números */
    p, li strong {
        color: #FFA500; /* Laranja para números */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título estilizado
st.markdown("<p style='font-size:28px; font-weight:bold; color:#9B4DCC;'>ICMS a Recolher</p>", unsafe_allow_html=True)
st.markdown("**`2300391`**")

st.markdown("""
- Separadas as notas de consumo próprio para lançamentos manuais pela contabilidade.
- Foi identificada na Filial **019** a diferença de **R$ 910,20** (pago a maior), devido à retificação tardia.  
  **DARE ICMS Próprio 06/2025:** valor retificado de **R$ 27.303,93** para **R$ 26.393,73**.  
  Verificar status com fiscal.

- Foi identificada que a Filial **003** na competência **06/2025** pagou **R$ 1.038,31 a maior**. Tinha saldo credor.  
  Verificar status com fiscal.

- Foram identificados valores no razão estavam em contas incorretas ou com valores registrados incorretos (ex.: provisões e autos de infração).  
  **Status:** contabilidade já corrigiu grande parte.

- Há outras diferenças de notas que constam no razão e não no fiscal, e vice-versa, incluindo divergências de valores.  
  O relatório está salvo na pasta da rede. Diferenças relacionadas aos valores do DOOTAX grande parte foram ajustadas e resolvidas pela Patrícia.

- Lançamentos referentes aos ajustes na apuração.  
  A contabilidade precisa abrir as apurações fiscais para efetuar os lançamentos necessários.
""")

st.markdown("---")

# Segundo bloco
st.markdown("<p style='font-size:28px; font-weight:bold; color:#9B4DCC;'>ICMS a Recuperar</p>", unsafe_allow_html=True)
st.markdown("**`1280345`**")

st.markdown("""
- Foi identificado que os créditos tomados de ICMS sobre frete pelo fiscal não estão sendo registrados na contabilidade.  
  **Ação:** lançamentos manuais estão sendo realizados pela contabilidade.

- Entradas de transferências com crédito de ICMS apresentam diversas diferenças que precisam ser analisadas pelos departamentos.  
  Entre **01/2025 e 08/2025**, foram identificadas **559 notas com divergências** entre razão e apuração fiscal.  
  **Status:** pendente. Detalhes salvos na pasta da rede.

- Diferença de valor na NF **880077**  
  **Status:** pendente de verificação pelos departamentos.
""")
``
