import pandas as pd
import random
import joblib
import streamlit as st
from time import sleep
import emoji

    
sentiment_model = joblib.load("sentiment_model.pkl")
viral_model = joblib.load("viral_model.pkl")

st.set_page_config(page_title="Viiper 🧠", layout="wide")

def contiene_emojis(comentario):
    return bool(emoji.emoji_list(comentario))

#RM
def obtener_emojis_random(cantidad=3):
    lista_emojis = ["🔥", "🚀", "😱", "✨", "🎉", "📣", "🌍", "💥", "📱", "🏆", "🎬", "🧠", "💬", "👀"]
    return " ".join(random.sample(lista_emojis, k=cantidad))

#Menu
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

# Secciones
if menu == "¿Cómo funciona Viipeer?":
    st.subheader("¿Cómo funciona Viiper?")
    st.write("""
    Viiper es una **inteligencia artificial avanzada** diseñada para analizar comentarios escritos por usuarios, y proporciona dos evaluaciones principales:

    - **Análisis de Sentimiento**:  
      Viiper utiliza modelos de procesamiento de lenguaje natural para identificar el **sentimiento** detrás de cada comentario. Esto determina si el contenido transmite una emoción **positiva**, **negativa** o **neutral**. Al identificar estas emociones, Viiper te permite comprender mejor como podria reaccionar la audiencia ante tu mensaje.

    - **Predicción de Viralidad**:  
      Utilizando algoritmos entrenados con una enorme cantidad de datos y ejemplos reales, Viiper evalúa el **potencial de viralidad** de un comentario. Esto se hace analizando patrones comunes en contenido viral, como el uso de **lenguaje emocional**, referencias a **temas actuales**, y elementos como **emojis**, **exclamaciones** o frases populares. Viiper predice si el comentario tiene características que lo hagan **atractivo** o **propenso a ser compartido** en plataformas sociales como Twitter, Instagram o Facebook.

    En resumen, Viiper te proporciona una **herramienta poderosa** para comprender como tu contenido podria impactar emocionalmente y su capacidad para **alcanzar una amplia audiencia**.
    """)


elif menu == "¿Tienes alguna duda?":
    st.subheader("¿Tienes alguna duda?")
    st.write("""
    Aqui respondemos algunas preguntas frecuentes:

    - **¿Que analiza Viiper?**
      Viiper analiza el contenido textual de tus comentarios y aplica modelos de aprendizaje automatico para detectar emociones y viralidad.

    - **¿Como funciona el modelo de sentimiento?**
      El modelo ha sido entrenado con miles de ejemplos para identificar si un comentario es positivo, negativo o neutral.

    - **¿Como predice la viralidad?**
      Utiliza patrones comunes como el lenguaje emocional, el uso de tendencias, y la presencia de elementos virales como emojis, exclamaciones, y frases populares.

    - **¿Los emojis influyen?**
      ¡Si! Si tu comentario tiene emojis, tienes una alta probabilidad de que tu comentario sea viral, Se asume que los emojis mejoran la expresividad y capturan mejor la atencion de la audiencia.

    - **¿Puedo confiar en los resultados?**
      Los resultados son estimaciones basadas en datos previos, por lo que no garantizan viralidad real, pero si te dan una buena orientacion.
    """)


elif menu == "Consejos para hacer tu comentario viral":
    st.subheader("Consejos para hacer tu comentario viral")
    st.write("""
    Si deseas maximizar las posibilidades de que tu comentario se vuelva viral, sigue estas estrategias clave basadas en el comportamiento en redes sociales y las mejores practicas:

    1. **Despierta emociones intensas**  
       El contenido que provoca emociones fuertes, como **sorpresa**, **entusiasmo**, **indignacion** o incluso **alegria** suele tener mas probabilidad de ser compartido. Las personas tienden a reaccionar y compartir cuando se sienten **emocionalmente** conectadas con un comentario.

    2. **Redacta frases claras y concisas**  
       A la gente le gusta la simplicidad. Las frases cortas y faciles de leer son mucho mas efectivas que parrafos largos y complejos. **Menos es mas**. Esto asegura que tu mensaje llegue rapido y claro.

    3. **Conecta tu comentario con temas actuales**  
       Relaciona tu mensaje con **noticias recientes**, eventos virales o **tendencias populares**. Al hacerlo, aprovecharas el interes general del publico y aumentaras las posibilidades de que tu comentario se comparta. Los temas de **cultura pop**, **politica** y **acontecimientos mundiales** suelen ser muy efectivos.

    4. **Usa un tono provocador, positivo o intrigante**  
       La forma en que te comunicas puede marcar la diferencia. Puedes optar por un tono **positivo y motivador**, **controversial** para generar debate, o **intrigante** para despertar la curiosidad de los demas. Cualquiera de estos enfoques puede generar mas interaccion.

    5. **Agrega humor cuando sea posible**  
       El **humor** es una excelente herramienta para hacer que tu comentario sea mas memorable. Las personas disfrutan compartir contenido que las haga reir o que presente situaciones comicas. Si puedes hacer que alguien sonria, tu mensaje tiene mas probabilidades de ser compartido.

    6. **Utiliza emojis para dar vida visual a tu comentario**  
       Los **emojis** no solo hacen que tu comentario sea mas atractivo visualmente, sino que tambien comunican emociones de manera rapida. Pueden ayudar a captar la atencion de las personas en medio de una gran cantidad de contenido. ¡Usarlos de forma estrategica puede aumentar la visibilidad de tu mensaje!

    7. **Incluye hashtags populares si estas en redes sociales**  
       Los **hashtags** son fundamentales para llegar a una audiencia mas amplia, especialmente en plataformas como **Instagram**, **Twitter** y **TikTok**. Utiliza hashtags relevantes y populares para aumentar la probabilidad de que tu comentario sea visto por mas personas.

    8. **Haz preguntas que incentiven la participacion de otros**  
       Las **preguntas abiertas** invitan a la audiencia a interactuar. Pregunta cosas como:  
       - "¿Que opinas tu sobre esto?"  
       - "¿Te ha pasado algo similar?"  
       - "¿Estas de acuerdo o no?"  
       Las preguntas fomentan el debate y la **participacion**, lo que puede hacer que tu comentario se vuelva mas visible y viral.

    9. **Aporta una opinion unica y autentica**  
       Evita caer en lo generico. **Aporta una opinion personal, original y autentica** que haga que tu comentario se destaque. Las personas valoran la sinceridad y la frescura. Si puedes ofrecer una perspectiva diferente, tus posibilidades de destacar aumentaran.

    ¿Listo para poner estos consejos en practica y hacer que tu proximo comentario se vuelva viral?
    """)
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

                if contiene_emojis(comentario_tema):
                    viral_label = "✅ Si, Completamente"
                else:
                    if hasattr(viral_model, 'predict_proba'):
                        prob = viral_model.predict_proba([comentario_tema])[0][1]
                        st.markdown(f"Probabilidad de viralidad: {prob:.2f}")
                        viral_label = "✅ Sí" if prob > 0.7 else "❌ No"
                    else:
                        viral = viral_model.predict([comentario_tema])[0]
                        viral_label = "✅ Sí" if viral == 1 else "❌ No"

                st.subheader("Resultados:")
                st.markdown(f"**Tema:** {tema}")
                st.markdown(f"**Sentimiento:** {sentiment_label}")
                st.markdown(f"**¿Viral?:** {viral_label}")

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

                if contiene_emojis(user_input):
                    viral_label = "✅ Si,  Completamente"
                else:
                    if hasattr(viral_model, 'predict_proba'):
                        prob = viral_model.predict_proba([user_input])[0][1]
                        st.markdown(f"Probabilidad de viralidad: {prob:.2f}")
                        viral_label = "✅ Sí" if prob > 0.7 else "❌ No"
                    else:
                        viral = viral_model.predict([user_input])[0]
                        viral_label = "✅ Sí" if viral == 1 else "❌ No"

                st.subheader(" Resultados del análisis:")
                st.markdown(f"**Sentimiento:** {sentiment_label}")
                st.markdown(f"**¿Puede volverse viral?:** {viral_label}")

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


st.markdown(
    """
    <style>
    body {
    
    }
    .stButton>button {
        background-color: #87CEEB;
        border: none;
        color: white; 
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
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
    unsafe_allow_html=True
)
