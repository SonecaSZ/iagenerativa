import streamlit as st
import requests

st.set_page_config(page_title="Tradutor com IA", layout="centered")

st.markdown("## 🌍✨ Tradutor Inteligente com IA")
st.markdown("Traduza textos com rapidez e inteligência usando a API MyMemory!")

st.info("Escolha os idiomas e clique em **'🔁 Traduzir agora'**.")

texto = st.text_area("✏️ Digite o texto para traduzir:")

col1, col2 = st.columns(2)

with col1:
    idioma_origem = st.selectbox("📥 Idioma de origem", ["pt", "en", "es", "fr", "it", "de"])

with col2:
    idioma_destino = st.selectbox("📤 Idioma de destino", ["en", "es", "fr", "pt", "it", "de"])

if st.button("🔁 Traduzir agora"):
    if not texto.strip():
        st.warning("⚠️ Por favor, digite algum texto para traduzir.")
    else:
        try:
            url = f"https://api.mymemory.translated.net/get?q={texto}&langpair={idioma_origem}|{idioma_destino}"
            response = requests.get(url)
            resultado = response.json()["responseData"]["translatedText"]
            st.text_area("📝 Resultado da tradução:", value=resultado, height=150)
        except Exception as e:
            st.error(f"Erro ao traduzir: {e}")
