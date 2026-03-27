import streamlit as st

# Configuration de la page
st.set_page_config(page_title="VeloDesign - Boutique en Ligne", layout="wide")

# --- STYLE CSS (Noir et Blanc + Arial) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Arial:wght@400;700&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background-color: #ffffff;
        color: #000000;
        font-family: 'Arial', sans-serif;
    }

    h1, h2, h3, p {
        color: #000000 !important;
        font-family: 'Arial', sans-serif;
    }

    .stButton>button {
        background-color: #000000;
        color: #ffffff;
        border: 1px solid #000000;
        border-radius: 0px;
        font-family: 'Arial', sans-serif;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #ffffff;
        color: #000000;
    }

    header, [data-testid="stHeader"] {
        background-color: #ffffff;
    }
    
    hr {
        border-top: 1px solid #000000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DONNÉES DES PRODUITS ---
velos = [
    {"nom": "Vélo de Route Classique", "prix": "1 200 €", "desc": "Performance et légèreté."},
    {"nom": "VTT Tout-Terrain", "prix": "950 €", "desc": "Robuste pour les sentiers sauvages."},
    {"nom": "Vélo Urbain Électrique", "prix": "2 100 €", "desc": "L'élégance en ville sans effort."},
    {"nom": "Fixie Minimaliste", "prix": "600 €", "desc": "Style pur et entretien réduit."}
]

# --- HEADER ---
st.title("VÉLO / DESIGN")
st.subheader("L'essentiel du cyclisme, en noir et blanc.")
st.write("---")

# --- CATALOGUE ---
st.header("Notre Collection")

# Création de colonnes pour l'affichage des produits
cols = st.columns(2)

for i, velo in enumerate(velos):
    with cols[i % 2]:
        st.subheader(velo["nom"])
        st.write(f"**Prix : {velo['prix']}**")
        st.write(velo["desc"])
        if st.button(f"Ajouter au panier", key=i):
            st.success(f"{velo['nom']} ajouté !")
        st.write("---")

# --- FOOTER ---
st.sidebar.title("À propos")
st.sidebar.info("Boutique spécialisée dans les vélos haute performance au design épuré.")
st.sidebar.write("Contact : contact@velodesign.com")
