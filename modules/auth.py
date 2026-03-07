"""
TransportCost Pro - Authentification simple par email
"""
import streamlit as st
from utils.database import get_ou_creer_utilisateur


def afficher_login():
    st.markdown("""
    <div style="text-align:center;padding:3rem 0 1rem;">
        <div class="brand-name" style="font-size:2rem;">Transport<span>Cost</span> Pro</div>
        <div style="color:#64748b;font-size:0.95rem;margin-top:0.8rem;">Connectez-vous pour sauvegarder vos donnees</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        with st.form("login_form"):
            email = st.text_input("Votre email professionnel", placeholder="contact@montransport.fr")
            nom = st.text_input("Nom de votre entreprise (optionnel)", placeholder="Transport Dupont")
            submitted = st.form_submit_button("Se connecter", use_container_width=True, type="primary")

        if submitted and email:
            if "@" not in email or "." not in email:
                st.error("Veuillez entrer un email valide.")
            else:
                user = get_ou_creer_utilisateur(email, nom)
                if user:
                    st.session_state["user"] = user
                    st.session_state["nav_page"] = "Accueil"
                    st.rerun()
                else:
                    st.error("Erreur de connexion. Reessayez.")

        st.markdown("""
        <div style="text-align:center;margin-top:1.5rem;font-size:0.82rem;color:#64748b;">
            Pas de mot de passe. Entrez votre email pour acceder a votre espace.<br>
            Vos donnees sont sauvegardees automatiquement.
        </div>
        """, unsafe_allow_html=True)


def verifier_connexion():
    return "user" in st.session_state and st.session_state["user"] is not None


def deconnecter():
    if "user" in st.session_state:
        del st.session_state["user"]
    st.rerun()
