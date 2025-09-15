import streamlit as st  # Biblioteca principal para criar app web interativo
import datetime          # Para manipular datas e horas
import pandas as pd      # Para criar tabelas (DataFrames) e gráficos
import numpy as np       # Biblioteca de cálculos numéricos (não usada aqui)
import time              # Para pausas e contagem regressiva

# Configuração da página
st.set_page_config(
    page_title="Serenidade - Seu Espaço de Bem-Estar",  # Título da aba
    page_icon="🧘",                                     # Ícone da aba
    layout="wide",                                      # Ocupa toda a largura da tela
    initial_sidebar_state="expanded"                    # Barra lateral aberta
)

# CSS personalizado
st.markdown("""<style>
    .main-header {font-size: 3rem; color: #6a9589; text-align: center;}
    .subheader {font-size: 1.5rem; color: #d7a575;}
    .breathing-container {text-align:center; padding:2rem; border-radius:15px; background-color:#f8f3e6; margin:1rem 0;}
    .mood-tracker {background-color:#f0f7ee; padding:1.5rem; border-radius:15px; margin:1rem 0;}
    .gratitude-journal {background-color:#f9f2e6; padding:1.5rem; border-radius:15px; margin:1rem 0;}
</style>""", unsafe_allow_html=True)  # Permite customizar cores, fontes e layout

# Inicialização de estado da sessão
if 'mood_data' not in st.session_state:  # Cria lista para guardar humor se não existir
    st.session_state.mood_data = []
if 'gratitude_entries' not in st.session_state:  # Lista para diário de gratidão
    st.session_state.gratitude_entries = []

# Cabeçalho
st.markdown('<h1 class="main-header">🧘 Serenidade</h1>', unsafe_allow_html=True)  # Título principal
st.markdown("### Seu espaço dedicado ao bem-estar e equilíbrio")  # Subtítulo

# Barra lateral
with st.sidebar:
    st.title("🧘 Serenidade")  # Título da sidebar
    st.markdown("---")        # Linha separadora
    page = st.radio("Navegar para:", ["🏠 Início", "🧘 Meditação", "📔 Diário de Gratidão", "😊 Rastreador de Humor", "🌬️ Respiração", "🌿 Dicas"])  # Menu de navegação
    st.markdown("---")
    st.info("💫 Respire fundo. Este momento é só seu.")  # Mensagem de informação

# Página inicial
if "Início" in page:
    col1, col2 = st.columns([2, 1])  # Divide a tela em duas colunas
    
    with col1:
        st.markdown("## Bem-vindo ao seu refúgio de paz")  # Subtítulo
        st.write("""Texto explicando o app e funcionalidades""")  # Explicação
    
    with col2:
        st.image("https://placehold.co/300x200/6a9589/white?text=☯", width=300)  # Imagem
    
    st.markdown("---")
    st.success("💡 **Dica do Dia:** Beba um copo de água ao acordar para hidratar o corpo")  # Dica

# Página de meditação
elif "Meditação" in page:
    st.markdown("## 🧘 Meditação Guiada")  # Subtítulo
    
    meditation_type = st.selectbox("Escolha o tipo de meditação:", ["Respiração Consciente", "Body Scan", "Visualização Guiada", "Mindfulness"])  # Seleção de meditação
    duration = st.slider("Duração (minutos):", 1, 5, 3)  # Slider para tempo
    
    if st.button("Iniciar Meditação", type="primary"):  # Botão iniciar
        st.write(f"## {meditation_type} por {duration} minutos")
        st.write("Instruções de meditação")
        
        progress_bar = st.progress(0)  # Barra de progresso
        status_text = st.empty()       # Espaço para atualizar o tempo restante
        
        for i in range(duration * 60):  # Loop para contar tempo
            progress = (i + 1) / (duration * 60)
            progress_bar.progress(progress)
            
            minutes_left = (duration * 60 - i) // 60
            seconds_left = (duration * 60 - i) % 60
            status_text.text(f"Tempo restante: {minutes_left:02d}:{seconds_left:02d}")
            time.sleep(1)  # Pausa 1s
        
        progress_bar.empty()
        status_text.empty()
        st.success("🎉 Meditação concluída!")

# Página de diário de gratidão
elif "Diário" in page:
    st.markdown("## 📔 Diário de Gratidão")
    
    with st.form("gratitude_form"):  # Formulário de entrada
        gratitude1 = st.text_input("Pelo que você é grato hoje? (1)")
        gratitude2 = st.text_input("Pelo que você é grato hoje? (2)")
        gratitude3 = st.text_input("Pelo que você é grato hoje? (3)")
        submitted = st.form_submit_button("Salvar Entrada")
        
        if submitted:  # Salva entradas na sessão
            entry = {"date": datetime.date.today().strftime("%d/%m/%Y"), "entries": [gratitude1, gratitude2, gratitude3]}
            st.session_state.gratitude_entries.append(entry)
            st.success("✅ Entrada salva com sucesso!")
    
    if st.session_state.gratitude_entries:  # Mostra entradas anteriores
        st.markdown("### Suas Entradas Anteriores")
        for entry in reversed(st.session_state.gratitude_entries[-3:]):
            st.write(f"**{entry['date']}:**")
            for i, item in enumerate(entry['entries'], 1):
                if item: st.write(f"{i}. {item}")

# Página de rastreador de humor
elif "Humor" in page:
    st.markdown("## 😊 Rastreador de Humor")
    
    mood = st.slider("Como você está se sentindo hoje? (1 = muito triste, 10 = excelente)", 1, 10, 5)  # Slider para humor
    notes = st.text_area("Alguma observação sobre seu humor hoje?")  # Notas adicionais
    
    if st.button("Registrar Humor"):  # Salvar humor
        entry = {"date": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"), "mood": mood, "notes": notes}
        st.session_state.mood_data.append(entry)
        st.success("✅ Humor registrado com sucesso!")
    
    if st.session_state.mood_data:  # Mostra gráfico de humor
        df = pd.DataFrame(st.session_state.mood_data)
        st.line_chart(df.set_index('date')['mood'])

# Página de exercícios de respiração
elif "Respiração" in page:
    st.markdown("## 🌬️ Exercícios de Respiração")
    
    technique = st.selectbox("Escolha uma técnica:", ["4-7-8 (Relaxamento)", "Box Breathing (Foco)", "Respiração Diafragmática (Ansiedade)"])
    
    if st.button("Iniciar Exercício"):
        st.write("💨 Siga as instruções visuais e auditivas")
        breath_placeholder = st.empty()  # Espaço para atualizar instruções
        
        for i in range(3):  # Ciclos de respiração
            breath_placeholder.info("🗣️ INSPIRE...")
            time.sleep(2)
            breath_placeholder.warning("⏸️ SEGURE...")
            time.sleep(2)
            breath_placeholder.success("😮‍💨 EXPIRE...")
            time.sleep(3)
        
        breath_placeholder.empty()
        st.success("✅ Exercício concluído!")

# Página de dicas de bem-estar
elif "Dicas" in page:
    st.markdown("## 🌿 Dicas de Bem-Estar")
    
    tab1, tab2 = st.tabs(["💧 Hidratação", "😴 Sono"])  # Cria abas
    
    with tab1:
        st.write("**Dicas de Hidratação:**\n- Beba 2L de água\n- Comece o dia com um copo\n- Use app para lembrar")
    
    with tab2:
        st.write("**Dicas para Melhor Sono:**\n- Mantenha horários\n- Evite telas 1h antes de dormir\n- Crie ambiente escuro e silencioso")

# Rodapé
st.markdown("---")
st.caption("Serenidade - Seu espaço de bem-estar | Desenvolvido com Streamlit")  # Texto no rodapé












