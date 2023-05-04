import streamlit as st
from PIL import Image


def Ressources():
    image6 = Image.open('streamlit/images/terre.jpeg')
    st.image(image6)
    st.title("Ressources")
    st.write("Dernier rapport du GIEC: https://www.ipcc.ch/languages-2/francais/")
    st.write("Site de l'Université de Berkeley: https://berkeleyearth.org/data/")
    st.write("Site de la Nasa: https://data.giss.nasa.gov/gistemp/")
    st.write("Site de Page2K: https://pastglobalchanges.org/science/wg/2k-network/intro")
    st.write("Site de Our World In Data: https://ourworldindata.org/")
    st.write("Pour comprendre le calcul des températures: https://www.climato-realistes.fr/climat-biais-et-erreurs-mesure-temperatures-globales/")
