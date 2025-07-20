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
