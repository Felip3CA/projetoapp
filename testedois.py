# Configurações da página
st.set_page_config(
    page_title="Serenidade - Seu Espaço de Bem-Estar",  # Título da aba
    page_icon="🧘",                                     # Ícone da aba
    layout="wide",                                      # Ocupa toda a largura da tela
    initial_sidebar_state="expanded"                     # Barra lateral expandida por padrão
)

# Título da página
st.title("Serenidade - Seu Espaço de Bem-Estar")

# Introdução
st.markdown("""
Bem-vindo ao **Serenidade**, seu espaço dedicado ao equilíbrio e bem-estar. 
Aqui você encontrará práticas, dicas e recursos para cultivar a paz interior e melhorar a sua saúde física e mental.
""")

# Seção de dicas de bem-estar
st.header("Dicas para o seu Bem-Estar")

st.write("""
- **Meditação diária**: A prática de meditação, mesmo que por poucos minutos, pode ajudar a reduzir o estresse e aumentar a concentração.
- **Exercícios de respiração**: Técnicas de respiração profunda são poderosas para acalmar a mente e reduzir a ansiedade.
- **Alimentação equilibrada**: Comer alimentos frescos e nutritivos pode ter um grande impacto no seu bem-estar geral.
- **Movimento corporal**: Incorporar atividades físicas como yoga, caminhadas ou alongamentos à sua rotina traz grandes benefícios.
""")

# Seção de vídeos e recursos
st.header("Recursos para Relaxamento")

st.markdown("""
Aqui estão alguns vídeos e recursos para ajudar você a relaxar e se reconectar consigo mesmo:
""")

# Links para recursos
st.markdown("""
- [Vídeo: Meditação Guiada para Iniciantes](https://www.youtube.com/watch?v=MIr3RsUGrP4)
- [Playlist de Música Relaxante no Spotify](https://spotify.com)
- [Artigo: A Arte de Relaxar](https://exemplo.com/artigo-arte-de-relaxar)
""")

# Barra lateral com navegação
st.sidebar.title("Menu de Navegação")

menu = st.sidebar.radio(
    "Escolha uma opção",
    ("Introdução", "Dicas de Bem-Estar", "Vídeos e Recursos", "Contato")
)

if menu == "Introdução":
    st.sidebar.write("Você está na página inicial, um espaço dedicado ao bem-estar.")
elif menu == "Dicas de Bem-Estar":
    st.sidebar.write("Aqui você encontra dicas de como cuidar melhor de sua saúde física e mental.")
elif menu == "Vídeos e Recursos":
    st.sidebar.write("Explore vídeos e outros materiais para te ajudar a relaxar.")
elif menu == "Contato":
    st.sidebar.write("Entre em contato conosco para saber mais sobre nossos programas de bem-estar.")

# Final da página
st.markdown("""
#### Em caso de dúvidas ou mais informações, não hesite em nos contatar.
""")

st.sidebar.markdown("""
#### Contato:
- Email: contato@serenidade.com
- Telefone: (XX) XXXXX-XXXX
""")