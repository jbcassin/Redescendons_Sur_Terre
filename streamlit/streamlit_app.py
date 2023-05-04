# Import packages
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from PIL import Image


# Set page title and favicon
st.set_page_config(page_title="Redescendons_Sur_Terre_App", page_icon=":earth:")

            
    

# Create a sidebar menu 
with st.sidebar:
    #st.markdown()
    image_sidebar = Image.open('images/terre.png')
    st.image(image_sidebar)
    st.header("Redescendons sur Terre !")
    choice = option_menu(
        menu_title = "Menu",
        options=["Introduction", "Exploration des données", "Analyses et Visualisations", "Modélisation", "Conclusion", "Ressources"],
        #icons = [""]
        menu_icon="cast",
        default_index=0)
    
    
    st.write("Analyse réalisée par:")
    st.subheader("- Jean-Baptiste CASSIN")
    col1, col2= st.columns(2)
    with col1:
        st.markdown('<img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width=30>', unsafe_allow_html=True)
        st.write("[Linkedin](<https://www.linkedin.com/in/jb-cassin/>)")
    with col2:    
        st.markdown('<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width=30>', unsafe_allow_html=True)
        st.write("[Github](<https://github.com/jbcassin/>)")
    
    st.subheader("- Salim ABDELOUAHAB")
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width=30>', unsafe_allow_html=True)
        st.write("[Linkedin](<https://www.linkedin.com/in/salim-a-a71815192/>)")
    with col4:
        st.markdown('<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width=30>', unsafe_allow_html=True)
        st.write("[Github](<https://github.com/abdelouahab70/>)")
        
        
    st.subheader("- Thomas CHAULET")
    col5, col6 = st.columns(2)
    with col5:
        st.markdown('<img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width=30>', unsafe_allow_html=True)
        st.write("[Linkedin](<https://www.linkedin.com/in/salim-a-a71815192/>)")
    with col6:   
        st.markdown('<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width=30>', unsafe_allow_html=True)
        st.write("[Github](<https://github.com/abdelouahab70/>)")




# Import Pajes
from Notebooks.Introduction import Introduction  
from Notebooks.Exploration import Exploration  
from Notebooks.Visualisations import Visualisations
from Notebooks.Modelisations import Modelisations
from Notebooks.Conclusion import Conclusion
from Notebooks.Ressources import Ressources


# MENU
# Introduction
if choice == "Introduction":
    Introduction()

# Exploration des données
elif choice == "Exploration des données":
    Exploration()
   
# Analyse et Visualisations   
elif choice == "Analyses et Visualisations":
    Visualisations()
    
# Modélisation ML   
elif choice == "Modélisation":
    Modelisations()    
    
# Conclusion    
elif choice == "Conclusion":
    Conclusion()    
        
# Ressources            
else:
    Ressources()

    

