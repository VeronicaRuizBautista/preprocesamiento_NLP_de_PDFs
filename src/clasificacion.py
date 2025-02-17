from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import streamlit as st

def clasificar(vector, textos):
    n_clusters = 3
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(vector)
    labels = kmeans.labels_
    
    vector_train, vector_test, labels_train, labels_test, textos_train, textos_test = train_test_split(vector, labels, textos, test_size=0.33, random_state=42)
    
    model = MultinomialNB()
    model.fit(vector_train, labels_train)
    
    y_pred = model.predict(vector_test)
    # Mostrar cómo clasificó cada frase
    classification_results = []
    for texto, prediccion in zip(textos_test, y_pred):
        classification_results.append(f"Frase: {texto}\nClase predicha: {prediccion}\n---")
        
    st.text_area("Resultados de clasificación:", "\n".join(classification_results), height=300)
    return accuracy_score(labels_test, y_pred)
    