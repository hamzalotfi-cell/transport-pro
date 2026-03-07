"""
TransportCost Pro - Application principale
"""
import streamlit as st

st.set_page_config(page_title="TransportCost Pro", page_icon="🚛", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    .stApp { font-family: 'DM Sans', sans-serif; }
    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a1225 0%, #0f1d33 100%);
        border-right: 1px solid rgba(77,163,255,0.15);
    }
    [data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.7rem; font-weight: 600;
    }
    [data-testid="stMetricLabel"] {
        font-size: 0.78rem; text-transform: uppercase;
        letter-spacing: 0.06em; color: #8899aa !important;
    }
    div[data-testid="metric-container"] {
        background: rgba(15, 30, 55, 0.6);
        border: 1px solid rgba(77,163,255,0.15);
        border-radius: 8px; padding: 1rem 1.2rem;
    }
    .stFormSubmitButton > button {
        background: linear-gradient(135deg, #1B6EC2 0%, #2980d9 100%);
        color: white; font-family: 'DM Sans', sans-serif;
        font-size: 0.95rem; font-weight: 600;
        padding: 0.65rem 2rem; border: none; border-radius: 8px;
    }
    .stFormSubmitButton > button:hover {
        background: linear-gradient(135deg, #2980d9 0%, #3498db 100%);
        box-shadow: 0 4px 15px rgba(27, 110, 194, 0.3);
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
    .brand-name span { color: #5cb8ff; }
    .section-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.12em; color: #64748b; font-weight: 600; margin-bottom: 0.5rem; }
</style>
""", unsafe_allow_html=True)

from modules.auth import verifier_connexion, afficher_login, deconnecter

if not verifier_connexion():
    if "nav_page" not in st.session_state:
        st.session_state["nav_page"] = "Accueil"

    # Sidebar avec bouton connexion
    with st.sidebar:
        st.markdown('<div style="text-align:center;padding:1.2rem 0;"><div class="brand-name">Transport<span>Cost</span> Pro</div><div style="width:40px;height:2px;background:#5cb8ff;margin:0.8rem auto;"></div><div style="font-size:0.68rem;color:#64748b;text-transform:uppercase;letter-spacing:0.15em;">Simulateur de rentabilite</div></div>', unsafe_allow_html=True)
        st.divider()
        if st.button("Se connecter", use_container_width=True, type="primary"):
            st.session_state["show_login"] = True
            st.rerun()
        st.markdown('<div style="font-size:0.78rem;color:#64748b;text-align:center;margin-top:0.5rem;">Gratuit - Sans mot de passe</div>', unsafe_allow_html=True)

    if st.session_state.get("show_login"):
        afficher_login()
    else:
        from modules.landing import afficher_landing
        afficher_landing()

else:
    user = st.session_state["user"]
    if "nav_page" not in st.session_state:
        st.session_state["nav_page"] = "Accueil"

    with st.sidebar:
        st.markdown(f'<div style="text-align:center;padding:1.2rem 0;"><div class="brand-name">Transport<span>Cost</span> Pro</div><div style="width:40px;height:2px;background:#5cb8ff;margin:0.8rem auto;"></div><div style="font-size:0.68rem;color:#64748b;text-transform:uppercase;letter-spacing:0.15em;">Simulateur de rentabilite</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align:center;padding:0.3rem 0.7rem;background:rgba(46,204,113,0.1);border:1px solid rgba(46,204,113,0.2);border-radius:6px;margin-bottom:0.8rem;"><div style="font-size:0.72rem;color:#2ecc71;font-weight:600;">CONNECTE</div><div style="font-size:0.8rem;color:#e2e8f0;margin-top:0.2rem;">{user.get("email","")}</div></div>', unsafe_allow_html=True)

        pages = ["Accueil", "Calculateur Cout/km", "Rentabilite Tournees", "Dashboard Financier"]
        for p in pages:
            is_active = st.session_state["nav_page"] == p
            if st.button(p, key=f"nav_{p}", use_container_width=True, type="primary" if is_active else "secondary"):
                st.session_state["nav_page"] = p
                st.rerun()

        st.divider()
        if "resultat_km" in st.session_state:
            r = st.session_state["resultat_km"]
            st.markdown(f'<div style="font-family:JetBrains Mono,monospace;"><div style="color:#94a3b8;font-size:0.75rem;">COUT REEL / KM</div><div style="color:#e2e8f0;font-size:1.1rem;font-weight:600;">{r.cout_km_reel:.3f} EUR</div></div>', unsafe_allow_html=True)

        st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
        if st.button("Deconnexion", use_container_width=True):
            deconnecter()
        st.markdown('<div style="position:fixed;bottom:1rem;font-size:0.68rem;color:#475569;font-family:JetBrains Mono,monospace;">v1.0</div>', unsafe_allow_html=True)

    page = st.session_state["nav_page"]
    if page == "Accueil":
        from modules.landing import afficher_landing
        afficher_landing()
    elif page == "Calculateur Cout/km":
        from modules.calculateur import afficher_calculateur
        afficher_calculateur()
    elif page == "Rentabilite Tournees":
        from modules.rentabilite import afficher_rentabilite
        afficher_rentabilite()
    elif page == "Dashboard Financier":
        from modules.dashboard import afficher_dashboard
        afficher_dashboard()
