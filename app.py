import streamlit as st
import requests

st.set_page_config(page_title="Tradutor com IA", layout="centered")

st.title("🌍 Tradutor com IA - MyMemory API")

texto = st.text_area("Digite o texto para traduzir:")
idioma_origem = st.selectbox("Idioma de origem", ["pt", "en", "es", "fr", "it", "de"])
idioma_destino = st.selectbox("Idioma de destino", ["en", "es", "fr", "pt", "it", "de"])

if st.button("Traduzir"):
    try:
        url = f"https://api.mymemory.translated.net/get?q={texto}&langpair={idioma_origem}|{idioma_destino}"
        response = requests.get(url)
        resultado = response.json()["responseData"]["translatedText"]
        st.success(f"Tradução: {resultado}")
    except Exception as e:
        st.error(f"Erro: {e}")
