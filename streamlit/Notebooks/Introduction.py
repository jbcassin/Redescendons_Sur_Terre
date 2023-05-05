import streamlit as st
from PIL import Image

def Introduction():
     image1 = Image.open('streamlit/images/rechauffement-climatique-illustration.jpeg')
     st.image(image1)
     st.title(" Redescendons sur Terre !")
     st.subheader("Analyse et modélisation du réchauffement climatique")
     st.write("réalisées par Jean-Baptiste CASSIN et Salim ABDELOUAHAB.")
     st.subheader("Problématique")
     st.error("Le réchauffement climatique est-il réel?")
     st.write((" Selon l’Organisation des Nations Unies, la période 2011-2020 a été la décennie la plus chaude jamais enregistrée."
          " En 2019, la température moyenne de la planète se situait 1,1 °C au-dessus des niveaux de l’ère préindustrielle."
          " Le réchauffement climatique dû aux humains augmente actuellement à un rythme de 0,2 °C par décennie."
          " L’utilisation de combustibles fossiles, la déforestation et l’élevage de bétail influent de plus en plus sur le climat et la température de la terre."
          " Ces activités libèrent d'énormes quantités de gaz à effet de serre, qui viennent s'ajouter à celles naturellement présentes dans l’atmosphère, renforçant ainsi l'effet de serre et le réchauffement de la planète."))
     st.write("Dans cette étude, nous allons nous poser les questions suivantes:")
     st.write("- Grâce aux données dont nous disposons, pouvons-nous confirmer le réchauffement climatique?")
     st.write("- Quel est l’évolution des températures sur différents points de la Terre sur une période de plusieurs centaines d’années?")
     st.write("- Les anomalies de températures sont-elles corrélées aux émissions de CO2?")
     st.write("- Pouvons-nous prédire l’évolution des températures dans les prochaines décennies?")
     st.subheader("Objectifs de notre étude")
     st.write("- Constater le dérèglement climatique global à l’échelle de la planète sur les derniers siècles et dernières décennies.")
     st.write("- Analyser par zone géographique pour voir les évolutions différentes.")
     st.write("- Comparer avec des phases d’évolution de température antérieure à notre époque.")
     st.write("- Comparer avec d’autres facteurs comme le taux de CO2 dans l’air.")
     st.write("- Modéliser et prédire des variations de températures sur plusieurs dizaines d’années")















