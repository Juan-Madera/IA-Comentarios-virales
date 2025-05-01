import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

# Cargar datos
data = pd.read_csv("comentarios.csv")  # Asegúrate de que tengas un archivo CSV con tus datos de comentarios
X = data['comentario']
y_sentiment = data['sentimiento']  # Sentimiento: 'Positive', 'Negative', 'Neutral'
y_viral = data['viralidad']  # Viralidad: 1 para viral, 0 para no viral

# Preprocesamiento de texto (vectorización usando TF-IDF)
vectorizer = TfidfVectorizer(max_features=5000)
X_vec = vectorizer.fit_transform(X)

# Dividir en entrenamiento y prueba
X_train, X_test, y_train_sentiment, y_test_sentiment = train_test_split(X_vec, y_sentiment, test_size=0.2, random_state=42)
X_train_viral, X_test_viral, y_train_viral, y_test_viral = train_test_split(X_vec, y_viral, test_size=0.2, random_state=42)

# Entrenar modelo de sentimiento
sentiment_model = RandomForestClassifier(n_estimators=100, random_state=42)
sentiment_model.fit(X_train, y_train_sentiment)
print("Modelo de Sentimiento Entrenado")
print(classification_report(y_test_sentiment, sentiment_model.predict(X_test)))

# Entrenar modelo de viralidad
viral_model = RandomForestClassifier(n_estimators=100, random_state=42)
viral_model.fit(X_train_viral, y_train_viral)
print("Modelo de Viralidad Entrenado")
print(classification_report(y_test_viral, viral_model.predict(X_test_viral)))

# Guardar los modelos entrenados
joblib.dump(sentiment_model, 'sentiment_model.pkl')
joblib.dump(viral_model, 'viral_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')  # Guarda el vectorizador también, ya que lo necesitas en la app
