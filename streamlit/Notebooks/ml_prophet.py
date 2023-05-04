import streamlit as st
import numpy as np
import joblib
from datetime import date
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from prophet.plot import plot_plotly, plot_components_plotly

st.title("Prédiction des évolution d'anomalie de température avec Prophet")
st.subheader("Application du modèle additif de Prophet")

# Chargement du modèle
model = joblib.load(filename='./Notebooks/model_Prophet.joblib')

# Créez une interface utilisateur pour permettre à l'utilisateur de saisir la date
input_date = st.date_input("Sélectionnez une date :", value=pd.to_datetime('1960-01-01'), min_value=pd.to_datetime('1960-01-01'),
                          max_value=pd.to_datetime('2073-01-01'))

# Prédisez la température pour la date saisie
future = pd.DataFrame({'ds': [input_date]})
forecast = model.predict(future)

# Affichez la prévision de température pour la date saisie
st.write("La température prévue pour le mois de", input_date.strftime("%B %Y"), "est de", round(forecast['yhat'].values[0], 2), "degrés Celsius.")

# Prédire les valeurs pour toutes les dates de la période d'intérêt
future = model.make_future_dataframe(periods=600, freq='M')
forecast = model.predict(future)

# Renommer les colonnes 'ds' et 'y' en 'Année' et 'Anomalie de température'
#forecast = forecast.rename(columns={'ds': 'Année', 'y': 'Anomalie de température'})

# Tracer la prévision globale
fig1 = plot_plotly(model, forecast, xlabel='Année', ylabel='Anomalie de température en degré Celsius')
st.plotly_chart(fig1)

# Tracer les composantes de la prévision
fig2 = plot_components_plotly(model, forecast)
st.plotly_chart(fig2)
