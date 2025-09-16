import streamlit as st
import requests
import sqlite3
from datetime import datetime

# Estilo da página com fundo degradê e cor do texto
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #9754BA, #A500FF, #CC84F0, #572A75 );
        color: #FFFAFA;
    }
    </style>
    """,
    unsafe_allow_html=True)

# =========================
# CONFIGURAÇÃO DO APP
# =========================
st.set_page_config(page_title="Bem-Estar Emocional", layout="centered")

st.title(" Bem-Estar Emocional")
st.write("Um espaço para cuidar da sua mente e registrar seu progresso.")

# =========================
# BANCO DE DADOS
# =========================
conn = sqlite3.connect("humor.db")
c = conn.cursor()

# Tabela do Diário de Humor
c.execute("""CREATE TABLE IF NOT EXISTS diario (
    data TEXT, humor TEXT, anotacao TEXT
)""")

# Tabela do Diário de Gratidão
c.execute("""CREATE TABLE IF NOT EXISTS gratidao (
    data TEXT, gratidao TEXT
)""")

conn.commit()

# =========================
# MENU PRINCIPAL
# =========================
menu = st.sidebar.radio("📌 Menu", [
    "Diário de Humor", 
    "Diário de Gratidão", 
    "Frases Motivacionais", 
    "Meditações"
])

# =========================
# 1. DIÁRIO DE HUMOR
# =========================
if menu == "Diário de Humor":
    st.subheader(" Registro do Humor")
    humor = st.selectbox("Como você está se sentindo hoje?", [" Feliz", " Triste", " Irritado", " Cansado", " Ansioso", " Calmo"])
    anotacao = st.text_area("Quer escrever algo sobre o seu dia?")
    
    if st.button("Salvar registro"):
        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        c.execute("INSERT INTO diario (data, humor, anotacao) VALUES (?, ?, ?)", (data, humor, anotacao))
        conn.commit()
        st.success(" Registro salvo com sucesso!")

    st.subheader(" Histórico")
    registros = c.execute("SELECT * FROM diario ORDER BY rowid DESC").fetchall()
    for r in registros:
        st.write(f"**{r[0]}** - {r[1]} <br> {r[2]}", unsafe_allow_html=True)

# =========================
# 2. DIÁRIO DE GRATIDÃO
# =========================
elif menu == "Diário de Gratidão":
    st.subheader(" Registro de Gratidão")
    gratidao = st.text_area("Pelo que você é grato hoje?")
    
    if st.button("Salvar gratidão"):
        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        c.execute("INSERT INTO gratidao (data, gratidao) VALUES (?, ?)", (data, gratidao))
        conn.commit()
        st.success(" Gratidão registrada com sucesso!")

    st.subheader(" Registros anteriores")
    registros = c.execute("SELECT * FROM gratidao ORDER BY rowid DESC").fetchall()
    for r in registros:
        st.write(f"**{r[0]}** <br> {r[1]}", unsafe_allow_html=True)

# =========================
# 3. FRASES MOTIVACIONAIS
# =========================
elif menu == "Frases Motivacionais":
    st.subheader(" Inspire-se com uma frase")
    if st.button("Gerar frase"):
        url = "https://zenquotes.io/api/random"
        try:
            resposta = requests.get(url).json()
            texto = resposta[0]['q']
            autor = resposta[0]['a']
            st.success(f"“{texto}” — {autor}")
        except:
            st.error("Não foi possível buscar a frase. Tente novamente.")

# =========================
# 4. MEDITAÇÕES
# =========================
elif menu == "Meditações":
    st.subheader(" Sessões de Meditação")
    st.markdown("""
    <iframe width="300" height="200" 
        src="https://www.youtube.com/embed/3yTY24625C8" 
        frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
    """, unsafe_allow_html=True)

    st.write("Aúdios de músicas mais 'calmas'... clique para ter uma surpresinha...")
    # Música calma - relaxamento
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3")
    # Música instrumental suave
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3")
    # Música ambiente tranquila
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3")

# =========================
# CONSELHO DO DIA (fixo no final)
# =========================
def buscar_conselho():
    url = "https://api.adviceslip.com/advice"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados['slip']['advice']
    else:
        return None

st.title(" 💡 Conselho do Dia")

if st.button("Quero um novo conselho!"):
    conselho = buscar_conselho()
    if conselho:
        st.write(conselho)
    else:
        st.write("❌ Não foi possível obter o conselho. Tente novamente mais tarde.")
else:
    conselho = buscar_conselho()
    if conselho:
        st.write(conselho)
    else:
        st.write("❌ Não foi possível obter o conselho. Tente novamente mais tarde.")
