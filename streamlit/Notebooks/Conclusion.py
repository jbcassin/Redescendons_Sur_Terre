import streamlit as st
from PIL import Image


def Conclusion():
    image5 = Image.open('streamlit/images/PHOTO-Climate-Collage-Diagonal-Design-NOAA-Communications-NO-NOAA-Logo.jpeg')
    st.image(image5)
    st.title("Conclusion")
    st.write("Grâce à l’analyse de données, nous avons pu répondre aux questions de notre problématique et atteindre nos objectifs.")
    st.write("Nous avons confirmé que le réchauffement climatique est bien réel. Nous avons montré que l’augmentation des températures est apparue avec la révolution industrielle de la fin du XIXème siècle, phénomène qui s’est accéléré depuis les années 1970.")
    st.write("Tous les pays sont touchés par cette hausse des températures et ce sont principalement les pays de l'hémisphère Nord qui sont impactés. L’augmentation des émissions de CO2 sont très fortement corrélées avec l'augmentation des températures à la surface de la Terre. Les prédictions réalisées grâce au Machine Learning nous montre que les températures vont continuer à augmenter dans les prochaines années et que nous aurons plus de 2°C d’augmentation dans 50 ans.")
    st.write("Le réchauffement climatique est un phénomène global de transformation du climat qui a de nombreuses conséquences:")
    st.write("- Une augmentation des températures à cause du réchauffement climatique affecte l’ensemble de l’écosystème mondial et pas seulement la chaleur ressentie. La météo s’en trouve perturbée, avec une augmentation des phénomènes météorologiques extrêmes, des changements des modèles météorologiques habituels. Cela veut dire plus de tempêtes, plus d’inondations, plus de cyclones et de sécheresses.")
    st.write("- La capacité de régulation des océans est aussi affectée par une augmentation des températures. Si les températures globales augmentent de façon très importante, il y aura donc augmentation des niveaux des océans, mais aussi une acidification et une désoxygénation des zones océaniques. En outre, une acidification des océans trop prononcée pourrait limiter la capacité des mers de la planète à produire de l’oxygène et à stocker le CO2, et donc augmenter encore le réchauffement climatique. Mais cela peut aussi affecter des zones de forêts et les écosystèmes fragiles (barrière de corail, forêt amazonienne) ainsi que la biodiversité (les coraux, certains insectes et même des mammifères pourraient ne pas survivre).")
    st.write("- Sur la société et l’économie, le réchauffement climatique peut avoir potentiellement plusieurs conséquences : la capacité des sociétés à s’adapter à un nouveau climat, à adapter leurs infrastructures, notamment médicales, mais aussi leurs bâtiments. Le réchauffement climatique aura aussi des conséquences sur la santé publique, la capacité alimentaire des pays…")
    st.write("Il est temps de redescendre sur Terre et de faire les efforts nécessaires pour endiguer le réchauffement climatique.")
