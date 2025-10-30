import streamlit as st

# Configuração da página
st.set_page_config(page_title="Conciliações dos Impostos", page_icon="🟪")

# Senha fixa
PASSWORD = "minhasenha123"

# Inicializa estado de login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 🔒 Esconde a barra lateral com CSS se não estiver logado
if not st.session_state.logged_in:
    hide_sidebar = """
        <style>
        [data-testid="stSidebar"] {display: none;}
        </style>
    """
    st.markdown(hide_sidebar, unsafe_allow_html=True)

# Se não estiver logado, pede senha
if not st.session_state.logged_in:
    st.title("Acesso Restrito")
    senha = st.text_input("Digite a senha:", type="password")
    if st.button("Entrar"):
        if senha == PASSWORD:
            st.session_state.logged_in = True
            st.success("Acesso liberado! Agora você pode navegar pelas páginas.")
            st.rerun() # Recarrega a página para mostrar o menu
        else:
            st.error("Senha incorreta.")
else:
    # 🔒 Conteúdo protegido
    st.image('teste.svg', width=400) 
    st.title('Conciliações dos Impostos')


    
st.markdown("""
<h1 style="
    color: #FF8C00;
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 10px;">
Conciliações dos Impostos
</h1>
""", unsafe_allow_html=True)

    
 
   


    st.markdown("<p style='font-size:29px; font-weight:bold; color:#FFA500;'>Seja bem vindo(a)</p>", unsafe_allow_html=True)  
    st.markdown("""
    - Nesta página, apresento o resumo do trabalho desenvolvido, com os principais destaques. 
    """)








