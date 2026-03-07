"""
TransportPro — Application principale
Outil de gestion financiere pour les transporteurs routiers.
"""

import streamlit as st

st.set_page_config(
    page_title="TransportPro",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
        .stApp { font-family: 'DM Sans', sans-serif; }
        html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0a0f1a 0%, #111827 100%);
            border-right: 1px solid rgba(30, 58, 95, 0.5);
        }
        [data-testid="stMetricValue"] {
            font-family: 'JetBrains Mono', monospace;
            font-size: 1.7rem; font-weight: 600; letter-spacing: -0.02em;
        }
        [data-testid="stMetricLabel"] {
            font-size: 0.78rem; text-transform: uppercase;
            letter-spacing: 0.06em; color: #8899aa !important;
        }
        div[data-testid="metric-container"] {
            background: rgba(17, 24, 39, 0.6);
            border: 1px solid rgba(30, 58, 95, 0.4);
            border-radius: 8px; padding: 1rem 1.2rem;
        }
        .stFormSubmitButton > button {
            background: linear-gradient(135deg, #1B6EC2 0%, #1557a0 100%);
            color: white; font-family: 'DM Sans', sans-serif;
            font-size: 0.95rem; font-weight: 600;
            padding: 0.65rem 2rem; border: none; border-radius: 6px;
        }
        .stFormSubmitButton > button:hover {
            background: linear-gradient(135deg, #1557a0 0%, #0e4a8a 100%);
            box-shadow: 0 4px 12px rgba(27, 110, 194, 0.3);
        }
        .stNumberInput > div > div > input {
            font-family: 'JetBrains Mono', monospace; font-size: 0.9rem;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container { padding-top: 1.5rem; max-width: 1200px; }
        hr { border-color: rgba(30, 58, 95, 0.3); }
        .brand-name { font-family: 'DM Sans', sans-serif; font-size: 1.5rem; font-weight: 700; color: #e2e8f0; letter-spacing: -0.03em; }
        .brand-name span { color: #1B6EC2; }
        .section-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.12em; color: #64748b; font-weight: 600; margin-bottom: 0.5rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown('<div style="text-align:center;padding:1.2rem 0;"><div class="brand-name">Transport<span>Pro</span></div><div style="width:40px;height:2px;background:#1B6EC2;margin:0.8rem auto;"></div><div style="font-size:0.7rem;color:#64748b;text-transform:uppercase;letter-spacing:0.15em;">Gestion financiere transport</div></div>', unsafe_allow_html=True)
    st.divider()
    page = st.radio("Nav", ["Accueil", "Calculateur Cout/km", "Rentabilite Tournees", "Dashboard Financier"], label_visibility="collapsed")
    st.divider()
    if "resultat_km" in st.session_state:
        r = st.session_state["resultat_km"]
        st.markdown(f'<div style="padding:0.5rem 0;font-family:JetBrains Mono,monospace;"><div style="color:#2ecc71;font-size:0.72rem;font-weight:600;">VEHICULE CONFIGURE</div><div style="color:#94a3b8;font-size:0.75rem;margin-top:0.4rem;">COUT REEL / KM</div><div style="color:#e2e8f0;font-size:1.1rem;font-weight:600;">{r.cout_km_reel:.3f} EUR</div></div>', unsafe_allow_html=True)
    st.markdown('<div style="position:fixed;bottom:1rem;font-size:0.68rem;color:#475569;font-family:JetBrains Mono,monospace;">v0.2.0</div>', unsafe_allow_html=True)

if page == "Accueil":
    st.markdown('<div style="padding:3rem 0 1rem;text-align:center;"><div class="brand-name" style="font-size:2.5rem;">Transport<span>Pro</span></div><div style="color:#64748b;font-size:1.05rem;margin-top:0.8rem;max-width:520px;margin-left:auto;margin-right:auto;line-height:1.6;">Maitrisez vos couts. Pilotez vos marges.<br>L outil financier concu pour les transporteurs routiers.</div></div>', unsafe_allow_html=True)
    st.markdown("<div style='height:2rem;'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        st.markdown('<div style="border:1px solid rgba(30,58,95,0.4);border-radius:8px;padding:1.8rem;background:rgba(17,24,39,0.4);"><div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#2ecc71;font-weight:600;margin-bottom:0.8rem;">Gratuit</div><div style="font-size:1.15rem;font-weight:700;color:#e2e8f0;margin-bottom:0.8rem;">Calculateur Cout/km</div><div style="font-size:0.85rem;color:#94a3b8;line-height:1.6;">Calculez votre cout reel au kilometre avec la methode trinome du CNR.</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div style="border:1px solid rgba(30,58,95,0.4);border-radius:8px;padding:1.8rem;background:rgba(17,24,39,0.4);"><div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#1B6EC2;font-weight:600;margin-bottom:0.8rem;">Essentiel - 29 EUR/mois</div><div style="font-size:1.15rem;font-weight:700;color:#e2e8f0;margin-bottom:0.8rem;">Rentabilite Tournees</div><div style="font-size:0.85rem;color:#94a3b8;line-height:1.6;">Analysez chaque tournee et calculez vos marges.</div><div style="font-size:0.75rem;color:#475569;margin-top:0.8rem;font-style:italic;">Bientot disponible</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div style="border:1px solid rgba(30,58,95,0.4);border-radius:8px;padding:1.8rem;background:rgba(17,24,39,0.4);"><div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#e67e22;font-weight:600;margin-bottom:0.8rem;">Pro - 49 EUR/mois</div><div style="font-size:1.15rem;font-weight:700;color:#e2e8f0;margin-bottom:0.8rem;">Dashboard Financier</div><div style="font-size:0.85rem;color:#94a3b8;line-height:1.6;">FRNG, BFR, tresorerie nette et alertes automatiques.</div><div style="font-size:0.75rem;color:#475569;margin-top:0.8rem;font-style:italic;">Bientot disponible</div></div>', unsafe_allow_html=True)

elif page == "Calculateur Cout/km":
    from modules.calculateur import afficher_calculateur
    afficher_calculateur()
elif page == "Rentabilite Tournees":
    from modules.rentabilite import afficher_rentabilite
    afficher_rentabilite()
elif page == "Dashboard Financier":
    from modules.dashboard import afficher_dashboard
    afficher_dashboard()
