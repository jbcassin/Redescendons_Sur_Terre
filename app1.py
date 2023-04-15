import streamlit as st
import numpy as np
import joblib
import datetime 
import pandas as pd

st.title("Prédiction des évolution des anomalies de température ")
st.subheader("Application d'un modèle de regression linéaire polynomiale d'ordre 1")

# Chargement du modèle
model = joblib.load(filename="./Notebooks/model_polynomial.joblib")

#definition d'une fonction inference 
def inference(futur_periods):   
    # Convertir la date en timestamp
    timestamp = pd.Timestamp(futur_periods)
    # Création d'un tableau numpy
    new_data = np.array([timestamp.value])
    prediction = model.predict(new_data.reshape(-1, 1))
    return prediction[0]

# L'utilisateur saisie une période sous la forme annee-mois-jour   
#min_date = pd.Timestamp("1960-01-01")
#max_date = pd.Timestamp("2073-12-31")
#future_period = st.date_input("Période future", min_value=min_date)

year = st.number_input("Année", value=2022, min_value=1960, max_value=2073, step=1)
month = st.number_input("Mois", value=1, min_value=1, max_value=12, step=1)
day = st.number_input("Jour", value=1, min_value=1, max_value=31, step=1)

futur_periods = datetime.datetime(year, month, day)

# Création d'un bouton predict qui retournera la prédiction du modèle 
if st.button("Predict"):
    prediction = inference(str(futur_periods))
    resultat = f"L'anomalie de température prévue est de : {prediction}"
    st.write(resultat)










