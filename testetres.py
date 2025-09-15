# -*- coding: utf-8 -*-
import streamlit as st
import requests
import pandas as pd
import altair as alt

# --- Estilo da página ---
st.set_page_config(page_title="App Interativo", layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #F5B8B8, #D79DE3, #AAD0E5);
        color: #000000;
    }
    h2 {
        color: #A500FF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌟 App Interativo: Conselho, Emoção e Nutrição")

# --- Função: Conselho do Dia ---
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

# --- Seção 1: Conselho do Dia ---
st.header("💡 Conselho do Dia")
if 'historico_conselhos' not in st.session_state:
    st.session_state['historico_conselhos'] = []

if st.button("Gerar Conselho"):
    conselho = pegar_conselho()
    st.session_state['historico_conselhos'].append(conselho)
    st.success(conselho)

if st.session_state['historico_conselhos']:
    st.write("📜 Histórico de Conselhos:")
    for c in st.session_state['historico_conselhos']:
        st.write(f"- {c}")

# --- Seção 2: Detector de Emoções ---
st.header("🔮 Detector de Emoções")
API_KEY = "SUA_CHAVE_NLP_CLOUD"
MODEL = "distilbert-base-uncased-emotion"

def analisar_emocao(texto):
    url = f"https://api.nlpcloud.io/v1/{MODEL}/emotion"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"text": texto}
    resposta = requests.post(url, headers=headers, json=payload)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return {"erro": resposta.text}

texto_emocao = st.text_area("Digite um texto para detectar a emoção:")

if st.button("Analisar Emoção"):
    if texto_emocao.strip() != "":
        resultado = analisar_emocao(texto_emocao)
        if "erro" in resultado:
            st.error(resultado["erro"])
        else:
            # Emoção predominante
            emocao_predominante = max(resultado, key=resultado.get)
            st.markdown(f"### Emoção predominante: {emocao_predominante.capitalize()}")
            
            # Mostrar gráfico
            df = pd.DataFrame(list(resultado.items()), columns=["Emoção", "Intensidade"])
            chart = alt.Chart(df).mark_bar(color="#A500FF").encode(
                x="Emoção",
                y="Intensidade"
            )
            st.altair_chart(chart, use_container_width=True)
    else:
        st.warning("Digite algum texto para analisar!")

# --- Seção 3: Nutrição de Alimentos ---
st.header("🥗 Análise Nutricional")
EDAMAM_APP_ID = "SEU_APP_ID_EDAMAM"
EDAMAM_APP_KEY = "SEU_APP_KEY_EDAMAM"

def analisar_nutricao(ingrediente):
    url = "https://api.edamam.com/api/nutrition-data"
    params = {
        "app_id": EDAMAM_APP_ID,
        "app_key": EDAMAM_APP_KEY,
        "ingr": ingrediente
    }
    resposta = requests.get(url, params=params)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return {"erro": resposta.text}

ingrediente = st.text_input("Digite o alimento ou ingrediente:")

if st.button("Analisar Nutrição"):
    if ingrediente.strip() != "":
        dados = analisar_nutricao(ingrediente)
        if "erro" in dados:
            st.error(dados["erro"])
        else:
            st.subheader(f"Informações nutricionais: {ingrediente}")
            st.write(f"**Calorias:** {dados.get('calories', 'N/A')}")
            st.write(f"**Peso total:** {dados.get('totalWeight', 'N/A')} g")
            st.write("**Nutrientes principais:**")
            for nutriente, info in dados.get("totalNutrients", {}).items():
                st.write(f"- {info.get('label')}: {info.get('quantity'):.2f} {info.get('unit')}")
    else:
        st.warning("Digite um alimento para analisar!")
