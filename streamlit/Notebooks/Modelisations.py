import streamlit as st
from PIL import Image
import numpy as np
import joblib
import datetime 
import pandas as pd
import sklearn
from prophet import Prophet
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from prophet.plot import plot_plotly, plot_components_plotly


def Modelisations():
    image4 = Image.open('images/climate-change-tree.jpeg')
    st.image(image4)
    st.title("Modélisation")
    
    st.write("Pour aller plus loin dans notre étude, nous décidons d’utiliser des techniques de Machine Learning avec de prédire les évolutions de températures sur plusieurs dizaines d’années.")
    st.write("Afin de trouver les meilleures prédictions possibles, nous avons testé 2 modèles différents, pour ainsi voir quel était le plus performant.")

    st.write("Pour chacun de modèles nous avons utilisé les données de Berkeley avec notre jeu de données:  températures_globales.csv")

    st.write("Nous avons vu plus haut que l’incertitude des anomalies de températures était pratiquement faible à partir des années 1960 et nous avons décidé d’utiliser les données seulement à partir du 1er Janvier 1960.")
    
    st.info("Préparation des données")
    
    st.write("Nous avons procédé à quelques transformations sur les données. Tout d’abord, nous avons transformé au format DateTime les variables temporelles pour faciliter leurs utilisations.")

    st.write("Puis nous avons séparé les données Test et Train en fonction de la date.")
    st.write("Données Train : du 01/01/1960 au 31/12/2009")
    st.write("Données Test : du 01/01/2010 au 30/11/2022")


    st.subheader("Machine Learning avec régression linéaire polynomiale d'ordre 1")

    st.error("Préparation de notre modèle")
    
    st.write("Nous avons utilisé la fonction GridSearchCV pour trouver les meilleurs paramètres à notre régression. Le meilleur hyperparamètre que nous avons obtenu est le Polynomial Features Degree d’ordre 1.")

    st.write("Nous avons procédé à 2 tests:")
    st.write("- Prédiction sur les données d'entraînement")
    st.write("- Prédiction sur les données de test")
    st.write("Nous obtenons le graphique suivant:")
    
    image_reg_1 = Image.open('Graphs/Anomalies de température avec prédictions - Regression Polynomiale.png')
    st.image(image_reg_1)

    st.write("Nous avons procédé au calcul des métriques de performance.")

    st.markdown("**Performances du modèle sur l'ensemble d'entraînement :**") 
    st.write("MAE : 0.26096916098541445")
    st.write("MSE : 0.11189778207153495")
    st.write("RMSE : 0.33451125851237795")
    st.write("R² : 0.5014505205687894")

    st.markdown("**Performances du modèle sur l'ensemble de test :**") 
    st.write("MAE : 0.2394088342016738")
    st.write("MSE : 0.10693830147168185")
    st.write("RMSE : 0.3270142221244847")
    st.write("R² : 0.5014505205687894")

    st.write("La MAE représente l'erreur moyenne absolue entre les prédictions et les valeurs réelles. Dans les deux cas, la MAE est relativement faible, ce qui indique que le modèle est capable de prédire avec précision les anomalies de température pour les données d'entraînement et de test.")
    st.write("La MSE représente la moyenne des carrés des erreurs entre les prédictions et les valeurs réelles. La MSE est également relativement faible pour les deux ensembles de données, ce qui indique que les erreurs sont faibles.")
    st.write("Le RMSE est simplement la racine carrée de la MSE. Il mesure également l'erreur moyenne entre les prédictions et les valeurs réelles, mais donne plus de poids aux erreurs les plus importantes. Le RMSE est relativement faible dans les deux cas, ce qui suggère que le modèle est capable de prédire avec précision les anomalies de température.")
    st.write("Le coefficient de détermination (R²) mesure la proportion de la variance totale de la variable de réponse (anomalies de température) qui est expliquée par le modèle. Dans ce cas, le R² est de 0,5014 pour l'ensemble d'entraînement et de test. Cela indique que le modèle explique environ 50 % de la variance totale, ce qui n'est pas très élevé mais peut être considéré comme acceptable.")
    
    st.write("")
    st.write("")
    st.success("Prédictions")
    st.write("Nous avons ensuite testé notre modèle afin de prédire les anomalies de températures sur une période de prédictions sur 50 ans, c'est-à-dire du 01/12/2022 au 31/12/2073. ")
    st.write("Vous pouvez afficher le résultat des prédictions en sélectionnant l'année, le mois et le jour.")
    
    
    
    # Chargement
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
    
    st.markdown("**Saisissez une date:**")


    year = st.number_input("Année", value=2023, min_value=1960, max_value=2073, step=1)
    month = st.number_input("Mois", value=1, min_value=1, max_value=12, step=1)
    day = st.number_input("Jour", value=1, min_value=1, max_value=31, step=1)

    futur_periods = datetime.datetime(year, month, day)


    st.write("**Cliquez sur le bouton 'Predict' pour voir la prédiction:**")
    
    # Création d'un bouton predict qui retournera la prédiction du modèle 
    if st.button("Predict"):
        prediction = inference(str(futur_periods))
        resultat = f"L'anomalie de température prévue est de {prediction} en °C"
        st.write(resultat)
    
    st.write("")
    st.warning("Conclusion")
    st.write("Dans l'ensemble, les métriques de performance suggèrent que le modèle de régression polynomiale est capable de prédire avec précision les anomalies de température pour les 50 prochaines années. Cependant, le faible coefficient de détermination suggère qu'il pourrait y avoir des facteurs non linéaires qui influencent les anomalies de température et qui ne sont pas pris en compte par le modèle. Il est donc important de prendre en compte ces résultats avec précaution et de continuer à améliorer le modèle en utilisant des approches plus sophistiquées. Avec ce graphique, nous constatons visuellement que ce modèle suggère une hausse d’environ 2,4°C des températures dans plus de 50 ans.")

    
    
    
    
    
    
    
    
    
    st.write("")
    st.subheader("Machine Learning avec Facebook Prophet")
    
    st.write("Nous avons par la suite décidé d'utiliser le modèle de Machine Learning développé par Facebook, Prophet. D'après Facebook, ce modèle est très adapté aux Time Series et pour les prévisions dans le temps.")
    
    st.info("Préparation des données")

    st.write("Nous avons procédé à quelques transformations sur les données. Tout d’abord, nous avons transformé au format DateTime les variables temporelles pour faciliter leurs utilisations.")  
    
    st.write("Pour l’utilisation du Facebook Prophet, nous devons suivre un cahier des charges précis concernant la préparation des données et les étapes de modélisation pour arriver à un résultat probant.")
    
    st.write("La variable de temps doit être sous le nom ds et l’anomalie sous le nom y. Nous faisons volontairement le choix de diviser les données en 90% pour l’ensemble d'entraînement  et de 10% pour l’ensemble de test.") 

    st.write("Puis nous avons séparé les données Train et Test en fonction de la date.")
    st.write("- Données Train: du 01/01/1960 au 31/01/2014")
    st.write("- Données Test: du 01/01/2015 au 30/11/2022")

    st.error("Préparation de notre modèle")
    
    st.write("Nous créons un modèle Prophet avec des hyperparamètres par défaut : modele additif") 
    st.markdown("**model = Prophet(seasonality_mode='additive')**")
    st.write("Puis nous faisons une prédiction sur 50 ans:")
    st.markdown("**future = model.make_future_dataframe(periods=50*12, freq='M')**")        
    st.markdown("**forecast = model.predict(future)**")
    
    #st.write("Nous obtenons le graphique suivant:")

    #image_prophet_1 = Image.open("Graphs/Anomalies de température avec prédictions jusqu'à 2015 - Prophet.png")
    #st.image(image_prophet_1)

    st.write("")    
    st.write("Notre modèle de prédiction suit fortement la courbe des températures réelles.")
    
    st.markdown("**Performances du modèle sur le jeu d'entraînement :**")
    st.write("MAE :  0.24032665570363626")
    st.write("MSE :  0.09662258273358046")
    st.write("RMSE :  0.31084173261256354")
    st.write("R²   :  0.601853008358856")
    
   
    st.write("")
    st.write("Les métriques de performance du modèle Prophet suggèrent que le modèle est capable de faire des prédictions précises pour les anomalies de température dans les 50 années à venir. Cependant, il est important de noter que ces métriques ne fournissent qu'une indication de la performance du modèle et qu'il est toujours important de vérifier la qualité des prédictions à l'aide d'autres outils et méthodes.") 
    
    st.write("En calculant les prédictions sur 50 ans nous obtenons le graphique suivant:")

    image_prophet_2 = Image.open('Graphs/Anomalies de température avec prédictions + 50 ans - Prophet.png')
    st.image(image_prophet_2)
    
    st.success("Prédictions")
    st.write("Nous avons ensuite testé notre modèle afin de prédire les anomalies de températures sur une période de prédictions sur 50 ans, c'est-à-dire du 01/12/2022 au 31/12/2072. ")

    st.markdown("Nous constatons une évolution constante à la hausse des températures depuis 1960.")

    st.write("")
    st.write("Vous pouvez afficher le résultat des prédictions en sélectionnant l'année, le mois et le jour.")
    
    # Chargement du modèle
    model = joblib.load(filename='./Notebooks/model_Prophet.joblib')
    
    st.markdown("**Saisissez une date:**")

    # Créez une interface utilisateur pour permettre à l'utilisateur de saisir la date
    input_date = st.date_input("", value=pd.to_datetime('1960-01-01'), min_value=pd.to_datetime('1960-01-01'),
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

    # présentation des prédictions sur 50 ans à partir de 2015
    st.markdown("La prédiction débute à compter de 2015 , la période 2015 à 2022 a été la période test pour mesurer la performance du modèle.")

    # Tracer la prévision globale
    fig1 = plot_plotly(model, forecast, xlabel='Année', ylabel='Anomalie de température en degré Celsius')
    st.plotly_chart(fig1)

    st.markdown("Cette visualisation fait ressortir les 2 composantes de la prédiction : la tendance et la saisonnalité.")
    st.markdown("Nous constatons un effect saisonnier : avec des hivers plus froids et des étés sont plus chauds.")
    # Tracer les composantes de la prévision
    fig2 = plot_components_plotly(model, forecast)
    st.plotly_chart(fig2)


    st.warning("Conclusion")
    st.write("Le modèle Facebook Prophet nous a permis de déterminer que la hausse des températures allait se poursuivre, et la prévision est d’environ +2,6°C dans 50 ans.")
    st.write("Nous constatons que le modèle confirme une évolution à la hausse des températures sans modification de notre mode de vie.")
    st.write("En comparaison avec le modèle préditif du GIEC qui prévoit par exemple +1.5°c d'ici 2030-2052 ,notre modèle prévoit +2.16°c .")
    st.write("Notre modèle confirme l'augmentation de température, la précision est modeste, nous emettons l'hypothèses que notre modèle avec d'autres features comme par exemple les émissions de CO2 aurait permi une meilleur prédiction.")    
    
    
