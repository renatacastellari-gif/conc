import streamlit as st
 
st.set_page_config(
    page_title="CONCILIAÇÕES",
    page_icon="🟪",
 
)
 
 
st.image('teste.svg', width=400)
st.title('Conciliações')
st.write('💜 💜:smile: :purple_heart: 💜')
 
 
 
 
st.markdown("""
 
  ## ICMS a Recuperar
- Foi identificado que os créditos tomados de ICMS sobre frete pelo fiscal não estão sendo registrados na contabilidade.  
  **Ação:** lançamentos manuais estão sendo realizados pela contabilidade.
 
- Entradas de transferências com crédito de ICMS apresentam diversas diferenças que precisam ser analisadas pelos departamentos.  
  Entre **01/2025 e 08/2025**, foram identificadas **559 notas com divergências** entre razão e apuração fiscal.  
  **Status:** pendente. Detalhes salvos na pasta da rede.
 
- Diferença de valor na NF **880077**  
  **Status:** pendente de verificação pelos departamentos.
 
---
🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣
## IPI a Recolher
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
 
---
🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣
 
## ICMS a Recolher
- Separadas as notas de consumo próprio para lançamentos manuais pela contabilidade.
- Foi identificada na Filial **019** a diferença de  910,20 (pago a maior).  
  Devido à retificação tardia.  
  **DARE ICMS Próprio 06/2025:** valor retificado de 27.303,93 para R$ 26.393,73.  
  Verificar status com fiscal.
 
- Foi identificada que a Filial **003** na competência **06/2025** pagou **R$ 1.038,31 a maior**. Tinha saldo credor.  
  Verificar status com fiscal.
 
- Foram identificados valores no razão estavam em contas incorretas ou com valores registrados incorretos (ex.: provisões e autos de infração).  
  **Status:** contabilidade já corrigiu grande parte.
 
- Há outras diferenças de notas que constam no razão e não no fiscal, e vice-versa, incluindo divergências de valores.  
  O relatório está salvo na pasta da rede. Diferenças relacionadas aos valores do DOOTAX grande parte foram ajustadas e resolvidas pela Patrícia.
 
- Lançamentos referentes aos ajustes na apuração.  
  A contabilidade precisa abrir as apurações fiscais para efetuar os lançamentos necessários.
 
---
🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣
 
## COFINS a Recolher
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
 
 
 
("""
 
---
🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣
""")
 
 
 
("""
 ## ICMS-ST
 
- Não foi identificado o pagamento do ICMS ST mensal 08/2025 no valor de R$ 55.394,97, referente à filial 15, com vencimento em 12/09.
 
  **Status:** Guia recalculada e enviada para pagamento.  Multa e Juros: R$ 6.892,22.
 
 
 
**Dúvidas**🤔⁉️
 
 
- Devoluções sem direito a credito: a contabilidade, o razão deve refletir todos os fatos relacionados ao **ICMS-ST**, mesmo os que **não geram crédito fiscal**.
 
Isso garante que a conta **bata com os relatórios fiscais** e com o **controle analítico das notas**.
 
Então, mesmo que a **devolução interestadual** não gere crédito fiscal, ela é um **fato econômico** que afeta a conta — porque representa o **retorno de mercadoria que já teve ICMS-ST recolhido**.
 
No controle fiscal, você apenas **não aproveita o crédito**, pois a legislação **veda o ressarcimento automático** de ICMS-ST interestadual (cada estado trata isso de forma diferente — geralmente exige processo de ressarcimento à parte).
 
### Como tratar na contabilidade:
 
Você pode:
- **Lançar normalmente** o valor na conta ICMS-ST (para manter o histórico completo).
- Mas usar **subconta, centro de custo ou histórico diferenciado**, indicando que é *“devolução interestadual sem crédito de ICMS-ST”*.
- Assim, na hora de **conciliar contábil x fiscal**, você consegue **filtrar essas situações** e entender por que o saldo não é compensado.
 
---
 
### 📘 Exemplo prático:
 
| Tipo de nota | Estado | Histórico contábil | Débito / Crédito | Observação |
|---------------|---------|--------------------|------------------|-------------|
| Venda         | SP      | ICMS-ST a recolher | Crédito (C)      | Valor a pagar |
| Devolução     | SP      | Estorno ICMS-ST    | Débito (D)       | Crédito permitido |
| Devolução     | MG      | Devolução interestadual sem crédito de ICMS-ST | Débito (D) | Não aproveita crédito |
 
**Resultado:** o valor da devolução de MG entra no razão (para controle), mas **não reduz o saldo de ICMS-ST a pagar** na apuração.
 
---
 
✅ **Conclusão:**
- **Sim**, deve entrar na conta do ICMS-ST no razão, pois contabilidade reflete todos os fatos.  
- **Mas contábil ≠ fiscal:** o crédito **não é aproveitado** no fiscal.  
- Ideal é **diferenciar com histórico** para não confundir na conciliação.
""")
 
 
("""
**Exemplo das Notas fiscais:**""")
st.image('ICMST.png', width=9000)
 