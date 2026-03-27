import streamlit as st

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="VÉLO • MOTO • TROTTINETTE | Noir & Blanc",
    page_icon="🚲",
    layout="wide"
)

# --- STYLE CSS PERSONNALISÉ (Noir et Blanc + Arial + Cartes Produits) ---
st.markdown("""
    <style>
    /* Import de la police Arial (par sécurité, même si souvent système) */
    @import url('https://fonts.googleapis.com/css2?family=Arial:wght@400;700&display=swap');

    /* Fond de l'application et couleur de texte globale */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #ffffff;
        color: #000000;
        font-family: 'Arial', sans-serif;
    }

    /* Titres et paragraphes */
    h1, h2, h3, h4, h5, h6, p, label {
        color: #000000 !important;
        font-family: 'Arial', sans-serif;
    }

    /* Style des boutons (Noir avec texte Blanc) */
    .stButton>button {
        background-color: #C1E8EB;
        color: #ffffff;
        border: 2px solid #000000;
        border-radius: 0px; /* Carré */
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
    }

    /* Survol des boutons (Inversion : Blanc avec texte Noir) */
    .stButton>button:hover {
        background-color: #ffffff;
        color: #000000;
        border: 2px solid #000000;
    }

    /* Style des "cartes" de produits */
    div[data-testid="stColumn"] {
        border: 1px solid #e0e0e0;
        padding: 15px;
        background-color: #ffffff;
        margin-bottom: 20px;
    }

    /* Forcer la hauteur des images pour l'alignement */
    [data-testid="stImage"] > img {
        object-fit: contain;
        height: 200px !important; /* Ajustez la hauteur selon vos besoins */
        width: 100%;
    }

    /* Masquer le menu Streamlit et le footer par défaut */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Ligne de séparation noire */
    hr {
        border: 0;
        border-top: 2px solid #000000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DONNÉES PRODUITS (Contient Vélos, Motos, Trottinettes) ---
# Note : Les images sont des placeholders génériques sur fond blanc.
produits = [
    {
        "categorie": "VÉLOS",
        "nom": "Vélo de Route 'Elegance'",
        "prix": "1 499 €",
        "image": "https://images.unsplash.com/photo-1485965120184-e220f15ef94a?q=80&w=600&auto=format&fit=crop", # Vélo générique fond clair
        "desc": "Cadre carbone léger, transmission fluide. Noir mat."
    },
    {
        "categorie": "VÉLOS",
        "nom": "VTT Tout-Terrain 'Roc'",
        "prix": "980 €",
        "image": "https://images.unsplash.com/photo-1576431959322-a9a3b6f849ff?q=80&w=600&auto=format&fit=crop", # VTT générique fond clair
        "desc": "Suspension intégrale, pneus crantés. Prêt pour l'aventure."
    },
    {
        "categorie": "MOTOS",
        "nom": "Moto Urbaine 'CityRider'",
        "prix": "5 200 €",
        "image": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?q=80&w=600&auto=format&fit=crop", # Moto custom sur fond clair
        "desc": "125cc, design néo-rétro pur. Idéale pour la ville."
    },
    {
        "categorie": "MOTOS",
        "nom": "Scooter Électrique 'E-Silenzio'",
        "prix": "3 800 €",
        "image": "https://images.unsplash.com/photo-1603714210659-331003f56977?q=80&w=600&auto=format&fit=crop", # Scooter blanc sur fond clair
        "desc": "Équivalent 50cc, autonomie 70km. Zéro émission."
    },
    {
        "categorie": "TROTTINETTES",
        "nom": "Trottinette 'Pégase LITE'",
        "prix": "650 €",
        "image": "https://images.unsplash.com/photo-1627931398851-933e4c0296c0?q=80&w=600&auto=format&fit=crop", # Trottinette sur fond blanc
        "desc": "Pliable, légère (12kg), vitesse 25km/h."
    },
    {
        "categorie": "TROTTINETTES",
        "nom": "Trottinette Pro 'Volta GT'",
        "prix": "1 150 €",
        "image": "https://images.unsplash.com/photo-1601053161474-129681329c66?q=80&w=600&auto=format&fit=crop", # Autre trottinette fond clair
        "desc": "Double moteur, autonomie 50km. Pneus 10 pouces."
    }
]

# --- EN-TÊTE DU SITE ---
st.write("# ⬛ MOBILITÉ / DESIGN")
st.write("### VÉLOS • MOTOS • TROTTINETTES")
st.write("L'esthétique épurée. La performance brute.")
st.markdown("---")

# --- FILTRES DE CATÉGORIE (Sidebar) ---
st.sidebar.title("CATEGORIES")
# Laisser Arial par défaut dans la sidebar
st.sidebar.write("Filtrer par type de véhicule :")
cats = ["Tous"] + sorted(list(set(p["categorie"] for p in produits)))
choix_cat = st.sidebar.radio("", cats)

st.sidebar.markdown("---")
st.sidebar.write("**Contact :** contact@mobilitedesign.com")
st.sidebar.write("Dakar, Sénégal")


# --- AFFICHAGE DU CATALOGUE ---
# Filtrer les produits selon le choix de la sidebar
if choix_cat == "Tous":
    produits_a_afficher = produits
else:
    produits_a_afficher = [p for p in produits if p["categorie"] == choix_cat]

st.header(f"Notre Collection {'' if choix_cat == 'Tous' else ': ' + choix_cat}")
st.write("") # Espace

# Création d'une grille de 3 colonnes pour les produits
cols = st.columns(3)

for i, prod in enumerate(produits_a_afficher):
    # On alterne les colonnes (0, 1, 2)
    with cols[i % 3]:
        # Affichage de l'image (l'image générique sur fond clair)
        st.image(prod["image"], use_column_width=True)
        
        # Détails du produit
        st.write(f"### {prod['nom']}")
        st.write(f"**{prod['categorie']}**")
        st.write(prod["desc"])
        st.write(f"## {prod['prix']}")
        
        # Bouton d'action
        if st.button(f"VOIR LE PRODUIT", key=f"btn_{i}_{prod['nom']}"):
            st.info(f"Détails pour {prod['nom']} bientôt disponibles.")
