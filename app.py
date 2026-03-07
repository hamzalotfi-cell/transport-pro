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

    /* NAV BUTTONS */
    .nav-btn {
        display: block;
        width: 100%;
        padding: 0.9rem 1rem;
        margin-bottom: 0.5rem;
        border-radius: 8px;
        text-decoration: none;
        transition: all 0.2s ease;
        cursor: pointer;
        border: 1px solid transparent;
        background-size: cover;
        background-position: center;
        position: relative;
        overflow: hidden;
    }
    .nav-btn::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        border-radius: 8px;
    }
    .nav-btn-content {
        position: relative;
        z-index: 1;
    }
    .nav-btn-title {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.85rem;
        font-weight: 600;
        color: #e2e8f0;
    }
    .nav-btn-desc {
        font-size: 0.7rem;
        color: #94a3b8;
        margin-top: 0.15rem;
    }
    .nav-btn-active {
        border-color: rgba(77,163,255,0.4) !important;
        background-color: rgba(27,110,194,0.12) !important;
    }
    .nav-btn-active .nav-btn-title { color: #5cb8ff; }
</style>
""", unsafe_allow_html=True)

# Navigation state
if "nav_page" not in st.session_state:
    st.session_state["nav_page"] = "Accueil"

with st.sidebar:
    st.markdown('<div style="text-align:center;padding:1.2rem 0;"><div class="brand-name">Transport<span>Cost</span> Pro</div><div style="width:40px;height:2px;background:#5cb8ff;margin:0.8rem auto;"></div><div style="font-size:0.68rem;color:#64748b;text-transform:uppercase;letter-spacing:0.15em;">Simulateur de rentabilite transport</div></div>', unsafe_allow_html=True)
    st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)

    pages = {
        "Accueil": ("Accueil", "Presentation de l outil"),
        "Calculateur Cout/km": ("Calculateur Cout/km", "Cout reel par kilometre"),
        "Rentabilite Tournees": ("Rentabilite Tournees", "Marge par mission"),
        "Dashboard Financier": ("Dashboard Financier", "Sante de l entreprise"),
    }

    for key, (title, desc) in pages.items():
        is_active = st.session_state["nav_page"] == key
        if st.button(
            f"{title}",
            key=f"nav_{key}",
            use_container_width=True,
            type="primary" if is_active else "secondary",
        ):
            st.session_state["nav_page"] = key
            st.rerun()

    st.divider()

    if "resultat_km" in st.session_state:
        r = st.session_state["resultat_km"]
        st.markdown(f'<div style="padding:0.5rem 0;font-family:JetBrains Mono,monospace;"><div style="color:#2ecc71;font-size:0.72rem;font-weight:600;">VEHICULE CONFIGURE</div><div style="color:#94a3b8;font-size:0.75rem;margin-top:0.4rem;">COUT REEL / KM</div><div style="color:#e2e8f0;font-size:1.1rem;font-weight:600;">{r.cout_km_reel:.3f} EUR</div></div>', unsafe_allow_html=True)

    st.markdown('<div style="position:fixed;bottom:1rem;font-size:0.68rem;color:#475569;font-family:JetBrains Mono,monospace;">v1.0</div>', unsafe_allow_html=True)

# Routing
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
