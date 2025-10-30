import streamlit as st
st.image('teste.svg', width=200) 


# Título estilizado
st.markdown("""
<h2 style="
    color:#9B4DCC;
    font-weight:700;
    border-bottom:2px solid #FFA500;
    padding-bottom:5px;
    margin-bottom:15px;">
IPI a Recolher
</h2>
""", unsafe_allow_html=True)

st.markdown("""**`Conta: 2300390`**""")

st.markdown("""

- Competência **06/2025** (pagamento em 07/2025).
- Filial **008**: Identificado pagamento de **R$ 14.174,76 a maior**.
- Filial **019**: Identificado pagamento de **R$ 6.463,23 a maior**.  
  **Status:** Fiscal ciente, verificar compensação.  
  **Sugestão:** Automatizar o processo que envia esses valores para DCTFWeb para evitar digitação manual.

- Competência **04/2025**: diferença de 10,00 na Filial 002 (valor pago 34.146,04 frente à apuração de 
 34.136,04) e diferença de **R$ 13,16** na Filial 006.
- Filial **015 (03/2025)**: pagou **R$ 5.000,00 a menor**.
- Diferença de valor na NF **880077**  
  **Status:** Fiscal ciente.

            




""")

