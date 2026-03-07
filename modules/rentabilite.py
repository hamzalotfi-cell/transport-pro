"""
TransportPro — Module 2 : Analyse de Rentabilité par Tournée
Module payant : analyse de chaque tournée + seuil de rentabilité.
"""

import streamlit as st


def afficher_rentabilite():
    """Affiche l'interface du module de rentabilité par tournée."""

    st.markdown(
        """
        <div style="text-align: center; padding: 1rem 0;">
            <h1 style="color: #1B6EC2; margin-bottom: 0.2rem;">
                📈 Rentabilité par Tournée
            </h1>
            <p style="color: #aaa; font-size: 1.1rem;">
                Analysez la rentabilité de chaque tournée et trouvez votre seuil de rentabilité
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # Vérifier si un profil véhicule existe
    if "resultat_km" not in st.session_state:
        st.warning(
            "⚠️ Vous devez d'abord calculer votre coût kilométrique dans le **Calculateur** "
            "pour pouvoir analyser la rentabilité de vos tournées."
        )
        return

    st.info(
        "🔒 **Module Premium** — Ce module sera disponible avec l'abonnement Essentiel (29€/mois). "
        "Il vous permettra de :\n\n"
        "- Saisir chaque tournée et calculer automatiquement sa marge\n"
        "- Voir un indicateur couleur de rentabilité (🟢🟡🟠🔴)\n"
        "- Calculer votre seuil de rentabilité mensuel et annuel\n"
        "- Identifier vos clients les plus et les moins rentables\n"
        "- Suivre l'évolution de vos marges dans le temps"
    )

    # Preview de ce que ça donnera
    st.markdown("---")
    st.subheader("🔍 Aperçu du module")

    r = st.session_state["resultat_km"]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("CK utilisé", f"{r.ck:.4f} €/km")
    with col2:
        st.metric("CC utilisé", f"{r.cc:.2f} €/h")
    with col3:
        st.metric("CJ utilisé", f"{r.cj:.2f} €/jour")

    st.markdown(
        "*Ces valeurs du trinôme CNR seront utilisées pour calculer le coût de chaque tournée.*"
    )
