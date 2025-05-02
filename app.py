import pandas as pd
import random
import joblib
import streamlit as st
from time import sleep
import emoji
import re

sentiment_model = joblib.load("sentiment_model.pkl")
viral_model = joblib.load("viral_model.pkl")

st.set_page_config(page_title="Viiper 🧠", layout="wide")

def contiene_emojis(comentario):
    return bool(emoji.emoji_list(comentario))

# Nueva función para evaluar viralidad basada en consejos
def evaluar_viralidad_por_consejos(comentario):
    puntaje = 0

    if contiene_emojis(comentario):
        puntaje += 1

    if "?" in comentario:
        puntaje += 1

    if "#" in comentario:
        puntaje += 1

    emociones = ["increíble", "sorprendente", "épico", "indignante", "alegría", "triste", "feliz", "odio", "encanta"]
    if any(palabra in comentario.lower() for palabra in emociones):
        puntaje += 1

    if len(comentario) < 200:
        puntaje += 1

    humor = ["jaja", "😂", "lol", "chiste", "gracioso", "divertido"]
    if any(palabra in comentario.lower() for palabra in humor):
        puntaje += 1

    opinion = ["yo", "pienso", "me parece", "creo que", "en mi opinión"]
    if any(palabra in comentario.lower() for palabra in opinion):
        puntaje += 1

    temas_actuales = ["inteligencia artificial", "elecciones", "messi", "tiktok", "climático", "ia"]
    if any(palabra in comentario.lower() for palabra in temas_actuales):
        puntaje += 1

    viral_label = "✅ Sí" if puntaje >= 5 else "❌ No"
    return viral_label, puntaje

def obtener_emojis_random(cantidad=3):
    lista_emojis = ["🔥", "🚀", "😱", "✨", "🎉", "📣", "🌍", "💥", "📱", "🏆", "🎬", "🧠", "💬", "👀"]
    return " ".join(random.sample(lista_emojis, k=cantidad))

menu = st.selectbox(
    "Selecciona una opción:",
    options=[
        "Análisis y Predicción de Comentarios",
        "¿Cómo funciona Viiper?",
        "¿Tienes alguna duda?",
        "Consejos para hacer tu comentario viral",
        "Análisis por tema"
    ]
)

if menu == "¿Cómo funciona Viiper?":
    st.subheader("¿Cómo funciona Viiper?")
    st.write("""
    Viiper es una inteligencia artificial avanzada diseñada para analizar comentarios escritos por usuarios, y proporciona dos evaluaciones principales:

    - **Análisis de Sentimiento**
    - **Predicción de Viralidad** basada en criterios sociales y lingüísticos.

    """)
elif menu == "¿Tienes alguna duda?":
    st.subheader("¿Tienes alguna duda?")
    st.write("""
    - **¿Qué analiza Viiper?** Sentimiento y potencial de viralidad.
    - **¿Los emojis influyen?** Sí, pero ya no garantizan viralidad por sí solos.
    - **¿Puedo confiar en los resultados?** Son estimaciones basadas en patrones reales.

    """)

elif menu == "Consejos para hacer tu comentario viral":
    st.subheader("Consejos para hacer tu comentario viral")
    st.write("""[tu texto original de los consejos aquí, puedes pegarlo tal cual para no hacerlo muy largo aquí]""")

elif menu == "Análisis por tema":
    st.title("Análisis por tema")
    tema = st.selectbox("Selecciona un tema", ["Deportes", "Política", "Tecnología", "Cultura", "Entretenimiento"])
    comentario_tema = st.text_area("Escribe tu comentario sobre el tema seleccionado:", height=150)

    if st.button("Analizar comentario por tema"):
        if not comentario_tema.strip():
            st.warning("Por favor escribe algo.")
        else:
            with st.spinner("Analizando..."):
                sleep(2)
                sentiment = sentiment_model.predict([comentario_tema])[0]
                sentiment_label = "Positivo" if sentiment == "Positive" else "Negativo" if sentiment == "Negative" else "Neutral"

                viral_label, puntaje = evaluar_viralidad_por_consejos(comentario_tema)

                st.subheader("Resultados:")
                st.markdown(f"**Tema:** {tema}")
                st.markdown(f"**Sentimiento:** {sentiment_label}")
                st.markdown(f"**¿Puede volverse viral?:** {viral_label} (Puntaje: {puntaje}/8)")

    def generar_comentario_por_tema(tema):
        emojis = obtener_emojis_random()
        if tema == "Deportes":
            jugador = random.choice(["Messi ⚡", "Cristiano 🔥", "LeBron 🏀", "Serena 🎾", "Max Verstappen 🏎️"])
            evento = random.choice(["final de la Copa del Mundo", "gran final de la NBA", "torneo de Grand Slam"])
            return f"¡{jugador} lo ha hecho de nuevo en la {evento}! ¡Una actuación épica! {emojis}"
        elif tema == "Política":
            return f"Este discurso está generando controversia en todo el país. ¿Qué opinas? {emojis}"
        elif tema == "Tecnología":
            return f"La nueva IA está cambiando el mundo. ¿La estás usando ya? {emojis}"
        elif tema == "Cultura":
            return f"Una obra maestra que mezcla tradición y modernidad. ¡Imperdible! {emojis}"
        elif tema == "Entretenimiento":
            return f"Esa escena fue simplemente legendaria. ¡Nadie lo esperaba! {emojis}"
        return f"Comentario viral sobre {tema}. {emojis}"

    if st.button("Generar comentario viral del tema"):
        sugerencia = generar_comentario_por_tema(tema)
        st.subheader("Comentario sugerido:")
        st.text_area("Aquí tienes una sugerencia:", value=sugerencia, height=100)

elif menu == "Análisis y Predicción de Comentarios":
    st.title("Viiper 🧠 - Analiza tu comentario")
    user_input = st.text_area("Escribe tu comentario:", height=150)

    if st.button("Analizar comentario"):
        if not user_input.strip():
            st.warning("Por favor escribe algo.")
        else:
            with st.spinner("Analizando..."):
                sleep(2)
                sentiment = sentiment_model.predict([user_input])[0]
                sentiment_label = "Positivo" if sentiment == "Positive" else "Negativo" if sentiment == "Negative" else "Neutral"

                viral_label, puntaje = evaluar_viralidad_por_consejos(user_input)

                st.subheader(" Resultados del análisis:")
                st.markdown(f"**Sentimiento:** {sentiment_label}")
                st.markdown(f"**¿Puede volverse viral?:** {viral_label} (Puntaje: {puntaje}/8)")

    def generar_comentario_viral():
        adjetivos = ["increíble", "asombroso", "impactante", "épico", "sorprendente"]
        verbos = ["ha revolucionado", "está explotando en redes", "es viral", "domina las plataformas"]
        sustantivos = ["momento", "evento", "revelación", "contenido", "historia"]
        exclamaciones = ["¡Wow!", "¡No puedo creerlo!", "¡Esto va a romper internet!", "¡Legendario!"]
        temas = ["tecnológico", "deportivo", "político", "cultural", "de entretenimiento"]
        emojis = obtener_emojis_random()

        return f"{random.choice(exclamaciones)} Este {random.choice(sustantivos)} {random.choice(verbos)} en el ámbito {random.choice(temas)}. ¡Simplemente {random.choice(adjetivos)}! {emojis}"

    if st.button("Generar comentario viral"):
        comentario = generar_comentario_viral()
        st.subheader("Comentario sugerido:")
        st.text_area("Comentario generado:", value=comentario, height=100)

# Estilos
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #87CEEB;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        font-size: 16px;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 1px solid #87CEEB;
    }
    .stButton>button:focus {
        outline: none;
        color: black !important;
        background-color: white;
        border: 1px solid #87CEEB !important;
    }
    </style>
    """,
    unsafe_allow_
