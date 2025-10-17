import streamlit as st
st.image('teste.svg', width=200) 


st.markdown("""

## PIS e COFINS a Recolher
- Foi identificado que o produto **LB espuma** estava sendo tributado na nota fiscal e indo para o razão, mas não na apuração fiscal.  
  O departamento fiscal constatou que a apuração estava incorreta.

- Foi identificado que a base de cálculo do imposto na emissão da nota não deduzia o ICMS destacado, como ocorre na apuração fiscal.  
  Ficou alinhado inicialmente que seriam feitos lançamentos manuais para ajuste na contabilidade.

- Na conciliação, verificou-se que itens da nota fiscal não estavam sendo tributados da mesma forma que nos itens da apuração fiscal.  
  **Status:** Constatou-se que alguns produtos apresentavam erro de parâmetro no SAP, já corrigido pela Silmara.

A conciliação do COFINS foi realizada comparando os itens do razão (notas fiscais), analisando os XMLs e confrontando com a planilha de apuração fiscal.  
Estamos aguardando as correções do mês **08**.  
A conciliação do mês **09** deverá vir com as divergências reduzidas devido às correções efetuadas pela Silmara.  
Entretanto, uma nova conciliação deverá ser realizada, inclusive para verificar notas fiscais que não entraram no razão e suas possíveis ações e ajustes na contabilidade.

""")