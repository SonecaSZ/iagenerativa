import streamlit as st
import requests

st.set_page_config(page_title="🌐 Tradutor com IA", layout="centered")
st.title("🌐 Tradutor com LibreTranslate (Online)")

texto = st.text_area("Digite o texto para traduzir:")

idiomas = {
    "Inglês": "en",
    "Espanhol": "es",
    "Francês": "fr",
    "Alemão": "de",
    "Italiano": "it",
    "Português": "pt"
}
idioma_destino_nome = st.selectbox("Idioma de destino:", list(idiomas.keys()))
idioma_destino = idiomas[idioma_destino_nome]

if st.button("Traduzir") and texto:
    with st.spinner("Traduzindo..."):
        try:
            response = requests.post(
                "https://libretranslate.de/translate",
                headers={"Content-Type": "application/json"},
                json={
                    "q": texto,
                    "source": "auto",
                    "target": idioma_destino,
                    "format": "text"
                }
            )
            if response.ok:
                st.success("Tradução:")
                st.write(response.json()["translatedText"])
            else:
                st.error("Erro ao traduzir.")
        except Exception as e:
            st.error(f"Erro: {e}")
