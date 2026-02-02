import streamlit as st

st.title("Gestion de documents - Famille")
st.write("Bienvenue sur votre application sécurisée.")

# Un petit test pour voir si ça marche
nom = st.text_input("Quel est votre prénom ?")
if nom:
    st.write(f"Bonjour {nom}, l'application est prête à être développée !")
