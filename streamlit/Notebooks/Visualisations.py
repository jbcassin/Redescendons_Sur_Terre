import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.subplots as sp
import plotly_express as px
import plotly.graph_objs as go
from streamlit_folium import st_folium
import altair as alt




def Visualisations():
    image3 = Image.open('streamlit/images/GettyImages-155141288-polar-bear-1200x630-2.jpeg')
    st.image(image3)
    st.title("Analyses et Visualisations")
  
    st.subheader("Analyse des anomalies de températures")
    st.write("Hypothèse: nous faisons l’hypothèse que les variations de températures enregistrées ont tendance à être positives, ce qui signifie que la température du globe à tendance à augmenter de manière générale. Nous essaierons de déterminer les zones où les températures ont tendance à le plus augmenter et à savoir si cette tendance haussière est homogène au fil du temps.")     
    st.info("Etude des anomalies globales")
   
    # selecteur pour slider
    values = [1, 2, 3]
    for i, value in enumerate(values):
        key = f"value_slider_{i}"
        
        
        
    ### Anomalies de la température globale et de l'incertitude
    ### Notebook Analyse Temp Globales + Hémisphèriques Berkeley
    
    # import Data
    df = pd.read_csv("Datasets/températures_globales_hémisphériques.csv", index_col=0)
    
    # Data Processing
    Temp_country_mean = df.groupby('Year').mean().reset_index()
    
    # Define the x values for the curves
    x = Temp_country_mean.Year
    # Define the two curves to plot
    y1 = Temp_country_mean['Anomaly-Gl']
    y2 = Temp_country_mean['Uncertainty-Gl']  

    # Ploting
    # Create the plot trace for the first curve
    trace1 = go.Scatter(x=x, y=y1, mode='lines', name='Anomalie', showlegend=True)

    # Create the plot trace for the second curve
    trace2 = go.Scatter(x=x, y=y2, mode='lines', name='Incertitude', visible=False, showlegend=True)

    # create the layout and add the traces
    layout = go.Layout(
        title="Anomalies de la température globale et de l'incertitude de 1753 à 2022",
        xaxis=dict(title='Année'),
        yaxis=dict(title='Valeur', range=[-3, 3.5]),
        updatemenus=[dict(
            type='buttons',
            buttons=[dict(
                label="Afficher l'Incertitude",
                method='update',
                args=[{'visible': [True, not trace2.visible]}],
                args2=[{'visible': [True, trace2.visible]}],
            )]
        )]
    )

    # create the figure and plot it
    fig = go.Figure(data=[trace1, trace2], layout=layout)

    # define a callback function to update the layout
    def update_layout(trace, points, state):
        if trace.name == 'Incertitude':
            fig.layout.title = 'Anomalies de températures globales et Incertitude (Incertitude is ' + ('visible' if trace.visible else 'hidden') + ')'

    # add the callback function to the figure
    fig.data[0].on_click(update_layout)
    fig.data[1].on_click(update_layout)
    st.write(fig)
    
    
    
    st.write("Nous constatons que l’incertitude était très élevée lors des premières mesures, ici 1753 et qu’elle a grandement diminué pour être pratiquement nulle depuis les années 1960. Cela est dû au fait que les équipements de mesures sont de plus en plus précis et que leur fiabilité est croissante.")
 
 
 
 
    ### Anomalies des températures hémisphériques et des incertitudes   
    # Define the two curves to plot
    y1 = Temp_country_mean['Anomaly-NH']
    y2 = Temp_country_mean['Uncertainty-NH']  
    y3 = Temp_country_mean['Anomaly-SH']
    y4 = Temp_country_mean['Uncertainty-SH']


    # Create the plot trace for the first curve
    trace1 = go.Scatter(x=x, y=y1, mode='lines', name='Anomalie Hémisphère Nord', line=dict(color='blue'), showlegend=True)

    # Create the plot trace for the second curve
    trace2 = go.Scatter(x=x, y=y2, mode='lines', name='Incertitude Hémisphère Nord', line=dict(color='green'), visible=False, showlegend=True)

    # Create the plot trace for the first curve
    trace3 = go.Scatter(x=x, y=y3, mode='lines', name='Anomalie Hémisphère Sud', line=dict(color='orange'), showlegend=True)

    # Create the plot trace for the second curve
    trace4 = go.Scatter(x=x, y=y4, mode='lines', name='Incertitude Hémisphère Sud', line=dict(color='purple'), visible=False, showlegend=True)


    # create the layout and add the traces
    layout = go.Layout(
        title='Anomalies des températures hémisphériques et des incertitudes de 1840 à 2022',
        xaxis=dict(title='Année', range=[1840, max(x)]),
        yaxis=dict(title='Valeur', range=[-1.5, 2]),
        updatemenus=[dict(
            type='buttons',
            buttons=[dict(
                label="Afficher l'Incertitude",
                method='update',
                args=[{'visible': [True, False, True, False]}],
                args2=[{'visible': [True, True, True, True]}],
            )]
        )]
    )

    # create the figure and plot it
    fig = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)

    # define a callback function to update the layout
    def update_layout(trace, points, state):
        if trace.name == 'Incertitude':
            fig.layout.title = 'Anomalies de températures globales et Incertitude (Incertitude is ' + ('visible' if trace.visible else 'hidden') + ')'

    # add the callback function to the figure
    fig.data[0].on_click(update_layout)
    fig.data[3].on_click(update_layout)
    st.write(fig)
  
    st.write("Comme pour le graphe précédent, l’incertitude était très importante au moment des premières mesures mais elle a beaucoup diminué au fur et à mesure du temps. Les données ont été collectées plus tôt dans l’hémisphère Nord et nous constatons, comme avec les données de la NASA que l’hémisphère Nord est plus impacté par le réchauffement climatique que l’hémisphère Sud")
    st.write("Nous constatons que la variation des températures est à la hausse depuis 1880, c'est-à-dire la fin de la Révolution Industrielle.. Après la fin de cette période et la fin de l’utilisation massive du charbon, la température a légèrement diminué; mais à partir de 1910 la température a suivi une courbe légèrement exponentielle à la hausse. Cette tendance haussière s’est accentuée à partir des années 1970. La crise COVID a légèrement influé sur les températures à court terme mais sur le long terme, la tendance reste la même. Cette augmentation est homogène et suit la même évolution quelque soit la zone et le mois de l’année.")
    st.write("Nous constatons également que cette hausse est plus élevée dans l’hémisphère nord que dans l’hémisphère sud. Et enfin nous constatons que c’est aux pôles que les variations de températures sont les plus importantes et c’est au pôle Nord que les températures ont le plus augmenté.")
    
    st.write("Avec le graphique suivant, vous pouvez choisir l'année et avoir un aperçu des anomalies sur les mois de l'année. Vous constaterez que les anomalies ont tendance à augmenter quel que soit le mois.")
    
    # import Data
    df_temp_pays = pd.read_csv("Datasets/Températures_par_pays_Vertical.csv")
    
    # Data Processing
    # Calcul de température moyenne par pays
    Temp_country_mean = df_temp_pays.groupby(['Country', 'Year']).mean().reset_index()
    # Selection de l'année à partir de 1880
    Temp_country_mean = Temp_country_mean[Temp_country_mean['Year'] >= 1880]
    # create a dictionary to map numeric values to month names
    month_names = {1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril', 5: 'Mai', 6: 'Juin',
                   7: 'Juillet', 8: 'Aout', 9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'}

    # replace numeric values in Month column with month names
    df['Month_str'] = df['Month'].replace(month_names)
    
    ### Diagramme polaire des Anomalies de température par mois
    # create subplots with polar charts   
    fig = make_subplots(rows=1, cols=1, subplot_titles=('',),
                        specs=[[{'type': 'polar'}]])

    # create traces for each year, with a slider to select the year
    for i, year in enumerate(df['Year'].unique()):
        trace = go.Scatterpolar(r=df[df['Year']==year]['Anomaly-Gl'],
                                theta=df[df['Year']==year]['Month_str'],
                                name=str(year), # convert Year in string
                                visible=(i==0), # set first year to visible
                                showlegend=False)
        fig.add_trace(trace)

    # adjust polar plot layout
    fig.update_layout(polar=dict(radialaxis=dict(range=[-3, 3])),
                      updatemenus=[dict(type='buttons',
                                        showactive=False,
                                        buttons=[dict(label='Play',
                                                      method='animate',
                                                      args=[None, {'frame': {'duration': 100, 'redraw': True},
                                                                   'fromcurrent': True,
                                                                   'transition': {'duration': 0}}]),
                                                 dict(label='Pause',
                                                      method='animate',
                                                      args=[[None], {'frame': {'duration': 0, 'redraw': False},
                                                                     'mode': 'immediate',
                                                                     'transition': {'duration': 0}}])])],
                      sliders=[dict(active=0,
                                     yanchor='top',
                                     xanchor='left',
                                     currentvalue=dict(font=dict(size=16), prefix='Year: ', visible=True, xanchor='right'),
                                     pad=dict(t=35, r=20),
                                     len=0.9,
                                     steps=[dict(label=str(year),
                                                 method='update',
                                                 args=[{'visible': [(i == j) for j in range(len(df['Year'].unique()))]},
                                                       {'title': "Anomalies de température globales pour l'année {}".format(year)}])
                                            for i, year in enumerate(df['Year'].unique())])])

    fig.update_layout(width=700, height=480)
    st.write(fig)




    st.write(" ")
    st.markdown("**Analyse des anomalies de température depuis 2000 ans**")
    st.write("A partir des données PAGES2K, nous vons obtenu le graphique suivant qui montre les anomalies de températures depuis l'année 0 jusqu'en 2014.")
    st.write("Visualisation avec uniquement les valeurs de la Full Ensemble Median ainsi que la moyenne filtrée sur une période de 31 ans (31-year filtered full ensemble median)")
    image_pages2K = Image.open('Graphs/Courbe Temp depuis 2000 ans V2.png')
    st.image(image_pages2K)
    st.write("Nous constatons que la courbe est assez plate pendant le 1er millénaire, avec une légère hausse vers la période 1000-1200 puis une baisse allant d’environ 1500 à 1800, puis une montée très prononcée à partir du 20 ème siècle.")
    st.write("Les données montrent que la période moderne est très différente de ce qui s'est passé dans le passé. La période chaude médiévale et le petit âge glaciaire souvent cités sont des phénomènes réels, mais petits par rapport aux changements récents.")
    st.write("Le réchauffement au cours des 50 dernières années est brutal par rapport aux variations qui se sont produites naturellement au cours des 2000 dernières années.")
    st.write(" ")





    # import Data
    df_temp_pays = pd.read_csv("Datasets/Températures_par_pays_Vertical.csv")
    
    # Data Processing
    # Calcul de température moyenne par pays
    Temp_country_mean = df_temp_pays.groupby(['Country', 'Year']).mean().reset_index()
    # Selection de l'année à partir de 1880
    Temp_country_mean = Temp_country_mean[Temp_country_mean['Year'] >= 1880]
    # create a dictionary to map numeric values to month names
    month_names = {1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril', 5: 'Mai', 6: 'Juin',
                   7: 'Juillet', 8: 'Aout', 9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'}

    # replace numeric values in Month column with month names
    df['Month_str'] = df['Month'].replace(month_names)

    
    st.text("")
    st.info("Etude des anomalies par pays")


    st.text("")
    st.write("Avec le sélecteur suivant, vous pouvez afficher les anomalies de température par pays.")
    
    
    # Creation d'un selecteur mulit-pays pour afficher les courbes de températures
    countries = st.multiselect('Sélectionner un ou plusieurs pays', Temp_country_mean['Country'].unique())

    # Filter the data by selected countries
    df_countries = Temp_country_mean[Temp_country_mean['Country'].isin(countries)]

    # Create a line plot of temperature anomaly and CO2 for selected countries
    fig = go.Figure()
    for country in countries:
        df_temp = df_countries[df_countries['Country'] == country]
        fig.add_trace(go.Scatter(x=df_temp['Year'], y=df_temp['Anomaly'], name=f'{country}'))
    fig.update_layout(title='Anomalies de températures', xaxis_title='Anomalies', yaxis_title='Valeur')
    st.plotly_chart(fig)
    st.text("")
    

   
    st.write("Nous constatons que les tendances des anomalies de températures sont sensiblement identiques sur tous les pays et que ce phénomène est donc globale dans le temps.")
    
   
  
  
    ### Données par pays
    ### Notebook Analyse Température par pays - Cartes interactives
    
    
    # creation d'une fonction pour créer une colonne classe en fonction des variations
    def map_anomaly(x):
        if x < 1:
            return 'moins de 1°'
        elif x < 2:
            return '1° à 2°'
        elif x < 3:
            return '2° à 3°'
        else:
            return 'plus de 3°'

    # use the apply() function to create a new column based on the values in the 'Anomaly' column
    Temp_country_mean['Classe'] = Temp_country_mean['Anomaly'].apply(map_anomaly)

    # Pays avec les anomalies les plus importantes
    top_15 = Temp_country_mean.groupby('Country').sum().sort_values('Anomaly', ascending=False)[:15].reset_index()['Country']

    # Pays avec les anomalies les moins importantes
    bottom_15 = Temp_country_mean.groupby('Country').sum().sort_values('Anomaly', ascending=True)[:15].reset_index()['Country']
    
    st.write("")
    st.write("A partir des données à notre disposition, nous avons sélectionner 30 pays, 15 pays les plus impactés et 15 pays les moins impactés. La sélection a été réalisée à partir de la valeur moyenne des anomalies de températures.")
    st.write("Vous pouvez voir un aperçu des pays les plus et les moins impactés par le changement climatiques. Avec les 2 graphiques suivants, nous voyons que la hausse des températures affectent tous les pays, sur tous les continents.")
    # Visualisation des anomalies de température pour les pays les plus impactés
    Temp_country_mean_top = Temp_country_mean[Temp_country_mean['Country'].isin(top_15)]
    fig = px.bar(Temp_country_mean_top, x='Anomaly', y='Country', animation_frame='Year', hover_name='Anomaly',
    range_x=[-3,4],color='Country', labels={
                  "Anomaly": "Anomalie",
                  "Country": "Pays"}, title = "Anomalies de température pour les 15 pays les plus impactés",width=800, height=500)
    fig.update_layout(showlegend=False)
    st.write(fig)
 
    # Visualisation des anomalies de température pour les pays les moins impactés
    Temp_country_mean_bottom = Temp_country_mean[Temp_country_mean['Country'].isin(bottom_15)]
    fig = px.bar(Temp_country_mean_bottom,x='Anomaly', y='Country', animation_frame='Year', hover_name='Anomaly',
      range_x=[-3,4], color='Country', labels={
                            "Anomaly": "Anomalie", "Country": "Pays"},
          title = "Anomalies de température pour les 15 pays les moins impactés", width=800, height=500)
    fig.update_layout(showlegend=False)
    st.write(fig)
    

    st.write("Nous constatons que tous les pays sont impactés par la hausse des températures. Nous faisons l'hypothèse que la hausse est plus importante pour les pays les plus industrialisés de l'hémisphère Nord, tandis que les hausses les plus faibles sont constatés sur des territoires peu industrialisés et situé majoritairement dans l'hémisphère Sud.")
    st.write("")
   
    ### carte interactive
    st.markdown("**Carte interactive des anomalies de températures**")
    st.write("Avec la carte suivante, vous pouvez afficher les anomalies de températures en sélectionnant l'année. En zoomant et en pointant sur un pays, vous pouvez avoir une vision précise des anomalies à un instant T.")
    st.write("Choississez l'année pour voir les mesures:")
    # remplacement de noms de pays en corrélation avec les nom s dans notre fichier geaojson
    Temp_country_mean = Temp_country_mean.replace(to_replace=["Dominican", "Burma", "Bosnia And Herzegovina", "Czech Republic", 'United States', "Ivorycoast", "Congo (Democratic Republic Of The)", 'Tanzania'], value=["Dominican Republic", "Myanmar", "Bosnia and Herzegovina", "Czechia", "United States of America", "Ivory Coast", "Democratic Republic of the Congo", "United Republic of Tanzania"])
    
    

    
    # Create the slider for the year
    year = st.slider("Année", min_value=1880, max_value=2020, value=1880)
    
    # Filter the data by the selected year
    data = Temp_country_mean[Temp_country_mean["Year"] == year]
    
    # Create the figure
    fig = px.choropleth(data, 
                        locations="Country", 
                        locationmode="country names",
                        color="Anomaly",
                        color_continuous_scale=px.colors.sequential.Plasma_r,
                        range_color=[-2.5, 4],
                        labels={"Anomaly": "Anomalies de température en °C"})
    
    
    # Update the layout
    fig.update_layout(title=f"Anomalies de température pour l'année {year}", margin=dict(t=50, b=50),height=400)
    
    # Display the figure
    st.plotly_chart(fig)

    st.write("Nous constatons que globalement l'ensemble des pays subissent une hausse des températures. Cette évolution n'est pas similaire pour tous les pays et certains sont très touchés par le réchauffement climatique alors que d'autres le sont beaucoup moins.")
    st.write("A partir de l’analyse et de la visualisation des données, nous démontrons que la hausse des températures est apparue à la fin de la Révolution Industrielle, qu’elle s’est accentuée à partir des années 1970, quel que soit le mois de l’année. Les pays de l'hémisphère Nord sont les plus impactés car on trouve dans cette zone les pays les plus industrialisés. Le pôle Nord est l’endroit le plus impacté par le changement climatique.")












    
    ###Analyse du C02
    st.text("")
    st.subheader("Analyse des émissions de CO2")
    
    st.markdown("**Analyse du CO2 dans l’atmosphère**")
    st.write("Pour poursuivre dans notre étude du réchaffement climatique, nous avons fait l'hypothèse que la hausse des températures est liée à la hausse des gaz à effet de serre dans l'atmosphère.")
    
    st.write("Nous avons tout d'abord utilisé les données du Climate & Energy College. Après traitement des données nous faisons apparaître 2 graphiques:")
    st.write("Le 1er graphique montre le taux de C02 globale dans l’atmosphère depuis l’année 0. Ce taux était assez stationnaire mais nous constatons que depuis le début du 19ème siècle et l’avènement de la révolution industrielle le taux a très fortement augmenté.")
    image_co2_1 = Image.open('Graphs/C02 0 à 2020.png')
    st.image(image_co2_1)
    st.write("Le 2ème graphique est un zoom sur la période 1880 à 2014, période similaire à notre jeu de données sur les anomalies de températures.Ce graphique nous montre que le taux à très largement augmenté depuis 1880 avec une tendance haussière encore plus prononcée depuis 1960. Nous constatons également que le taux de CO2 est légèrement plus élevé dans le l’hémisphère Nord que dans le l’hémisphère Sud et que cet écart à tendance à augmenter au fil du temps.")
    image_co2_2 = Image.open('Graphs/C02 1880 à 2020.png')
    st.image(image_co2_2)
    
    
    st.markdown("**Emissions de CO2 par pays**")
    
    # import Data CO2
    df_co2 = pd.read_csv("Datasets/co2_par_pays.csv")
    
    #Data processing
    df_co2 = df_co2.rename({'country':'Country', 'year':'Year'}, axis=1)
    df_temp_co2 = Temp_country_mean.merge(right = df_co2, on = ['Year', 'Country'], how = 'outer')
    st.write("Avec le sélecteur suivant, vous pouvez afficher les émissions de C02 par pays.")

    # Creation d'un selecteur mulit-pays pour afficher les courbes de températures
    countries = st.multiselect('Sélectionner un ou plusieurs pays', df_co2['Country'].unique())

    # Filter the data by selected countries
    df_countries_co2 = df_co2[df_co2['Country'].isin(countries)]

    # Create a line plot of temperature anomaly and CO2 for selected countries
    fig = go.Figure()
    for country in countries:
        df_co2_2 = df_countries_co2[df_countries_co2['Country'] == country]
        fig.add_trace(go.Scatter(x=df_co2_2['Year'], y=df_co2_2['co2'], name=f'{country}'))
    fig.update_layout(title='Emissions de CO2', xaxis_title='Année', yaxis_title='Emissions en millions de tonnes')
    st.plotly_chart(fig)

    
    
    
    
    
    
    
    st.markdown("**Carte interactive des émissions de CO2**")
    st.write("Avec la carte suivante, vous pouvez afficher les émissions de CO2 en sélectionnant l'année. En zoomant et en pointant sur un pays, vous pouvez avoir une vision précise des émissions à un instant T.")

    st.write("Choississez l'année pour voir les mesures:")
    
           ### Carte interactive émissions de C02 par pays en fonction de l'année
    

    # Create the slider for the year
    year_co2 = st.slider("Année", min_value=1880, max_value=2021, value=1880)
    
    # Filter the data by the selected year co2
    data_2 = df_co2[df_co2["Year"] == year_co2]
    
    # Create the figure
    fig = px.choropleth(data_2, 
                        locations="Country", 
                        locationmode="country names",
                        color="co2",
                        color_continuous_scale=px.colors.sequential.Plasma_r,
                        range_color=[0, 8000],
                        labels={"co2": "Emissions de CO2 en millions de tonnes"})
    
    # Update the layout
    fig.update_layout(title=f"Emissions de CO2 pour l'année {year_co2}", margin=dict(t=50, b=50),height=400)
    
    # Display the figure
    st.plotly_chart(fig)

    
    st.write("Le taux de C02 dans l’atmosphère suit les mêmes tendances que les anomalies de C02. Ce n’est qu’à partir de la fin du XIXème siècle que le taux de CO2 à commencer à fortement augmenté, porté par la Révolution Industrielle et le développement des pays industrialisés.Ces émissions de CO2 n’ont rien d'égal avec ce que la terre a connu depuis 2 millénaires. Nous allons donc nous pencher un peu plus sur la relation entre anomalies de températures et émissions de C02.")
    st.write("")
    st.write("")








    ### Notebook: Analyse CO2 par pays V2
    st.write("L’évolution des émissions de CO2 dans les grands pays industrialisés et les grands pôles d’activités n’est pas la même. Dans les pays d’Europe et les Etats-Unis, les émissions de CO2 ont globalement reculées, contrairement à la Chine ou l’Asie.")
    st.write("Pour les pays avec un taux de revenu élevé (High-income countries), les émissions sont plus importantes, mais depuis 2008 et le choc économique les émissions ont baissé. Pour les pays avec un plus faible taux de revenu (Upper-middle-income et lower-middle-income countries), les émissions étaient très faibles avant 1945 mais elles ont très fortement augmenté depuis, sans pour autant atteindre celle de l’autre groupe de pays. On constate une inflexion sur l'ensemble des courbes despays lors de la crise du COVID-19.")
    st.write("Si l'on observe l’évolution des émissions des membres de l’OCDE, celle-çi est très similaire à celle des pays ayant le plus de revenus. Elle suit une tendance haussière jusqu’en 2008 puis à tendance à baisser. Alors que la courbe des pays non-membres suit une tendance haussière exponentielle, portée principalement par les émissions de la Chine. A partir du début des années 2000, ceux ce sont désormais les pays non-membres de l’OCDE qui sont les plus émetteurs de CO2.")
    st.write("")
    
    
    ### Comparaison C02 et température
    st.subheader("Comparaison entre les anomalies de température et les émissions de C02")    
    st.write("Dans ce graphique, nous superposons le taux de CO2 et les anomalies de température sur la période de 1880 à nos jours en mergeant ce dataset avec celui des températures globales de la Nasa (GLB.Ts+dSST). Nous constatons que les 2 courbes suivent la même tendance haussière avec la même inflexion vers le haut depuis le milieu du XXème siècle. Il y a donc de très fortes probabilités que ces 2 paramètres soient liés et que la hausse du taux de gaz à effet de serre dans l’atmosphère contribue à faire augmenter la température à la surface du globe. Nous décidons d’utiliser une méthode statistique pour montrer la corrélation entre la hausse des températures et l'augmentation des émissions de CO2. Nous avons donc effectué un test de corrélation de Pearson entre le taux de CO2 globale et les anomalies globales de température.")
    image_co2_3 = Image.open('Graphs/C02+Temp 1880 à 2020.png')
    st.image(image_co2_3)    
    st.write("Nous obtenons les résultats de corrélation suivants:")
    st.write("Coefficient de corrélation: 0.9276260482581129")
    st.write("P Value : 9.717225418853804e-59")
    st.write("Les résultats prouvent qu’il existe une forte corrélation positive et statistiquement significative  entre le taux de CO2 et les anomalies de température.")
    
    st.write("")
    st.markdown("**Anomalies de température et émissions de CO2 par pays**")

    st.write("Avec le graphique interactif suivant, vous pouvez comparer les anomalies de températures et les émissions de CO2 en sélectionnant le pays.")


    # Create the multi-select widget for the countries
    countries = st.multiselect("Sélectionner un ou plusieurs pays", df_temp_co2["Country"].unique())
    
    # Filter the data by the selected countries
    data_co2_temp = df_temp_co2[df_temp_co2["Country"].isin(countries)]
    
    chart_anomaly = (
        alt.Chart(data_co2_temp)
        .mark_line(color="red")
        .encode(
            x="Year:O",
            y=alt.Y("Anomaly:Q", scale=alt.Scale(domain=[-2, 4])),
            color=alt.Color("Country:N", legend=alt.Legend(title="Pays"))
        )
        .properties(width=300, height=350, title="Anomalies de températures")
    )

    chart_co2 = (
        alt.Chart(data_co2_temp)
        .mark_line(color="blue")
        .encode(
            x="Year:O",
            y=alt.Y("co2:Q", scale=alt.Scale(domain=[0,11000])),
            color=alt.Color("Country:N", legend=alt.Legend(title="Pays"))
        )
        .properties(width=300, height=350, title="Emissions de co2 en millions de tonnes")
    )

    # Display charts
    st.altair_chart(chart_anomaly | chart_co2)









    st.write("Cette étude des émissions de CO2 nous montre que les anomalies de température sont très fortement liées à la hausse des émissions de CO2 au niveau mondial. On constate que des pays ont fait des efforts pour réduire leurs émissions de CO2 mais la montée en puissance de la Chine et des pays en voie de développement a contrebalancé ce phénomène. La hausse des émissions est croissante et ce phénomène va sûrement provoquer une hausse de la température globale de la Terre.")



































    
    
    
    

