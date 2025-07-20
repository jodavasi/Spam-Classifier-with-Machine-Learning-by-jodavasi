#  Spam Classifier with Machine Learning and NLP

This project is a text message (SMS) classifier that predicts whether a message is **spam** or **legitimate (ham)**. It was developed using Python, scikit-learn, and basic Natural Language Processing (NLP) techniques, leveraging a public SMS dataset from Kaggle.

---

##  What does it do?

✅ Classifies messages as spam or ham  
✅ Applies **text preprocessing** and **TF-IDF** vectorization  
✅ Trains a **Naive Bayes** classification model  
✅ Allows predictions via a command-line Python script  
✅ Includes visualizations and evaluation metrics

---

##  Dataset

- **Source**: [Kaggle - SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

---

##  Tools and Libraries Used

- Python 3.x
- Jupyter Notebook
- scikit-learn
- pandas, seaborn, matplotlib
- TF-IDF for text vectorization
- joblib for model serialization
- (Optional) Streamlit for a web interface

---

##  Preprocessing

Before training the model, all messages are cleaned:
- Converted to lowercase
- Punctuation and special characters removed

![alt text](/spam-classifier/Images/image-1.png)

![alt text](/spam-classifier/Images/image.png)

---

##  Results

- Accuracy: ~96%
- High F1-score despite class imbalance
- Clear and reliable confusion matrix

![alt text](/spam-classifier/Images/image-2.png)

---

##  Prediction Examples

A command-line `.py` script was added to manually test the model. It uses the trained classifier to detect spam from user-provided input.

![alt text](/spam-classifier/Images/image-3.png)

---

##  Author

**Daniel Vargas Sibaja**  
Data Engineer  
Costa Rica 🇨🇷

__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Spam Classifier with Machine Learning and NLP

Este proyecto es un clasificador de mensajes de texto (SMS) que predice si un mensaje es **spam** o **legítimo (ham)**. Fue desarrollado con Python, scikit-learn y técnicas básicas de procesamiento de lenguaje natural (NLP), utilizando el dataset público de mensajes SMS de Kaggle.

---

## ¿Qué hace?

✅ Clasifica mensajes como spam o no spam  
✅ Utiliza **preprocesamiento de texto** y vectorización con **TF-IDF**  
✅ Entrena un modelo **Naive Bayes**  
✅ Permite predecir desde consola con un script personalizado  
✅ Incluye visualizaciones y métricas de evaluación

---

## Dataset

- **Fuente**: [Kaggle - SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

---

## Herramientas utilizadas

- Python 3.x
- Jupyter Notebook
- scikit-learn
- pandas, seaborn, matplotlib
- TF-IDF para vectorización de texto
- joblib para serializar el modelo
- (Opcional) Streamlit para interfaz web

---

## Preprocesamiento

Antes de entrenar el modelo, todos los mensajes son limpiados:
- Convertidos a minúsculas
- Eliminados signos de puntuación y caracteres especiales


![alt text](/spam-classifier/Images/image-1.png)

![alt text](/spam-classifier/Images/image.png)


## Resultados

- Accuracy: ~96%

- F1-score alto en clases desbalanceadas

- Matriz de confusión clara y precisa

![alt text](/spam-classifier/Images/image-2.png)

## Ejemplos de predicción

En el main agregué un .py en consola para pruebas manuales, la cual utiliza el modelo para identificar correos SPAM de entradas manuales.

![alt text](/spam-classifier/Images/image-3.png)

## Autor
Daniel Vargas Sibaja
Data Engineer
Costa Rica 🇨🇷
