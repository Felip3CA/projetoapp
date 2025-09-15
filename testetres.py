import streamlit as st
import requests

# Função para pegar o conselho do dia
def pegar_conselho():
    url = "https://api.adviceslip.com/advice"
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            return dados['slip']['advice']
        else:
            return f"Erro ao buscar conselho: {resposta.status_code}"
    except Exception as e:
        return f"Erro: {str(e)}"

# --- Interface Streamlit ---
st.title("💡 Conselho do Dia")
st.write("Clique no botão para receber um conselho aleatório:")

if st.button("Gerar Conselho"):
    conselho = pegar_conselho()
    st.success(conselho)
