"""
TransportCost Pro
"""
import streamlit as st

st.set_page_config(page_title="TransportCost Pro", page_icon="🚛", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    .stApp { font-family: 'DM Sans', sans-serif; }
    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0f1e 0%, #111a2e 100%);
        border-right: 1px solid rgba(59,130,246,0.1);
    }
    [data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.7rem; font-weight: 600; color: #f1f5f9;
    }
    [data-testid="stMetricLabel"] {
        font-size: 0.78rem; text-transform: uppercase;
        letter-spacing: 0.06em; color: #94a3b8 !important;
    }
    div[data-testid="metric-container"] {
        background: rgba(30,41,59,0.5);
        border: 1px solid rgba(59,130,246,0.1);
        border-radius: 10px; padding: 1rem 1.2rem;
    }
    .stFormSubmitButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white; font-family: 'DM Sans', sans-serif;
        font-size: 0.95rem; font-weight: 600;
        padding: 0.65rem 2rem; border: none; border-radius: 8px;
        box-shadow: 0 2px 8px rgba(59,130,246,0.2);
    }
    .stFormSubmitButton > button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        box-shadow: 0 4px 15px rgba(59,130,246,0.35);
    }
    .stNumberInput > div > div > input {
        font-family: 'JetBrains Mono', monospace; font-size: 0.9rem;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding-top: 1.5rem; max-width: 1200px; }
    hr { border-color: rgba(59,130,246,0.08); }

    .brand-name { font-family: 'DM Sans', sans-serif; font-size: 1.5rem; font-weight: 700; color: #f1f5f9; letter-spacing: -0.03em; }
    .brand-name span { color: #f59e0b; }
    .section-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.12em; color: #94a3b8; font-weight: 600; margin-bottom: 0.5rem; }
</style>
""", unsafe_allow_html=True)

from modules.auth import verifier_connexion, afficher_login, deconnecter

if not verifier_connexion():
    if "nav_page" not in st.session_state:
        st.session_state["nav_page"] = "Accueil"
    with st.sidebar:
        st.markdown('<div style="text-align:center;padding:1.2rem 0;"><div class="brand-name">Transport<span>Cost</span> Pro</div><div style="width:40px;height:2px;background:linear-gradient(90deg,#3b82f6,#f59e0b);margin:0.8rem auto;"></div><div style="font-size:0.68rem;color:#64748b;text-transform:uppercase;letter-spacing:0.15em;">Simulateur de rentabilite</div></div>', unsafe_allow_html=True)
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
        st.markdown('<div style="text-align:center;padding:1.2rem 0;"><div class="brand-name">Transport<span>Cost</span> Pro</div><div style="width:40px;height:2px;background:linear-gradient(90deg,#3b82f6,#f59e0b);margin:0.8rem auto;"></div><div style="font-size:0.68rem;color:#64748b;text-transform:uppercase;letter-spacing:0.15em;">Simulateur de rentabilite</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align:center;padding:0.4rem 0.7rem;background:rgba(245,158,11,0.08);border:1px solid rgba(245,158,11,0.2);border-radius:8px;margin-bottom:1rem;"><div style="font-size:0.72rem;color:#f59e0b;font-weight:600;letter-spacing:0.05em;">CONNECTE</div><div style="font-size:0.82rem;color:#f1f5f9;margin-top:0.2rem;">{user.get("email","")}</div></div>', unsafe_allow_html=True)

        pages = ["Accueil", "Calculateur Cout/km", "Rentabilite Tournees", "Dashboard Financier"]
        for p in pages:
            is_active = st.session_state["nav_page"] == p
            if st.button(p, key=f"nav_{p}", use_container_width=True, type="primary" if is_active else "secondary"):
                st.session_state["nav_page"] = p
                st.rerun()

        st.divider()
        if "resultat_km" in st.session_state:
            r = st.session_state["resultat_km"]
            st.markdown(f'<div style="font-family:JetBrains Mono,monospace;padding:0.5rem 0;"><div style="color:#94a3b8;font-size:0.72rem;letter-spacing:0.08em;">COUT REEL / KM</div><div style="color:#f59e0b;font-size:1.2rem;font-weight:600;">{r.cout_km_reel:.3f} EUR</div></div>', unsafe_allow_html=True)

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
