import streamlit
import numpy as np
import joblib

st.title("Prédiction des évolution des anomalies de température ")
st.subheader("Application d'un modèle de regression linéaire polynomiale d'ordre 1")


# Chargement du modèle

model = joblib.load(filename="model_polynomial.joblib")

#prediction = model.predict