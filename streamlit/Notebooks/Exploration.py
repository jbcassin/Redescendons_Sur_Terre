import streamlit as st
import pandas as pd
from PIL import Image

def Exploration():
    image2 = Image.open('streamlit/images/GlobalWarming_Lead.jpeg')
    st.image(image2)
    st.title("Exploration des données")
    st.subheader("Présentation des données")
    st.write("Pour cette étude, nous avons utilisé des jeux de données relatifs à la température terrestre et au taux de C02 dans l'atmosphère")
    st.info("Données de Berkeley")
    st.write("Pour l’analyse de la température terrestre, les jeux de données principalement utilisés proviennent du projet Berkeley Earth Project disponibles sur le site de l’Université de Berkeley https://berkeleyearth.org/data/")
    st.write("Les données proviennent des enregistrements des stations météo et sont supposées être représentatives d’une zone entourant chacune des stations météo formant l’ensemble de tous les points plus proches de cette station que de tout autre (algorithme de Voronoï). Comme les stations ne sont pas réparties de manière homogène et que leur nombre a considérablement évolué dans le temps, des « erreurs algorithmiques » sont associées à cette méthode de moyennage spatial.")
    st.write("La température moyenne (en fait son anomalie) est calculée en faisant la somme des données individuelles provenant des différentes stations et en attribuant à chaque point un poids proportionnel à la cellule correspondante (moyenne pondérée). Comme la taille des cellules a changé au fil du temps, le poids des points d’origine (les stations météo) a également changé, ce qui induit un biais dans le calcul de la valeur moyenne globale.")
    st.write("Les anomalies de température présentées dans les différents jeux de données sont une présentation chiffrée des écarts de températures par rapport aux moyennes sur la période 1951-1980.")
    st.write("Nous avons plusieurs jeux de données à notre disposition:")
    st.write("- Liste des variations de température globale (Terre uniquement) en degré Celsius de Janvier 1753 à Septembre 2022")
    st.write("- Liste des variations de température dans l'hémisphère nord (Terre uniquement) en degré Celsius de Janvier 1880 à Septembre 2022")
    st.write("- Liste des variations de température dans l'hémisphère Sud (Terre uniquement) en degré Celsius de Janvier 1880 à Septembre 2022")
    st.write("- Liste des variations de température dans chaque pays en degré Celsius (les périodes varient de pays en pays)")

    st.write("")
    st.markdown("**Aperçu du Dataframe**")
    # import Data
    df = pd.read_csv("Datasets/températures_globales_hémisphériques.csv", index_col=1)
    df.drop(columns=['Unnamed: 0'], axis=1, inplace=True)
    st.dataframe(df)
    
    
    
    st.info("Données de la NASA")
    st.write("En complément du jeu de données précédent, nous avons utilisé celui de GISS Surface Temperature Analysis que l’on peut trouver sur le site de la NASA: https://data.giss.nasa.gov/gistemp/ ")
    st.write("Les informations présentes dans les jeux de données sont similaires à celles que l’on a dans le jeu de Berkeley mais présentées sous une autre forme permettant une utilisation plus aisée pour certaines visualisations.")
    st.write("Nous utilisons pour notre étude 2 datasets:")
    st.write("- GLB.Ts+dSST (anomalies globales)")
    st.write("- ZonAnn.Ts+dSST (anomalies par zones hémisphériques et par tranche de latitudes)")
    st.write("Les anomalies de température présentées dans ce jeu de données sont une présentation chiffrée des écarts de températures par rapport aux moyennes sur la période 1951-1980, les anomalies ont été standardisées et les outliers supprimés.")

    st.write("")
    st.markdown("**Aperçu du Dataframe**")
    # import Data
    df = pd.read_csv("Datasets/ZonAnn.Ts+dSST.csv", index_col=0)
    st.dataframe(df)


    st.info("Données de Page2K")    
    st.write("Nous avons également utilisé les données scientifiques du PAGES2k Consortium 2019 qui fournit un support pour la collecte et la synthèse des observations, des reconstitutions et la modélisation des dynamiques climatiques, écosystémiques, environnementales et sociétales dans le passé. https://pastglobalchanges.org/science/wg/2k-network/intro ")
    st.write("le dataset se trouve sur cette page: https://web.archive.org/web/20200229093647/https://figshare.com/articles/Reconstruction_ensemble_median_and_95_range/8143094 ")
    st.write("Nous avons une nouvelle reconstitution de la température globale remontant à l'an 1AD grâce au travail de l'équipe PAGES2k. Cette reconstruction comprend des données provenant d'une grande variété d'enregistrements proxy tels que les cernes d'arbres, les dépôts de grottes, les coraux, etc.")


    st.write("")
    st.markdown("**Aperçu du Dataframe**")
    # import Data
    df = pd.read_table("Datasets/Full_ensemble_median_and_95pct_range_edit.txt", index_col=0)
    st.dataframe(df)


    st.warning("Données du Climate & Energy College")
    st.write("Nous avons utilisé les données scientifiques du Climate & Energy College qui est une équipe internationale de chercheurs en début de carrière. Le Collège mène des recherches sur les systèmes climatiques et énergétiques dans un environnement interdisciplinaire, faisant progresser les connaissances et éclairant les réponses aux défis complexes du changement climatique.")
    st.write("Ce centre de recherche de classe mondiale est situé à l'Université de Melbourne, en collaboration avec des instituts de recherche australiens et allemands de premier plan. Leurs recherches sont centrées sur le changement climatique et les transitions énergétiques. https://www.climatecollege.unimelb.edu.au/ ")
    st.write("le dataset se trouve sur cette page: https://www.climatecollege.unimelb.edu.au/cmip6 ")
    st.write("Il recense les taux de C02 dans l’atmosphère depuis l’année 0 jusqu’à l’année 2014. Il comprend 3 variables: le taux global, le taux dans l’hémisphère Nord et celui dans l'hémisphère Sud.")


    st.write("")
    st.markdown("**Aperçu du Dataframe**")
    # import Data
    df = pd.read_csv("Datasets/mole_fraction_of_carbon_dioxide_in_air_input4MIPs_GHGConcentrations_CMIP_UoM-CMIP-1-1-0_gr3-GMNHSH_0000-2014 2.csv", index_col=0)
    st.dataframe(df)





    st.warning("Données de Our World In Data")
    st.write("Pour aller plus loin dans l’analyse des émissions de C02, nous avons utilisé les données issues du projet Our World in Data du Global Change Data Lab. Cette organisation à but non lucratif basée au Royaume-Uni, partenaire du l’université d’Oxford à pour  mission de publier « la recherche et les données de milliers de chercheurs et spécialistes pour progresser contre les plus grands problèmes du monde ». https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions ")

    st.write("")
    st.markdown("**Aperçu du Dataframe**")
    # import Data
    df = pd.read_csv("Datasets/co2_par_pays.csv")
    st.dataframe(df)

    st.write("")
    st.caption("Liens vers les Datasets: https://github.com/jbcassin/Redescendons_Sur_Terre/tree/main/Datasets")
