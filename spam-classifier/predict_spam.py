import joblib
import re

# Función de limpieza (idéntica a la del entrenamiento)
def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z0-9\s]', '', texto)
    return texto

# Cargar modelo y vectorizador
model = joblib.load("models/spam_classifier_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Entrada
mensaje = input("Ingresá el mensaje a analizar: ")
mensaje_limpio = limpiar_texto(mensaje)

# Vectorizar
mensaje_vectorizado = vectorizer.transform([mensaje_limpio])

# Predicción
prediccion = model.predict(mensaje_vectorizado)[0]

# Resultado
if prediccion == 1:
    print("El mensaje es SPAM")
else:
    print("El mensaje es legítimo")
